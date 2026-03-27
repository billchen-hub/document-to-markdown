"""Comprehensive unit tests for doc_to_markdown.quality_checker."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from doc_to_markdown.quality_checker import QualityChecker


@pytest.fixture
def checker() -> QualityChecker:
    return QualityChecker()


# ======================================================================
# 1. check_garbled
# ======================================================================

class TestCheckGarbled:
    """Tests for QualityChecker.check_garbled."""

    def test_normal_ascii_text(self, checker: QualityChecker):
        """Normal ASCII text should NOT be flagged as garbled."""
        text = "Hello, this is a perfectly normal sentence."
        assert checker.check_garbled(text) is False

    def test_cjk_characters_not_garbled(self, checker: QualityChecker):
        """CJK characters (Chinese/Japanese/Korean) should be accepted."""
        # Use only CJK Unified Ideographs + CJK Symbols/Punctuation (U+3000 range)
        # Avoid fullwidth forms (U+FF00+) which are outside _CJK_RANGES.
        text = "這是一段中文文字包含繁體字"  # pure CJK ideographs
        assert checker.check_garbled(text) is False

    def test_japanese_text_not_garbled(self, checker: QualityChecker):
        """Japanese hiragana/katakana should be accepted."""
        text = "これはテストです。日本語のテキスト。"
        assert checker.check_garbled(text) is False

    def test_many_control_characters_garbled(self, checker: QualityChecker):
        """Text with many control characters (0x00-0x1f) should be garbled."""
        # Build a string that is >5% control characters
        control_chars = "\x00\x01\x02\x03\x04\x05\x06\x07\x08"
        normal = "A" * 10  # 10 normal chars + 9 control = ~47% bad
        text = normal + control_chars
        assert checker.check_garbled(text) is True

    def test_replacement_characters_garbled(self, checker: QualityChecker):
        """U+FFFD replacement characters should count as garbled."""
        # 10 replacement characters out of 20 total => 50% bad
        text = "abcdefghij" + "\ufffd" * 10
        assert checker.check_garbled(text) is True

    def test_empty_string(self, checker: QualityChecker):
        """Empty string should NOT be flagged as garbled."""
        assert checker.check_garbled("") is False

    def test_mixed_text_just_below_threshold(self, checker: QualityChecker):
        """Text with bad chars at exactly 5% ratio should NOT be garbled (threshold is >5%)."""
        # GARBLED_CHAR_THRESHOLD = 0.05 and the check is ratio > threshold (strict >)
        # 95 normal chars + 5 bad chars = 5/100 = 0.05, which is NOT > 0.05
        normal = "A" * 95
        bad = "\x00" * 5
        text = normal + bad
        assert checker.check_garbled(text) is False

    def test_mixed_text_just_above_threshold(self, checker: QualityChecker):
        """Text with bad chars just above 5% should be flagged as garbled."""
        # 94 normal chars + 6 bad chars = 6/100 = 0.06 > 0.05
        normal = "A" * 94
        bad = "\x00" * 6
        text = normal + bad
        assert checker.check_garbled(text) is True

    def test_whitespace_characters_not_garbled(self, checker: QualityChecker):
        """Tab, LF, CR are allowed whitespace and should not be counted as garbled."""
        text = "Hello\tWorld\nNew line\rCarriage return"
        assert checker.check_garbled(text) is False


# ======================================================================
# 2. check_empty_table
# ======================================================================

class TestCheckEmptyTable:
    """Tests for QualityChecker.check_empty_table."""

    def test_table_with_data_rows(self, checker: QualityChecker):
        """Table with header + separator + data rows should NOT be flagged."""
        text = (
            "| Name | Age |\n"
            "| --- | --- |\n"
            "| Alice | 30 |\n"
            "| Bob | 25 |"
        )
        assert checker.check_empty_table(text) is False

    def test_table_header_only_no_data(self, checker: QualityChecker):
        """Table with header + separator but NO data rows should be flagged."""
        text = (
            "| Name | Age |\n"
            "| --- | --- |"
        )
        assert checker.check_empty_table(text) is True

    def test_multi_column_table_with_data(self, checker: QualityChecker):
        """Multi-column table with data should NOT be flagged."""
        text = (
            "| Col1 | Col2 | Col3 | Col4 |\n"
            "| --- | --- | --- | --- |\n"
            "| a | b | c | d |\n"
            "| e | f | g | h |"
        )
        assert checker.check_empty_table(text) is False

    def test_multiple_tables_one_empty(self, checker: QualityChecker):
        """If one of multiple tables is empty, should be flagged."""
        text = (
            "| Name | Age |\n"
            "| --- | --- |\n"
            "| Alice | 30 |\n"
            "\n"
            "| Status | Code |\n"
            "| --- | --- |"
        )
        assert checker.check_empty_table(text) is True

    def test_no_table_at_all(self, checker: QualityChecker):
        """Text with no table should NOT be flagged."""
        text = "This is just plain text with no tables at all."
        assert checker.check_empty_table(text) is False

    def test_separator_line_only_no_header(self, checker: QualityChecker):
        """A separator line with nothing before it is still detected as an empty table."""
        text = "| --- | --- |"
        assert checker.check_empty_table(text) is True

    def test_table_followed_by_blank_line_then_text(self, checker: QualityChecker):
        """Empty table followed by a blank line then non-table text is flagged."""
        text = (
            "| Header |\n"
            "| --- |\n"
            "\n"
            "Some paragraph text."
        )
        assert checker.check_empty_table(text) is True

    def test_table_with_alignment_markers(self, checker: QualityChecker):
        """Separator with alignment colons should be recognized."""
        text = (
            "| Left | Center | Right |\n"
            "| :--- | :---: | ---: |\n"
            "| a | b | c |"
        )
        assert checker.check_empty_table(text) is False


# ======================================================================
# 3. check_image_missing
# ======================================================================

class TestCheckImageMissing:
    """Tests for QualityChecker.check_image_missing."""

    def test_no_images_in_pdf(self, checker: QualityChecker):
        """If has_images=False, always return False regardless of text."""
        assert checker.check_image_missing("No images at all.", has_images=False) is False
        assert checker.check_image_missing("", has_images=False) is False
        assert checker.check_image_missing("![img](test.png)", has_images=False) is False

    def test_has_images_with_markdown_image(self, checker: QualityChecker):
        """Markdown ![alt](url) syntax should satisfy image presence."""
        text = "Some text and ![diagram](fig1.png) more text."
        assert checker.check_image_missing(text, has_images=True) is False

    def test_has_images_with_html_img_tag(self, checker: QualityChecker):
        """HTML <img src=...> tag should satisfy image presence."""
        text = 'Some text and <img src="figure.png" /> more text.'
        assert checker.check_image_missing(text, has_images=True) is False

    def test_has_images_with_img_tag_case_insensitive(self, checker: QualityChecker):
        """HTML <IMG SRC=...> should be matched case-insensitively."""
        text = 'Some text and <IMG SRC="figure.png"> more text.'
        assert checker.check_image_missing(text, has_images=True) is False

    def test_has_images_with_image_description_bracket(self, checker: QualityChecker):
        """[Image description] bracket notation should satisfy image presence."""
        text = "Some text and [Image: A photo of a cat] more text."
        assert checker.check_image_missing(text, has_images=True) is False

    def test_has_images_with_lowercase_image_bracket(self, checker: QualityChecker):
        """[image ...] with lowercase 'i' should also be accepted."""
        text = "Some text and [image of a diagram] more text."
        assert checker.check_image_missing(text, has_images=True) is False

    def test_has_images_no_image_reference(self, checker: QualityChecker):
        """If page has images but markdown has no image reference, flag it."""
        text = "This is just plain text with no image references whatsoever."
        assert checker.check_image_missing(text, has_images=True) is True

    def test_has_images_empty_text(self, checker: QualityChecker):
        """Empty text with has_images=True should be flagged."""
        assert checker.check_image_missing("", has_images=True) is True

    def test_has_images_markdown_image_no_alt(self, checker: QualityChecker):
        """![](img.png) with empty alt text should still be recognized."""
        text = "![](img.png)"
        assert checker.check_image_missing(text, has_images=True) is False


# ======================================================================
# 4. check_too_short
# ======================================================================

class TestCheckTooShort:
    """Tests for QualityChecker.check_too_short."""

    def test_text_shorter_than_threshold(self, checker: QualityChecker):
        """Text < 50 chars should be flagged as too short."""
        text = "Short."  # 6 chars
        assert checker.check_too_short(text) is True

    def test_text_exactly_at_threshold(self, checker: QualityChecker):
        """Text with exactly 50 stripped chars should NOT be flagged (< 50 is short)."""
        text = "A" * 50  # exactly 50 chars
        assert checker.check_too_short(text) is False

    def test_text_one_below_threshold(self, checker: QualityChecker):
        """Text with 49 stripped chars should be flagged."""
        text = "A" * 49
        assert checker.check_too_short(text) is True

    def test_lots_of_whitespace_short_content(self, checker: QualityChecker):
        """Text with lots of whitespace but short actual content should be flagged."""
        text = "   \n\t  Hello   \n   \t  "  # stripped = "Hello" = 5 chars
        assert checker.check_too_short(text) is True

    def test_empty_string(self, checker: QualityChecker):
        """Empty string should be flagged as too short."""
        assert checker.check_too_short("") is True

    def test_long_text(self, checker: QualityChecker):
        """Text well above the threshold should NOT be flagged."""
        text = "This is a long enough text that exceeds the minimum content length easily."
        assert len(text.strip()) >= 50
        assert checker.check_too_short(text) is False


# ======================================================================
# 5. check_format_broken
# ======================================================================

class TestCheckFormatBroken:
    """Tests for QualityChecker.check_format_broken."""

    def test_unclosed_table_row(self, checker: QualityChecker):
        """A table row starting with | but not ending with | should be flagged."""
        text = "| data without closing pipe"
        assert checker.check_format_broken(text) is True

    def test_normal_table_row(self, checker: QualityChecker):
        """A properly closed table row should NOT be flagged."""
        text = "| data | value |"
        assert checker.check_format_broken(text) is False

    def test_orphaned_heading_marker(self, checker: QualityChecker):
        """A heading marker with no text after it should be flagged."""
        text = "# "
        assert checker.check_format_broken(text) is True

    def test_orphaned_heading_marker_h2(self, checker: QualityChecker):
        """## with no text should be flagged."""
        text = "## "
        assert checker.check_format_broken(text) is True

    def test_orphaned_heading_no_space(self, checker: QualityChecker):
        """# with nothing after it (no space) should be flagged."""
        text = "#"
        assert checker.check_format_broken(text) is True

    def test_normal_heading(self, checker: QualityChecker):
        """A normal heading with text should NOT be flagged."""
        text = "# Title"
        assert checker.check_format_broken(text) is False

    def test_badly_nested_list_jump_over_4(self, checker: QualityChecker):
        """A list with indentation jump > 4 spaces should be flagged."""
        text = (
            "- item 1\n"
            "          - deeply nested item"  # 10 spaces indent, jump of 10 > 4
        )
        assert checker.check_format_broken(text) is True

    def test_normal_nested_list(self, checker: QualityChecker):
        """A normally nested list (up to 4 space jump) should NOT be flagged."""
        text = (
            "- item 1\n"
            "    - item 2\n"
            "        - item 3"
        )
        assert checker.check_format_broken(text) is False

    def test_list_indent_exactly_4(self, checker: QualityChecker):
        """Indent jump of exactly 4 should NOT be flagged (> 4 is the threshold)."""
        text = (
            "- item 1\n"
            "    - item 2"
        )
        assert checker.check_format_broken(text) is False

    def test_list_indent_5_spaces(self, checker: QualityChecker):
        """Indent jump of 5 spaces should be flagged (> 4)."""
        text = (
            "- item 1\n"
            "     - item 2"
        )
        assert checker.check_format_broken(text) is True

    def test_clean_text_no_issues(self, checker: QualityChecker):
        """Clean text without tables, headings, or lists should pass."""
        text = "Just a plain paragraph with no special formatting."
        assert checker.check_format_broken(text) is False

    def test_multiple_issues_returns_true(self, checker: QualityChecker):
        """Text with multiple format issues should still just return True."""
        text = (
            "# \n"
            "| unclosed row\n"
        )
        assert checker.check_format_broken(text) is True

    def test_table_separator_unclosed_not_flagged(self, checker: QualityChecker):
        """A malformed separator line (without closing |) should be excluded from the unclosed row check."""
        # The regex for malformed separators: ^\|[\s\-:|]+$
        text = "| --- | ---"
        assert checker.check_format_broken(text) is False

    def test_empty_text(self, checker: QualityChecker):
        """Empty text should NOT be flagged."""
        assert checker.check_format_broken("") is False

    def test_list_reset_on_blank_line(self, checker: QualityChecker):
        """Blank line between lists resets indent tracking, so a second list at any indent is fine."""
        text = (
            "- item 1\n"
            "\n"
            "          - new list starts here"
        )
        assert checker.check_format_broken(text) is False


# ======================================================================
# 6. check_page (aggregate)
# ======================================================================

class TestCheckPage:
    """Tests for QualityChecker.check_page aggregate method."""

    def test_clean_page_passes(self, checker: QualityChecker):
        """A clean page should pass all checks."""
        markdown = "A" * 100  # long enough, no issues
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=False)
        assert result["pass"] is True
        assert result["issues"] == []

    def test_garbled_text_fails(self, checker: QualityChecker):
        """A page with garbled text should fail with garbled_text reason."""
        markdown = "A" * 94 + "\x00" * 6  # >5% garbled
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=False)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "garbled_text" in reasons
        actions = {i["reason"]: i["action"] for i in result["issues"]}
        assert actions["garbled_text"] == "redo"

    def test_empty_table_fails(self, checker: QualityChecker):
        """A page with has_tables=True and an empty table should fail."""
        markdown = (
            "Some text padding to meet length requirements and avoid too_short check.\n"
            "| Header |\n"
            "| --- |"
        )
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=True)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "empty_table" in reasons
        actions = {i["reason"]: i["action"] for i in result["issues"]}
        assert actions["empty_table"] == "redo"

    def test_empty_table_not_checked_when_no_tables(self, checker: QualityChecker):
        """When has_tables=False, empty_table check should be skipped."""
        markdown = (
            "Some text that is definitely long enough to pass the length check.\n"
            "| Header |\n"
            "| --- |"
        )
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=False)
        reasons = [i["reason"] for i in result["issues"]]
        assert "empty_table" not in reasons

    def test_image_missing_fails(self, checker: QualityChecker):
        """A page with has_images=True but no image references should fail with vision_describe."""
        markdown = "A" * 100  # long enough, no image references
        result = checker.check_page(page_num=1, markdown=markdown, has_images=True, has_tables=False)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "image_missing" in reasons
        actions = {i["reason"]: i["action"] for i in result["issues"]}
        assert actions["image_missing"] == "vision_describe"

    def test_too_short_fails(self, checker: QualityChecker):
        """A page with very short content should fail with too_short."""
        markdown = "Short."
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=False)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "too_short" in reasons
        actions = {i["reason"]: i["action"] for i in result["issues"]}
        assert actions["too_short"] == "redo"

    def test_format_broken_fails(self, checker: QualityChecker):
        """A page with broken formatting should fail with format_broken."""
        markdown = (
            "This is enough text to pass the length check for the content.\n"
            "| unclosed row without pipe ending\n"
        )
        result = checker.check_page(page_num=1, markdown=markdown, has_images=False, has_tables=False)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "format_broken" in reasons
        actions = {i["reason"]: i["action"] for i in result["issues"]}
        assert actions["format_broken"] == "redo"

    def test_multiple_issues(self, checker: QualityChecker):
        """A page can have multiple issues reported simultaneously."""
        markdown = "Hi"  # too short + image missing
        result = checker.check_page(page_num=1, markdown=markdown, has_images=True, has_tables=False)
        assert result["pass"] is False
        reasons = [i["reason"] for i in result["issues"]]
        assert "too_short" in reasons
        assert "image_missing" in reasons


# ======================================================================
# 7. check_all_pages
# ======================================================================

class TestCheckAllPages:
    """Tests for QualityChecker.check_all_pages."""

    @staticmethod
    def _make_pdf_info(image_regions: dict[int, list], tables: dict[int, bool]) -> MagicMock:
        """Create a mock pdf_info object."""
        pdf_info = MagicMock()
        pdf_info.get_page_image_regions = MagicMock(
            side_effect=lambda pn: image_regions.get(pn, [])
        )
        pdf_info.page_has_tables = MagicMock(
            side_effect=lambda pn: tables.get(pn, False)
        )
        return pdf_info

    def test_all_pages_pass(self, checker: QualityChecker):
        """All clean pages should result in full pass count."""
        marker_results = {
            1: "A" * 100,
            2: "B" * 100,
            3: "C" * 100,
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: [], 2: [], 3: []},
            tables={1: False, 2: False, 3: False},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["total_pages"] == 3
        assert result["passed"] == 3
        assert result["needs_redo"] == []
        assert result["needs_vision_describe"] == []

    def test_pages_categorized_into_redo(self, checker: QualityChecker):
        """Pages with garbled text should appear in needs_redo."""
        garbled_text = "A" * 90 + "\x00" * 10  # 10% garbled
        marker_results = {
            1: "A" * 100,       # clean
            2: garbled_text,    # garbled
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: [], 2: []},
            tables={1: False, 2: False},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["total_pages"] == 2
        assert result["passed"] == 1
        assert len(result["needs_redo"]) >= 1
        redo_pages = [entry["page"] for entry in result["needs_redo"]]
        assert 2 in redo_pages
        redo_reasons = [entry["reason"] for entry in result["needs_redo"] if entry["page"] == 2]
        assert "garbled_text" in redo_reasons

    def test_pages_categorized_into_vision_describe(self, checker: QualityChecker):
        """Pages with missing images should appear in needs_vision_describe."""
        marker_results = {
            1: "A" * 100,  # clean but has images -> missing image ref
            2: "B" * 100,  # no images, clean
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: ["img_region_1"], 2: []},
            tables={1: False, 2: False},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["total_pages"] == 2
        assert result["passed"] == 1
        assert len(result["needs_vision_describe"]) >= 1
        vision_pages = [entry["page"] for entry in result["needs_vision_describe"]]
        assert 1 in vision_pages
        vision_reasons = [entry["reason"] for entry in result["needs_vision_describe"] if entry["page"] == 1]
        assert "image_missing" in vision_reasons

    def test_mixed_redo_and_vision(self, checker: QualityChecker):
        """Pages can be split across redo and vision_describe categories."""
        marker_results = {
            1: "A" * 100,                        # clean
            2: "A" * 90 + "\x00" * 10,           # garbled -> redo
            3: "C" * 100,                         # has images, no ref -> vision_describe
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: [], 2: [], 3: ["some_region"]},
            tables={1: False, 2: False, 3: False},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["total_pages"] == 3
        assert result["passed"] == 1
        redo_pages = [entry["page"] for entry in result["needs_redo"]]
        vision_pages = [entry["page"] for entry in result["needs_vision_describe"]]
        assert 2 in redo_pages
        assert 3 in vision_pages

    def test_empty_table_with_has_tables(self, checker: QualityChecker):
        """Empty table on a page with has_tables=True should trigger redo."""
        marker_results = {
            1: (
                "Enough text to pass length check for the content padding here.\n"
                "| Header |\n"
                "| --- |"
            ),
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: []},
            tables={1: True},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["passed"] == 0
        redo_reasons = [entry["reason"] for entry in result["needs_redo"]]
        assert "empty_table" in redo_reasons

    def test_empty_marker_results(self, checker: QualityChecker):
        """Empty marker_results should return zero counts."""
        pdf_info = self._make_pdf_info(image_regions={}, tables={})
        result = checker.check_all_pages({}, pdf_info)
        assert result["total_pages"] == 0
        assert result["passed"] == 0
        assert result["needs_redo"] == []
        assert result["needs_vision_describe"] == []

    def test_pdf_info_methods_called_for_each_page(self, checker: QualityChecker):
        """Verify pdf_info methods are called once per page."""
        marker_results = {1: "A" * 100, 2: "B" * 100}
        pdf_info = self._make_pdf_info(
            image_regions={1: [], 2: []},
            tables={1: False, 2: False},
        )

        checker.check_all_pages(marker_results, pdf_info)
        assert pdf_info.get_page_image_regions.call_count == 2
        assert pdf_info.page_has_tables.call_count == 2

    def test_page_with_multiple_issues_produces_multiple_entries(self, checker: QualityChecker):
        """A page that fails multiple checks produces one entry per issue."""
        # This text is too short AND has broken formatting (orphaned heading)
        marker_results = {
            1: "# \n",
        }
        pdf_info = self._make_pdf_info(
            image_regions={1: []},
            tables={1: False},
        )

        result = checker.check_all_pages(marker_results, pdf_info)
        assert result["passed"] == 0
        # Should have at least too_short and format_broken in redo
        redo_reasons = [entry["reason"] for entry in result["needs_redo"]]
        assert "too_short" in redo_reasons
        assert "format_broken" in redo_reasons
