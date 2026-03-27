"""PDF metadata extraction and page analysis using PyMuPDF (fitz).

Provides the ``PdfInfo`` class that wraps a single PDF file and exposes
helpers consumed by the rest of the conversion pipeline.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
from PIL import Image

from doc_to_markdown.config import (
    MAX_CHAPTER_PAGES,
    MIN_CHAPTER_PAGES,
    MAX_CHAPTER_COUNT,
)


class PdfInfo:
    """Analyse a PDF file for the conversion pipeline.

    Parameters
    ----------
    pdf_path:
        Filesystem path to the PDF file.

    Raises
    ------
    FileNotFoundError
        If *pdf_path* does not point to an existing file.
    RuntimeError
        If PyMuPDF cannot open the file (corrupt / unsupported format).
    """

    def __init__(self, pdf_path: str) -> None:
        path = Path(pdf_path)
        if not path.is_file():
            raise FileNotFoundError(
                f"PDF file not found: {pdf_path}"
            )

        try:
            self._doc: fitz.Document = fitz.open(str(path))
        except Exception as exc:
            raise RuntimeError(
                f"Failed to open PDF '{pdf_path}': {exc}"
            ) from exc

        self._path = path

    # ------------------------------------------------------------------
    # Basic properties
    # ------------------------------------------------------------------

    @property
    def page_count(self) -> int:
        """Total number of pages in the PDF."""
        return self._doc.page_count

    def is_encrypted(self) -> bool:
        """Return *True* if the PDF is encrypted (even if already authenticated)."""
        return self._doc.is_encrypted

    # ------------------------------------------------------------------
    # TOC helpers
    # ------------------------------------------------------------------

    def get_toc(self) -> list[dict[str, Any]]:
        """Extract the table-of-contents from PDF metadata.

        Returns a list of dicts, each with keys ``title``, ``level`` and
        ``page_num`` (0-indexed).
        """
        raw_toc = self._doc.get_toc(simple=True)  # [[level, title, page], ...]
        entries: list[dict[str, Any]] = []
        for level, title, page_1based in raw_toc:
            entries.append(
                {
                    "title": title.strip(),
                    "level": int(level),
                    "page_num": max(int(page_1based) - 1, 0),  # 0-indexed
                }
            )
        return entries

    # ------------------------------------------------------------------
    # Chapter computation
    # ------------------------------------------------------------------

    def get_chapters(self) -> list[dict[str, Any]]:
        """Compute chapter boundaries suitable for splitting the PDF.

        Rules
        -----
        1. Use **level-1** TOC entries as primary chapter boundaries.
        2. If the TOC is empty, fall back to scanning for large-font headings.
        3. Chapters exceeding *MAX_CHAPTER_PAGES* are subdivided at the next
           level-2 headings inside them.
        4. Chapters shorter than *MIN_CHAPTER_PAGES* are merged with the
           previous chapter (unless it is an appendix).
        5. Entries whose title starts with ``"Appendix"`` always stay separate.
        6. A warning is printed if the resulting chapter count exceeds
           *MAX_CHAPTER_COUNT*.

        Returns
        -------
        list[dict]
            Each dict has keys ``title``, ``start_page`` and ``end_page``
            (0-indexed, inclusive).
        """
        toc = self.get_toc()
        total_pages = self.page_count

        if toc:
            chapters = self._chapters_from_toc(toc, total_pages)
        else:
            chapters = self._chapters_from_headings(total_pages)

        # --- Split oversized chapters ------------------------------------
        chapters = self._split_large_chapters(chapters, toc)

        # --- Merge tiny chapters -----------------------------------------
        chapters = self._merge_small_chapters(chapters)

        if len(chapters) > MAX_CHAPTER_COUNT:
            print(
                f"[pdf_parser] WARNING: {len(chapters)} chapters detected "
                f"(threshold is {MAX_CHAPTER_COUNT})."
            )

        return chapters

    # -- private helpers --------------------------------------------------

    @staticmethod
    def _chapters_from_toc(
        toc: list[dict[str, Any]],
        total_pages: int,
    ) -> list[dict[str, Any]]:
        """Build chapter list from level-1 TOC entries."""
        level1 = [e for e in toc if e["level"] == 1]
        if not level1:
            # No level-1 entries; promote everything to chapters.
            level1 = toc

        chapters: list[dict[str, Any]] = []
        for idx, entry in enumerate(level1):
            start = entry["page_num"]
            if idx + 1 < len(level1):
                end = level1[idx + 1]["page_num"] - 1
            else:
                end = total_pages - 1
            # Clamp
            end = max(end, start)
            chapters.append(
                {
                    "title": entry["title"],
                    "start_page": start,
                    "end_page": end,
                }
            )
        return chapters

    def _chapters_from_headings(
        self, total_pages: int
    ) -> list[dict[str, Any]]:
        """Fallback: scan every page for large-font lines and treat them as
        chapter boundaries."""
        boundaries: list[dict[str, Any]] = []

        for page_num in range(total_pages):
            page = self._doc[page_num]
            blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)[
                "blocks"
            ]
            for block in blocks:
                if block.get("type") != 0:  # text block
                    continue
                for line in block.get("lines", []):
                    max_size = max(
                        (span["size"] for span in line.get("spans", [])),
                        default=0.0,
                    )
                    text = "".join(
                        span["text"] for span in line.get("spans", [])
                    ).strip()
                    # Heuristic: font size >= 18 pt and non-empty text that
                    # looks like a heading (starts with a digit or uppercase).
                    if max_size >= 18.0 and text and (
                        text[0].isdigit() or text[0].isupper()
                    ):
                        # Avoid duplicates on the same page
                        if not boundaries or boundaries[-1]["page_num"] != page_num:
                            boundaries.append(
                                {"title": text, "page_num": page_num}
                            )
                        break  # one heading per page is enough
                else:
                    continue
                break  # already found heading in first qualifying block

        if not boundaries:
            # Ultimate fallback: treat the entire PDF as a single chapter.
            return [
                {
                    "title": "Full Document",
                    "start_page": 0,
                    "end_page": total_pages - 1,
                }
            ]

        chapters: list[dict[str, Any]] = []
        for idx, b in enumerate(boundaries):
            start = b["page_num"]
            end = (
                boundaries[idx + 1]["page_num"] - 1
                if idx + 1 < len(boundaries)
                else total_pages - 1
            )
            end = max(end, start)
            chapters.append(
                {"title": b["title"], "start_page": start, "end_page": end}
            )
        return chapters

    @staticmethod
    def _split_by_headings(
        ch: dict[str, Any],
        sub_headings: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Split a single chapter at the given sub-heading positions."""
        result: list[dict[str, Any]] = []
        prev_start = ch["start_page"]
        prev_title = ch["title"]

        for sub in sub_headings:
            sub_start = sub["page_num"]
            result.append(
                {
                    "title": prev_title,
                    "start_page": prev_start,
                    "end_page": sub_start - 1,
                }
            )
            prev_start = sub_start
            prev_title = sub["title"]

        result.append(
            {
                "title": prev_title,
                "start_page": prev_start,
                "end_page": ch["end_page"],
            }
        )
        return result

    @staticmethod
    def _split_evenly(ch: dict[str, Any], target_size: int = 30) -> list[dict[str, Any]]:
        """Split a chapter into roughly equal parts of ~target_size pages."""
        start = ch["start_page"]
        end = ch["end_page"]
        span = end - start + 1
        n_parts = max(2, (span + target_size - 1) // target_size)
        part_size = span // n_parts

        result: list[dict[str, Any]] = []
        for i in range(n_parts):
            part_start = start + i * part_size
            if i == n_parts - 1:
                part_end = end
            else:
                part_end = part_start + part_size - 1
            result.append(
                {
                    "title": f"{ch['title']} (Part {i + 1})",
                    "start_page": part_start,
                    "end_page": part_end,
                }
            )
        return result

    @staticmethod
    def _split_large_chapters(
        chapters: list[dict[str, Any]],
        toc_all: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Split any chapter that exceeds *MAX_CHAPTER_PAGES*.

        Tries, in order: level-2 headings, level-3 headings, even page split.
        """
        result: list[dict[str, Any]] = []

        for ch in chapters:
            span = ch["end_page"] - ch["start_page"] + 1
            if span <= MAX_CHAPTER_PAGES:
                result.append(ch)
                continue

            # Try level-2 entries first, then level-3
            split_done = False
            for level in (2, 3, 4):
                subs = [
                    e
                    for e in toc_all
                    if e["level"] == level
                    and ch["start_page"] < e["page_num"] <= ch["end_page"]
                ]
                if subs:
                    parts = PdfInfo._split_by_headings(ch, subs)
                    # Check if all parts are now small enough
                    max_part = max(p["end_page"] - p["start_page"] + 1 for p in parts)
                    if max_part <= MAX_CHAPTER_PAGES or level == 4:
                        result.extend(parts)
                        split_done = True
                        break
                    # If still too large, try next level

            if not split_done:
                # Fallback: even page split
                result.extend(PdfInfo._split_evenly(ch))

        return result

    @staticmethod
    def _is_appendix(title: str) -> bool:
        return title.strip().lower().startswith("appendix")

    @classmethod
    def _merge_small_chapters(
        cls,
        chapters: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Merge chapters with fewer than *MIN_CHAPTER_PAGES* pages into
        the preceding chapter.  Appendices are never merged."""
        if not chapters:
            return chapters

        merged: list[dict[str, Any]] = [chapters[0]]

        for ch in chapters[1:]:
            span = ch["end_page"] - ch["start_page"] + 1
            if span < MIN_CHAPTER_PAGES and not cls._is_appendix(ch["title"]):
                # Merge into previous chapter.
                merged[-1]["end_page"] = ch["end_page"]
            else:
                merged.append(ch)

        return merged

    # ------------------------------------------------------------------
    # Page-level analysis
    # ------------------------------------------------------------------

    def get_page_image_regions(
        self, page_num: int
    ) -> list[dict[str, Any]]:
        """Return image bounding-boxes on *page_num* (0-indexed).

        Each dict has keys ``bbox`` *(x0, y0, x1, y1)* and ``area``.
        """
        page = self._doc[page_num]
        image_list = page.get_images(full=True)
        regions: list[dict[str, Any]] = []

        for img_info in image_list:
            xref = img_info[0]
            rects = page.get_image_rects(xref)
            for rect in rects:
                if rect.is_empty or rect.is_infinite:
                    continue
                bbox = (rect.x0, rect.y0, rect.x1, rect.y1)
                area = abs(rect.width * rect.height)
                regions.append({"bbox": bbox, "area": area})

        return regions

    def page_has_tables(self, page_num: int) -> bool:
        """Heuristic check for whether *page_num* likely contains a table.

        Detection strategy (any one is sufficient):
        1. A high density of horizontal/vertical line drawings (grid lines).
        2. Text layout that resembles tabular structure (multiple
           whitespace-aligned columns).
        """
        page = self._doc[page_num]

        # --- Strategy 1: vector line drawings ----------------------------
        drawings = page.get_drawings()
        h_lines = 0
        v_lines = 0
        for path in drawings:
            for item in path.get("items", []):
                kind = item[0]
                if kind == "l":  # line segment
                    p1, p2 = item[1], item[2]
                    dx = abs(p1.x - p2.x) if hasattr(p1, "x") else abs(p1[0] - p2[0])
                    dy = abs(p1.y - p2.y) if hasattr(p1, "y") else abs(p1[1] - p2[1])
                    if dy < 2 and dx > 20:
                        h_lines += 1
                    elif dx < 2 and dy > 20:
                        v_lines += 1

        if h_lines >= 3 and v_lines >= 2:
            return True

        # --- Strategy 2: tabular text patterns ---------------------------
        text = page.get_text("text")
        lines = text.split("\n")
        multi_space_lines = 0
        for line in lines:
            # Lines with 2+ runs of 2+ spaces separating tokens hint at
            # column-aligned data.
            if len(re.findall(r" {2,}", line.strip())) >= 2:
                multi_space_lines += 1

        if multi_space_lines >= 4:
            return True

        return False

    def has_text_layer(self, page_num: int) -> bool:
        """Return *True* if the page has extractable text (i.e. is not a
        scan-only image page)."""
        page = self._doc[page_num]
        text = page.get_text("text").strip()
        return len(text) > 0

    def render_page(
        self, page_num: int, dpi: int = 200
    ) -> Image.Image:
        """Render *page_num* to a :class:`PIL.Image.Image`.

        Parameters
        ----------
        page_num:
            0-indexed page number.
        dpi:
            Resolution for the rasterisation (default 200).
        """
        page = self._doc[page_num]
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Explicitly close the underlying PDF document."""
        self._doc.close()

    def __enter__(self) -> PdfInfo:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f"PdfInfo(path={str(self._path)!r}, pages={self.page_count})"
        )
