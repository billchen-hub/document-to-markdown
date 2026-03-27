"""Comprehensive unit tests for doc_to_markdown.pdf_parser.PdfInfo."""
from __future__ import annotations

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from doc_to_markdown.pdf_parser import PdfInfo
from doc_to_markdown.config import MAX_CHAPTER_PAGES, MIN_CHAPTER_PAGES

# ---------------------------------------------------------------------------
# Fixtures & markers
# ---------------------------------------------------------------------------

PDF_PATH = Path(__file__).parent.parent / "UFS 4.1JESD220G.PDF"
needs_pdf = pytest.mark.skipif(not PDF_PATH.exists(), reason="Test PDF not available")


@pytest.fixture(scope="module")
def pdf_info():
    """Open the real PDF once for the entire test module."""
    if not PDF_PATH.exists():
        pytest.skip("Test PDF not available")
    info = PdfInfo(str(PDF_PATH))
    yield info
    info.close()


@pytest.fixture(scope="module")
def toc(pdf_info):
    """Pre-fetch TOC so individual tests don't repeat the call."""
    return pdf_info.get_toc()


@pytest.fixture(scope="module")
def chapters(pdf_info):
    """Pre-fetch chapters so individual tests don't repeat the call."""
    return pdf_info.get_chapters()


# ===================================================================
# 1. Basic properties
# ===================================================================


class TestBasicProperties:
    @needs_pdf
    def test_page_count(self, pdf_info):
        assert pdf_info.page_count == 542

    @needs_pdf
    def test_is_not_encrypted(self, pdf_info):
        assert pdf_info.is_encrypted() is False

    @needs_pdf
    def test_repr_contains_path_and_page_count(self, pdf_info):
        r = repr(pdf_info)
        assert "PdfInfo(" in r
        assert "UFS 4.1JESD220G.PDF" in r
        assert "542" in r


# ===================================================================
# 2. TOC extraction
# ===================================================================


class TestTocExtraction:
    @needs_pdf
    def test_toc_is_non_empty(self, toc):
        assert len(toc) > 0

    @needs_pdf
    def test_toc_entry_keys(self, toc):
        required_keys = {"title", "level", "page_num"}
        for entry in toc:
            assert required_keys.issubset(entry.keys()), (
                f"Entry missing keys: {required_keys - entry.keys()}"
            )

    @needs_pdf
    def test_toc_level_is_int_gte_1(self, toc):
        for entry in toc:
            assert isinstance(entry["level"], int)
            assert entry["level"] >= 1, f"Level {entry['level']} < 1 for '{entry['title']}'"

    @needs_pdf
    def test_toc_page_num_is_0indexed_within_range(self, pdf_info, toc):
        total = pdf_info.page_count
        for entry in toc:
            assert isinstance(entry["page_num"], int)
            assert 0 <= entry["page_num"] < total, (
                f"page_num {entry['page_num']} out of range [0, {total}) "
                f"for '{entry['title']}'"
            )

    @needs_pdf
    def test_toc_titles_are_non_empty_strings(self, toc):
        for entry in toc:
            assert isinstance(entry["title"], str)
            assert len(entry["title"]) > 0


# ===================================================================
# 3. Chapter computation
# ===================================================================


class TestChapterComputation:
    @needs_pdf
    def test_chapters_returns_list_of_dicts(self, chapters):
        assert isinstance(chapters, list)
        assert len(chapters) > 0
        for ch in chapters:
            assert isinstance(ch, dict)
            assert "title" in ch
            assert "start_page" in ch
            assert "end_page" in ch

    @needs_pdf
    def test_chapter_count_in_expected_range(self, chapters):
        assert 10 <= len(chapters) <= 100, (
            f"Chapter count {len(chapters)} not in [10, 100]"
        )

    @needs_pdf
    def test_no_chapter_exceeds_max_pages(self, chapters):
        for ch in chapters:
            span = ch["end_page"] - ch["start_page"] + 1
            assert span <= MAX_CHAPTER_PAGES, (
                f"Chapter '{ch['title']}' has {span} pages, exceeding MAX_CHAPTER_PAGES={MAX_CHAPTER_PAGES}"
            )

    @needs_pdf
    def test_start_lte_end_for_all_chapters(self, chapters):
        for ch in chapters:
            assert ch["start_page"] <= ch["end_page"], (
                f"Chapter '{ch['title']}': start_page {ch['start_page']} > end_page {ch['end_page']}"
            )

    @needs_pdf
    def test_chapters_cover_all_pages_no_gaps(self, pdf_info, chapters):
        total = pdf_info.page_count
        # First chapter starts at 0
        assert chapters[0]["start_page"] == 0, (
            f"First chapter starts at {chapters[0]['start_page']}, expected 0"
        )
        # Last chapter ends at total - 1
        assert chapters[-1]["end_page"] == total - 1, (
            f"Last chapter ends at {chapters[-1]['end_page']}, expected {total - 1}"
        )
        # Consecutive chapters are contiguous (no gaps, no overlaps)
        for i in range(1, len(chapters)):
            expected_start = chapters[i - 1]["end_page"] + 1
            assert chapters[i]["start_page"] == expected_start, (
                f"Gap or overlap between chapter {i-1} (end={chapters[i-1]['end_page']}) "
                f"and chapter {i} (start={chapters[i]['start_page']})"
            )

    @needs_pdf
    def test_first_chapter_starts_at_page_0(self, chapters):
        assert chapters[0]["start_page"] == 0


# ===================================================================
# 4. Page-level analysis
# ===================================================================


class TestPageAnalysis:
    @needs_pdf
    def test_get_page_image_regions_page0_returns_list(self, pdf_info):
        regions = pdf_info.get_page_image_regions(0)
        assert isinstance(regions, list)
        # Page 0 of the UFS spec is expected to have at least one image
        # (typically a logo or cover image).
        assert len(regions) > 0, "Expected page 0 to have at least one image region"

    @needs_pdf
    def test_image_region_has_bbox_and_area(self, pdf_info):
        regions = pdf_info.get_page_image_regions(0)
        for region in regions:
            assert "bbox" in region
            assert "area" in region
            # bbox is a tuple of 4 numbers
            assert len(region["bbox"]) == 4
            assert all(isinstance(v, (int, float)) for v in region["bbox"])
            # area is a positive number
            assert isinstance(region["area"], (int, float))
            assert region["area"] >= 0

    @needs_pdf
    def test_page_has_tables_returns_bool(self, pdf_info):
        result = pdf_info.page_has_tables(0)
        assert isinstance(result, bool)

    @needs_pdf
    def test_has_text_layer_page0(self, pdf_info):
        assert pdf_info.has_text_layer(0) is True

    @needs_pdf
    def test_render_page_returns_pil_image(self, pdf_info):
        from PIL import Image
        img = pdf_info.render_page(0)
        assert isinstance(img, Image.Image)
        assert img.width > 0
        assert img.height > 0

    @needs_pdf
    def test_render_page_mode_is_rgb(self, pdf_info):
        img = pdf_info.render_page(0)
        assert img.mode == "RGB"


# ===================================================================
# 5. Context manager
# ===================================================================


class TestContextManager:
    @needs_pdf
    def test_context_manager_usage(self):
        with PdfInfo(str(PDF_PATH)) as info:
            assert info.page_count == 542
        # After exiting, the underlying document should be closed.
        # PyMuPDF raises ValueError when accessing a closed document.
        with pytest.raises(ValueError):
            _ = info.page_count

    @needs_pdf
    def test_context_manager_returns_self(self):
        with PdfInfo(str(PDF_PATH)) as info:
            assert isinstance(info, PdfInfo)


# ===================================================================
# 6. Error handling
# ===================================================================


class TestErrorHandling:
    def test_file_not_found_raises(self):
        with pytest.raises(FileNotFoundError, match="PDF file not found"):
            PdfInfo("/nonexistent/path/fake.pdf")

    def test_file_not_found_with_descriptive_message(self):
        bad_path = "/some/missing/file.pdf"
        with pytest.raises(FileNotFoundError) as exc_info:
            PdfInfo(bad_path)
        assert bad_path in str(exc_info.value)

    @needs_pdf
    def test_accepts_path_object(self):
        # PdfInfo accepts str; internally it converts to Path. We
        # verify that passing a str representation of a Path works.
        info = PdfInfo(str(PDF_PATH))
        assert info.page_count == 542
        info.close()

    @needs_pdf
    def test_accepts_pathlib_path_via_str(self):
        # Ensure Path objects can be used (as str).
        p = Path(PDF_PATH)
        info = PdfInfo(str(p))
        assert info.page_count > 0
        info.close()


# ===================================================================
# 7. Static / class methods with synthetic data
# ===================================================================


class TestIsAppendix:
    """Test the _is_appendix static method."""

    def test_appendix_uppercase(self):
        assert PdfInfo._is_appendix("Appendix A") is True

    def test_appendix_lowercase(self):
        assert PdfInfo._is_appendix("appendix B") is True

    def test_appendix_with_leading_space(self):
        assert PdfInfo._is_appendix("  Appendix C - Foo") is True

    def test_chapter_is_not_appendix(self):
        assert PdfInfo._is_appendix("Chapter 1") is False

    def test_introduction_is_not_appendix(self):
        assert PdfInfo._is_appendix("Introduction") is False

    def test_empty_string_is_not_appendix(self):
        assert PdfInfo._is_appendix("") is False

    def test_partial_match_is_not_appendix(self):
        assert PdfInfo._is_appendix("Not an Appendix") is False


class TestMergeSmallChapters:
    """Test _merge_small_chapters with synthetic chapter data."""

    def test_empty_list_returns_empty(self):
        assert PdfInfo._merge_small_chapters([]) == []

    def test_single_chapter_not_merged(self):
        chapters = [{"title": "Ch1", "start_page": 0, "end_page": 0}]
        result = PdfInfo._merge_small_chapters(chapters)
        assert len(result) == 1
        assert result[0]["title"] == "Ch1"

    def test_small_chapter_merged_into_previous(self):
        chapters = [
            {"title": "Ch1", "start_page": 0, "end_page": 9},
            {"title": "Ch2", "start_page": 10, "end_page": 10},  # 1 page < MIN_CHAPTER_PAGES
            {"title": "Ch3", "start_page": 11, "end_page": 20},
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        assert len(result) == 2
        # Ch2 should have been merged into Ch1
        assert result[0]["title"] == "Ch1"
        assert result[0]["end_page"] == 10
        assert result[1]["title"] == "Ch3"

    def test_appendix_never_merged_even_if_small(self):
        chapters = [
            {"title": "Ch1", "start_page": 0, "end_page": 9},
            {"title": "Appendix A", "start_page": 10, "end_page": 10},  # 1 page
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        assert len(result) == 2
        assert result[1]["title"] == "Appendix A"
        assert result[1]["start_page"] == 10
        assert result[1]["end_page"] == 10

    def test_consecutive_small_chapters_cascade_merge(self):
        # Two consecutive small chapters should both merge into the first big one.
        chapters = [
            {"title": "Big", "start_page": 0, "end_page": 19},
            {"title": "Tiny1", "start_page": 20, "end_page": 20},  # 1 page
            {"title": "Tiny2", "start_page": 21, "end_page": 21},  # 1 page
            {"title": "Normal", "start_page": 22, "end_page": 30},
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        assert len(result) == 2
        assert result[0]["title"] == "Big"
        assert result[0]["end_page"] == 21  # absorbed both tiny chapters
        assert result[1]["title"] == "Normal"

    def test_large_chapters_not_merged(self):
        chapters = [
            {"title": "Ch1", "start_page": 0, "end_page": 9},
            {"title": "Ch2", "start_page": 10, "end_page": 19},
            {"title": "Ch3", "start_page": 20, "end_page": 29},
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        assert len(result) == 3

    def test_first_chapter_small_stays(self):
        # The first chapter is never merged into anything (no predecessor).
        chapters = [
            {"title": "Tiny", "start_page": 0, "end_page": 0},  # 1 page
            {"title": "Big", "start_page": 1, "end_page": 20},
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        # First chapter stays because there's no previous chapter to merge into.
        assert len(result) == 2
        assert result[0]["title"] == "Tiny"

    def test_appendix_between_small_chapters_blocks_merge(self):
        chapters = [
            {"title": "Ch1", "start_page": 0, "end_page": 9},
            {"title": "Tiny", "start_page": 10, "end_page": 10},  # merged into Ch1
            {"title": "Appendix A", "start_page": 11, "end_page": 11},  # stays
            {"title": "Small", "start_page": 12, "end_page": 12},  # merged into Appendix A
        ]
        result = PdfInfo._merge_small_chapters(chapters)
        # Tiny merges into Ch1.  Appendix A stays. Small merges into Appendix A.
        assert len(result) == 2
        assert result[0]["end_page"] == 10
        assert result[1]["title"] == "Appendix A"
        assert result[1]["end_page"] == 12


class TestSplitEvenly:
    """Test _split_evenly with synthetic chapter data."""

    def test_produces_at_least_two_parts(self):
        ch = {"title": "Big Chapter", "start_page": 0, "end_page": 99}
        parts = PdfInfo._split_evenly(ch, target_size=30)
        assert len(parts) >= 2

    def test_parts_cover_original_range(self):
        ch = {"title": "Ch", "start_page": 10, "end_page": 109}
        parts = PdfInfo._split_evenly(ch, target_size=30)
        assert parts[0]["start_page"] == 10
        assert parts[-1]["end_page"] == 109
        # Check contiguity
        for i in range(1, len(parts)):
            assert parts[i]["start_page"] == parts[i - 1]["end_page"] + 1

    def test_part_titles_include_part_numbers(self):
        ch = {"title": "MyChapter", "start_page": 0, "end_page": 59}
        parts = PdfInfo._split_evenly(ch, target_size=30)
        for i, part in enumerate(parts):
            assert f"Part {i + 1}" in part["title"]
            assert "MyChapter" in part["title"]

    def test_roughly_equal_sizes(self):
        ch = {"title": "Ch", "start_page": 0, "end_page": 119}
        parts = PdfInfo._split_evenly(ch, target_size=30)
        sizes = [p["end_page"] - p["start_page"] + 1 for p in parts]
        # All sizes should be within a reasonable factor of each other.
        assert max(sizes) <= 2 * min(sizes), (
            f"Parts are too uneven: {sizes}"
        )

    def test_small_chapter_split(self):
        ch = {"title": "Ch", "start_page": 0, "end_page": 3}
        parts = PdfInfo._split_evenly(ch, target_size=30)
        # Even a small chapter should produce at least 2 parts.
        assert len(parts) >= 2
        assert parts[0]["start_page"] == 0
        assert parts[-1]["end_page"] == 3


class TestChaptersFromToc:
    """Test _chapters_from_toc static method with synthetic TOC data."""

    def test_basic_toc_to_chapters(self):
        toc = [
            {"title": "Intro", "level": 1, "page_num": 0},
            {"title": "Body", "level": 1, "page_num": 10},
            {"title": "Conclusion", "level": 1, "page_num": 20},
        ]
        chapters = PdfInfo._chapters_from_toc(toc, total_pages=30)
        assert len(chapters) == 3
        assert chapters[0] == {"title": "Intro", "start_page": 0, "end_page": 9}
        assert chapters[1] == {"title": "Body", "start_page": 10, "end_page": 19}
        assert chapters[2] == {"title": "Conclusion", "start_page": 20, "end_page": 29}

    def test_toc_with_mixed_levels_uses_level1(self):
        toc = [
            {"title": "Ch1", "level": 1, "page_num": 0},
            {"title": "Sec1.1", "level": 2, "page_num": 5},
            {"title": "Ch2", "level": 1, "page_num": 10},
        ]
        chapters = PdfInfo._chapters_from_toc(toc, total_pages=20)
        assert len(chapters) == 2
        assert chapters[0]["title"] == "Ch1"
        assert chapters[1]["title"] == "Ch2"

    def test_toc_no_level1_promotes_all(self):
        toc = [
            {"title": "Sec A", "level": 2, "page_num": 0},
            {"title": "Sec B", "level": 2, "page_num": 5},
        ]
        chapters = PdfInfo._chapters_from_toc(toc, total_pages=10)
        assert len(chapters) == 2
        assert chapters[0]["title"] == "Sec A"

    def test_single_entry_toc(self):
        toc = [
            {"title": "Only", "level": 1, "page_num": 0},
        ]
        chapters = PdfInfo._chapters_from_toc(toc, total_pages=50)
        assert len(chapters) == 1
        assert chapters[0]["end_page"] == 49

    def test_clamps_end_page(self):
        # When two chapters start on the same page, end is clamped to start.
        toc = [
            {"title": "A", "level": 1, "page_num": 5},
            {"title": "B", "level": 1, "page_num": 5},
        ]
        chapters = PdfInfo._chapters_from_toc(toc, total_pages=10)
        assert chapters[0]["start_page"] == 5
        assert chapters[0]["end_page"] == 5  # clamped (max(4, 5) = 5)


class TestSplitByHeadings:
    """Test _split_by_headings static method with synthetic data."""

    def test_split_at_single_heading(self):
        ch = {"title": "Main", "start_page": 0, "end_page": 19}
        subs = [{"title": "Sub", "page_num": 10}]
        parts = PdfInfo._split_by_headings(ch, subs)
        assert len(parts) == 2
        assert parts[0] == {"title": "Main", "start_page": 0, "end_page": 9}
        assert parts[1] == {"title": "Sub", "start_page": 10, "end_page": 19}

    def test_split_at_multiple_headings(self):
        ch = {"title": "Main", "start_page": 0, "end_page": 29}
        subs = [
            {"title": "S1", "page_num": 10},
            {"title": "S2", "page_num": 20},
        ]
        parts = PdfInfo._split_by_headings(ch, subs)
        assert len(parts) == 3
        assert parts[0]["end_page"] == 9
        assert parts[1]["start_page"] == 10
        assert parts[1]["end_page"] == 19
        assert parts[2]["start_page"] == 20
        assert parts[2]["end_page"] == 29


class TestSplitLargeChapters:
    """Test _split_large_chapters with synthetic data."""

    def test_small_chapters_unchanged(self):
        chapters = [
            {"title": "Ch1", "start_page": 0, "end_page": 10},
        ]
        result = PdfInfo._split_large_chapters(chapters, toc_all=[])
        assert result == chapters

    def test_large_chapter_without_sub_headings_split_evenly(self):
        chapters = [
            {"title": "Huge", "start_page": 0, "end_page": 99},
        ]
        result = PdfInfo._split_large_chapters(chapters, toc_all=[])
        assert len(result) >= 2
        # All parts should be within MAX_CHAPTER_PAGES (or close due to even split).
        for part in result:
            span = part["end_page"] - part["start_page"] + 1
            # _split_evenly targets ~30 pages, so all should be reasonable.
            assert span <= MAX_CHAPTER_PAGES + 5  # small tolerance for rounding

    def test_large_chapter_split_by_level2_headings(self):
        chapters = [
            {"title": "Big", "start_page": 0, "end_page": 79},
        ]
        toc_all = [
            {"title": "Big", "level": 1, "page_num": 0},
            {"title": "Sec A", "level": 2, "page_num": 20},
            {"title": "Sec B", "level": 2, "page_num": 50},
        ]
        result = PdfInfo._split_large_chapters(chapters, toc_all)
        assert len(result) == 3
        assert result[0]["title"] == "Big"
        assert result[1]["title"] == "Sec A"
        assert result[2]["title"] == "Sec B"
