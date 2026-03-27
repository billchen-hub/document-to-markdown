"""Quality checking for Marker-converted Markdown output.

Layer 1: Rule-based checks (no API needed) - garbled text, empty tables,
         missing images, too-short content, broken formatting.
Layer 2: Sampling comparison (Vision API) - randomly samples pages and
         compares Marker output against Vision API output.
"""
from __future__ import annotations

import logging
import random
import re

from doc_to_markdown.config import (
    CATEGORY_FAIL_THRESHOLD,
    GARBLED_CHAR_THRESHOLD,
    MIN_PAGE_CONTENT_LENGTH,
    SAMPLING_PAGE_COUNT,
    SAMPLING_SIMILARITY_THRESHOLD,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# CJK Unified Ideographs and common CJK ranges
_CJK_RANGES = (
    (0x2E80, 0x2EFF),   # CJK Radicals Supplement
    (0x2F00, 0x2FDF),   # Kangxi Radicals
    (0x3000, 0x303F),   # CJK Symbols and Punctuation
    (0x3040, 0x309F),   # Hiragana
    (0x30A0, 0x30FF),   # Katakana
    (0x3100, 0x312F),   # Bopomofo
    (0x3130, 0x318F),   # Hangul Compatibility Jamo
    (0x31F0, 0x31FF),   # Katakana Phonetic Extensions
    (0x3200, 0x32FF),   # Enclosed CJK Letters and Months
    (0x3300, 0x33FF),   # CJK Compatibility
    (0x3400, 0x4DBF),   # CJK Unified Ideographs Extension A
    (0x4E00, 0x9FFF),   # CJK Unified Ideographs
    (0xA000, 0xA48F),   # Yi Syllables
    (0xAC00, 0xD7AF),   # Hangul Syllables
    (0xF900, 0xFAFF),   # CJK Compatibility Ideographs
    (0xFE30, 0xFE4F),   # CJK Compatibility Forms
    (0x1F000, 0x1F9FF), # Emoticons / Symbols & Pictographs
    (0x20000, 0x2A6DF), # CJK Unified Ideographs Extension B
    (0x2A700, 0x2B73F), # CJK Unified Ideographs Extension C
    (0x2B740, 0x2B81F), # CJK Unified Ideographs Extension D
)

# Common whitespace / newline characters that should never count as garbled
_WHITESPACE = {0x09, 0x0A, 0x0D}  # tab, LF, CR


def _is_common_unicode(cp: int) -> bool:
    """Return True if the codepoint is in a common Unicode range (CJK, etc.)."""
    for lo, hi in _CJK_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def _is_acceptable_char(cp: int) -> bool:
    """Return True if the codepoint is printable ASCII, whitespace, or common unicode."""
    # Printable ASCII: 0x20 (space) through 0x7E (~)
    if 0x20 <= cp <= 0x7E:
        return True
    # Whitespace characters we tolerate
    if cp in _WHITESPACE:
        return True
    # Common unicode (CJK, etc.)
    if _is_common_unicode(cp):
        return True
    return False


# ---------------------------------------------------------------------------
# QualityChecker
# ---------------------------------------------------------------------------

class QualityChecker:
    """Performs rule-based and sampling-based quality checks on Markdown output."""

    # ------------------------------------------------------------------ #
    # Layer 1 - individual rule checks
    # ------------------------------------------------------------------ #

    def check_garbled(self, text: str) -> bool:
        """Return True if the ratio of suspicious characters exceeds the threshold.

        Suspicious characters are those outside printable ASCII (0x20-0x7E),
        common whitespace, and well-known Unicode ranges (CJK, Hangul, etc.).
        Focuses on control characters and replacement characters (U+FFFD).
        """
        if not text:
            return False

        total = len(text)
        bad = sum(1 for ch in text if not _is_acceptable_char(ord(ch)))
        ratio = bad / total
        return ratio > GARBLED_CHAR_THRESHOLD

    def check_empty_table(self, text: str) -> bool:
        """Return True if the markdown contains table headers but no data rows.

        A table header separator looks like ``| --- | --- |``.  Data rows are
        subsequent lines starting with ``|`` that are *not* separator lines.
        """
        lines = text.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Detect separator row (e.g. |---|---|)
            if re.match(r"^\|[\s\-:|]+\|$", line):
                # Walk backwards to find the header row
                # Walk forwards to see if any data rows follow
                has_data = False
                for j in range(i + 1, len(lines)):
                    following = lines[j].strip()
                    if not following:
                        # blank line ends the table
                        break
                    if following.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", following):
                        has_data = True
                        break
                    if not following.startswith("|"):
                        break
                if not has_data:
                    return True
            i += 1
        return False

    def check_image_missing(self, text: str, has_images: bool) -> bool:
        """Return True if the PDF page has images but the markdown has none.

        Checks for ``![...](...)``, ``<img`` tags, and ``[image`` / ``[Image``
        description brackets that some converters produce.
        """
        if not has_images:
            return False

        # Standard markdown image syntax
        if re.search(r"!\[.*?\]", text):
            return False
        # HTML image tags
        if re.search(r"<img\s", text, re.IGNORECASE):
            return False
        # Description brackets mentioning images
        if re.search(r"\[\s*[Ii]mage", text):
            return False

        return True

    def check_too_short(self, text: str) -> bool:
        """Return True if stripped content length is below the minimum threshold."""
        return len(text.strip()) < MIN_PAGE_CONTENT_LENGTH

    def check_format_broken(self, text: str) -> bool:
        """Return True if the markdown has structural formatting issues.

        Detects:
        - Unclosed table rows (lines starting with ``|`` but not ending with ``|``)
        - Orphaned heading markers (``#`` at start of line with no text after)
        - Badly nested lists (indentation jumps by more than 4 spaces at once)
        """
        lines = text.split("\n")

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            # --- Unclosed table rows ---
            if stripped.startswith("|") and not stripped.endswith("|"):
                # Ignore separator lines that might be malformed
                if not re.match(r"^\|[\s\-:|]+$", stripped):
                    return True

            # --- Orphaned heading markers ---
            heading_match = re.match(r"^(#{1,6})\s*$", stripped)
            if heading_match:
                return True

        # --- Badly nested lists ---
        prev_indent = 0
        in_list = False
        for line in lines:
            if not line.strip():
                in_list = False
                prev_indent = 0
                continue

            list_match = re.match(r"^(\s*)([-*+]|\d+\.)\s", line)
            if list_match:
                indent = len(list_match.group(1))
                if in_list and indent > prev_indent and (indent - prev_indent) > 4:
                    return True
                in_list = True
                prev_indent = indent
            else:
                # Non-list line resets tracking only if it's not a continuation
                if not line.startswith(" " * (prev_indent + 2)):
                    in_list = False
                    prev_indent = 0

        return False

    # ------------------------------------------------------------------ #
    # Layer 1 - aggregate per-page check
    # ------------------------------------------------------------------ #

    def check_page(
        self,
        page_num: int,
        markdown: str,
        has_images: bool,
        has_tables: bool,
    ) -> dict:
        """Run all rule-based checks on a single page.

        Returns
        -------
        dict
            ``{"pass": bool, "issues": [{"reason": str, "action": str}]}``
            where *action* is ``"redo"`` or ``"vision_describe"``.
        """
        issues: list[dict[str, str]] = []

        if self.check_garbled(markdown):
            issues.append({"reason": "garbled_text", "action": "redo"})

        if self.check_too_short(markdown):
            issues.append({"reason": "too_short", "action": "redo"})

        if has_tables and self.check_empty_table(markdown):
            issues.append({"reason": "empty_table", "action": "redo"})

        if self.check_image_missing(markdown, has_images):
            issues.append({"reason": "image_missing", "action": "vision_describe"})

        if self.check_format_broken(markdown):
            issues.append({"reason": "format_broken", "action": "redo"})

        return {"pass": len(issues) == 0, "issues": issues}

    # ------------------------------------------------------------------ #
    # Layer 1 - check all pages
    # ------------------------------------------------------------------ #

    def check_all_pages(
        self,
        marker_results: dict[int, str],
        pdf_info,
    ) -> dict:
        """Run rule-based checks on every page and aggregate results.

        Parameters
        ----------
        marker_results:
            Mapping of page number to Markdown text.
        pdf_info:
            Object providing ``get_page_image_regions()`` and
            ``page_has_tables()`` for each page.

        Returns
        -------
        dict
            ``{"total_pages": int, "passed": int,
              "needs_redo": [...], "needs_vision_describe": [...]}``
        """
        total = len(marker_results)
        passed = 0
        needs_redo: list[dict] = []
        needs_vision_describe: list[dict] = []

        for page_num, markdown in sorted(marker_results.items()):
            has_images = bool(pdf_info.get_page_image_regions(page_num))
            has_tables = pdf_info.page_has_tables(page_num)

            result = self.check_page(page_num, markdown, has_images, has_tables)

            if result["pass"]:
                passed += 1
            else:
                for issue in result["issues"]:
                    entry = {"page": page_num, "reason": issue["reason"]}
                    if issue["action"] == "redo":
                        needs_redo.append(entry)
                    elif issue["action"] == "vision_describe":
                        needs_vision_describe.append(entry)

        return {
            "total_pages": total,
            "passed": passed,
            "needs_redo": needs_redo,
            "needs_vision_describe": needs_vision_describe,
        }

    # ------------------------------------------------------------------ #
    # Layer 2 - Sampling comparison via Vision API
    # ------------------------------------------------------------------ #

    def sample_and_compare(
        self,
        pdf_info,
        marker_results: dict[int, str],
        vision_converter,
        sample_count: int | None = None,
        progress_callback=None,
    ) -> dict:
        """Sample pages and compare Marker output vs Vision API output.

        Pages are categorised into *table*, *image*, and *text* buckets.
        Samples are drawn proportionally from each category.  Each sampled
        page is sent to ``vision_converter.compare_outputs()`` which returns
        a similarity score in [0, 1].  Pages scoring below
        ``SAMPLING_SIMILARITY_THRESHOLD`` are flagged.

        Parameters
        ----------
        pdf_info:
            Object with ``get_page_image_regions(page_num)`` and
            ``page_has_tables(page_num)`` methods.
        marker_results:
            Mapping of page number to Markdown string.
        vision_converter:
            Object with a ``compare_outputs(page_num, markdown)`` method that
            returns a float similarity score.
        sample_count:
            Number of pages to sample.  Defaults to ``SAMPLING_PAGE_COUNT``.

        Returns
        -------
        dict
            See class docstring for schema.
        """
        if sample_count is None:
            sample_count = SAMPLING_PAGE_COUNT

        all_pages = sorted(marker_results.keys())
        total_pages = len(all_pages)

        # ---- Categorise pages ---- #
        table_pages: list[int] = []
        image_pages: list[int] = []
        text_pages: list[int] = []

        for pn in all_pages:
            has_tables = pdf_info.page_has_tables(pn)
            has_images = bool(pdf_info.get_page_image_regions(pn))
            if has_tables:
                table_pages.append(pn)
            elif has_images:
                image_pages.append(pn)
            else:
                text_pages.append(pn)

        # ---- Proportional sampling ---- #
        sample_count = min(sample_count, total_pages)

        def _proportional_sample(bucket: list[int], total: int, n: int) -> list[int]:
            if total == 0 or not bucket:
                return []
            share = max(1, round(len(bucket) / total * n))
            share = min(share, len(bucket))
            return random.sample(bucket, share)

        sampled_tables = _proportional_sample(table_pages, total_pages, sample_count)
        sampled_images = _proportional_sample(image_pages, total_pages, sample_count)
        sampled_text = _proportional_sample(text_pages, total_pages, sample_count)

        # Trim to exact sample_count if we overshoot due to rounding
        sampled = sampled_tables + sampled_images + sampled_text
        if len(sampled) > sample_count:
            sampled = random.sample(sampled, sample_count)
        sampled.sort()

        # ---- Compare each sampled page ---- #
        flagged_pages: list[int] = []
        category_stats = {
            "table_pages": {"total": 0, "failed": 0},
            "image_pages": {"total": 0, "failed": 0},
            "text_pages": {"total": 0, "failed": 0},
        }

        sampled_table_set = set(sampled_tables) & set(sampled)
        sampled_image_set = set(sampled_images) & set(sampled)
        sampled_text_set = set(sampled_text) & set(sampled)

        for idx, pn in enumerate(sampled):
            markdown = marker_results[pn]
            try:
                image = pdf_info.render_page(pn)
                result = vision_converter.compare_outputs(image, markdown)
                similarity = result.get("similarity", 0.0)
            except Exception:
                logger.warning("Vision comparison failed for page %d, treating as flagged", pn)
                similarity = 0.0

            if progress_callback:
                progress_callback(idx + 1, len(sampled))

            failed = similarity < SAMPLING_SIMILARITY_THRESHOLD

            if failed:
                flagged_pages.append(pn)

            # Update category stats
            if pn in sampled_table_set:
                category_stats["table_pages"]["total"] += 1
                if failed:
                    category_stats["table_pages"]["failed"] += 1
            elif pn in sampled_image_set:
                category_stats["image_pages"]["total"] += 1
                if failed:
                    category_stats["image_pages"]["failed"] += 1
            elif pn in sampled_text_set:
                category_stats["text_pages"]["total"] += 1
                if failed:
                    category_stats["text_pages"]["failed"] += 1

        # ---- Determine category-level redo ---- #
        def _should_redo(stats: dict) -> bool:
            if stats["total"] == 0:
                return False
            return (stats["failed"] / stats["total"]) > CATEGORY_FAIL_THRESHOLD

        category_redo = {
            "table": _should_redo(category_stats["table_pages"]),
            "image": _should_redo(category_stats["image_pages"]),
        }

        return {
            "sampled": sampled,
            "flagged_pages": flagged_pages,
            "category_stats": category_stats,
            "category_redo": category_redo,
        }
