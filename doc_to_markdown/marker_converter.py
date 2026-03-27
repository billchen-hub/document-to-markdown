"""Wrapper around marker-pdf for converting PDF pages to Markdown.

Uses marker-pdf v1.10.x API with paginated output to produce
per-page Markdown content suitable for downstream quality checking
and chapter assembly.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict

logger = logging.getLogger(__name__)

# Regex matching the page separator marker injected by marker-pdf
# when ``paginate_output=True``.  The format is:
#     {PAGE_NUMBER}\n------------------------------------------------
_PAGE_SEP_RE = re.compile(
    r"\n*\{(\d+)\}\n-{10,}\n*"
)


class MarkerConverter:
    """Thin wrapper around *marker-pdf* that exposes per-page Markdown output.

    Models are loaded once on construction and reused for every subsequent
    conversion call so that the expensive model-loading step is amortised
    across the pipeline.
    """

    def __init__(self) -> None:
        logger.info("Loading marker models (this may take a moment)...")
        self._model_dict = create_model_dict()
        logger.info("Marker models loaded successfully.")

    # --------------------------------------------------------------------- #
    #  Public API                                                            #
    # --------------------------------------------------------------------- #

    def convert_all(
        self,
        pdf_path: str,
        progress_callback=None,
    ) -> dict[int, str]:
        """Convert every page of *pdf_path* and return per-page Markdown.

        Parameters
        ----------
        pdf_path:
            Filesystem path to the source PDF.
        progress_callback:
            Optional callable ``(current_page, total_pages) -> None``
            invoked once per page to report progress.

        Returns
        -------
        dict[int, str]
            Mapping of 0-based page number to its Markdown text.
            Pages that produced no output are included with an empty string.
        """
        pdf_path = str(Path(pdf_path).resolve())

        converter = PdfConverter(
            config={
                "output_format": "markdown",
                "paginate_output": True,
            },
            artifact_dict=self._model_dict,
        )

        rendered = converter(pdf_path)
        full_markdown: str = rendered.markdown

        # Determine total page count.  ``rendered`` may expose a page count
        # attribute; otherwise we fall back to counting unique page markers.
        total_pages = self._detect_total_pages(rendered, full_markdown, pdf_path)

        pages = self._split_paginated_output(full_markdown, total_pages)

        # Fire progress callback for every page we extracted.
        if progress_callback is not None:
            for idx in range(total_pages):
                try:
                    progress_callback(idx, total_pages)
                except Exception:  # noqa: BLE001
                    logger.debug("progress_callback raised; ignoring")

        return pages

    def convert_pages(
        self,
        pdf_path: str,
        page_nums: list[int],
    ) -> dict[int, str]:
        """Convert only the specified pages of *pdf_path*.

        Parameters
        ----------
        pdf_path:
            Filesystem path to the source PDF.
        page_nums:
            List of 0-based page numbers to convert.

        Returns
        -------
        dict[int, str]
            Mapping of 0-based page number to its Markdown text for each
            requested page.  Pages that yielded no content map to ``""``.
        """
        if not page_nums:
            return {}

        pdf_path = str(Path(pdf_path).resolve())

        converter = PdfConverter(
            config={
                "output_format": "markdown",
                "paginate_output": True,
                "page_range": sorted(page_nums),
            },
            artifact_dict=self._model_dict,
        )

        rendered = converter(pdf_path)
        full_markdown: str = rendered.markdown

        raw_pages = self._split_paginated_output(
            full_markdown,
            total_pages=len(page_nums),
        )

        # ``raw_pages`` is keyed 0..N-1 from the split; remap to the
        # original requested page numbers.
        sorted_nums = sorted(page_nums)
        result: dict[int, str] = {}

        for local_idx, page_num in enumerate(sorted_nums):
            result[page_num] = raw_pages.get(local_idx, "")

        # Ensure every requested page is present even when marker returned
        # fewer chunks than expected.
        for page_num in page_nums:
            result.setdefault(page_num, "")

        return result

    # --------------------------------------------------------------------- #
    #  Internal helpers                                                      #
    # --------------------------------------------------------------------- #

    @staticmethod
    def _detect_total_pages(
        rendered: object,
        full_markdown: str,
        pdf_path: str,
    ) -> int:
        """Best-effort detection of the total number of pages.

        Tries, in order:
        1. ``rendered.metadata.total_pages``
        2. Count of unique page separator markers in the output.
        3. PyMuPDF as an independent fallback.
        4. ``1`` as a last resort.
        """
        # 1. Metadata on the rendered object.
        metadata = getattr(rendered, "metadata", None)
        if metadata is not None:
            tp = getattr(metadata, "total_pages", None)
            if tp is not None and isinstance(tp, int) and tp > 0:
                return tp

        # 2. Count page separator markers.
        markers = _PAGE_SEP_RE.findall(full_markdown)
        if markers:
            # Page numbers in markers are typically 1-based.
            return max(int(m) for m in markers)

        # 3. PyMuPDF fallback.
        try:
            import fitz  # type: ignore[import-untyped]

            with fitz.open(pdf_path) as doc:
                return doc.page_count
        except Exception:  # noqa: BLE001
            pass

        # 4. Absolute fallback.
        logger.warning("Could not determine page count; defaulting to 1.")
        return 1

    @staticmethod
    def _split_paginated_output(
        full_markdown: str,
        total_pages: int,
    ) -> dict[int, str]:
        """Split marker's paginated output into per-page Markdown chunks.

        When ``paginate_output=True`` marker inserts separators of the form::

            {PAGE_NUMBER}
            ------------------------------------------------

        between pages.  We split on those markers and map each chunk to its
        0-based page index.

        If the output contains no recognisable page separators (e.g. a
        single-page PDF), the entire text is assigned to page 0.
        """
        parts = _PAGE_SEP_RE.split(full_markdown)

        result: dict[int, str] = {}

        if len(parts) == 1:
            # No page separator found — treat everything as page 0.
            result[0] = parts[0].strip()
        else:
            # ``re.split`` with a capturing group interleaves text and the
            # captured group values:
            #   [text_before_first_sep, page_num_1, text_1, page_num_2, text_2, ...]
            # The leading chunk (before the first separator) belongs to
            # page 0 if there is no explicit marker for it.

            leading_text = parts[0].strip()
            idx = 1  # start after the leading text

            if leading_text:
                result[0] = leading_text

            while idx < len(parts) - 1:
                try:
                    page_num_1based = int(parts[idx])
                except (ValueError, TypeError):
                    idx += 1
                    continue
                page_text = parts[idx + 1].strip() if idx + 1 < len(parts) else ""
                page_index = page_num_1based - 1  # convert to 0-based
                result[page_index] = page_text
                idx += 2

        # Fill in any missing pages so callers always get a contiguous dict.
        for i in range(total_pages):
            result.setdefault(i, "")

        return result
