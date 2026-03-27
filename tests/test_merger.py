"""Comprehensive unit tests for ChapterMerger."""
from __future__ import annotations

import pytest

from doc_to_markdown.merger import ChapterMerger


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def merger():
    return ChapterMerger()


def _chapter(title: str, start: int, end: int) -> dict:
    """Helper to build a chapter dict (0-indexed pages)."""
    return {"title": title, "start_page": start, "end_page": end}


# ===================================================================
# 1. merge basic
# ===================================================================

class TestMergeBasic:
    """Core merge behaviour: file creation and content assembly."""

    def test_single_chapter_creates_one_file(self, merger, tmp_path):
        chapters = [_chapter("Intro", 0, 2)]
        pages = {0: "Page zero.", 1: "Page one.", 2: "Page two."}

        results = merger.merge(chapters, pages, tmp_path)

        assert len(results) == 1
        files = list((tmp_path / "chapters").iterdir())
        assert len(files) == 1

    def test_multiple_chapters_correct_file_count(self, merger, tmp_path):
        chapters = [
            _chapter("Ch1", 0, 1),
            _chapter("Ch2", 2, 3),
            _chapter("Ch3", 4, 5),
        ]
        pages = {i: f"Content of page {i}." for i in range(6)}

        results = merger.merge(chapters, pages, tmp_path)

        assert len(results) == 3
        files = list((tmp_path / "chapters").iterdir())
        assert len(files) == 3

    def test_file_content_is_concatenation_of_pages(self, merger, tmp_path):
        chapters = [_chapter("Chapter", 0, 2)]
        pages = {0: "AAA", 1: "BBB", 2: "CCC"}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_chapter.md").read_text(encoding="utf-8")
        # Content should contain all three page blocks joined by double newlines,
        # with a chapter heading prepended since none of the pages start with "# ".
        assert "AAA" in content
        assert "BBB" in content
        assert "CCC" in content
        # Verify ordering: AAA before BBB before CCC
        assert content.index("AAA") < content.index("BBB") < content.index("CCC")

    def test_missing_pages_gracefully_skipped(self, merger, tmp_path):
        """Pages absent from page_markdowns should not cause errors."""
        chapters = [_chapter("Sparse", 0, 4)]
        pages = {0: "First page.", 3: "Fourth page."}  # pages 1, 2, 4 missing

        results = merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_sparse.md").read_text(encoding="utf-8")
        assert "First page." in content
        assert "Fourth page." in content
        assert len(results) == 1


# ===================================================================
# 2. merge file output
# ===================================================================

class TestMergeFileOutput:
    """Filesystem artefacts: directory, filenames, encoding, return value."""

    def test_chapters_subdirectory_created(self, merger, tmp_path):
        chapters = [_chapter("X", 0, 0)]
        pages = {0: "Hello."}

        merger.merge(chapters, pages, tmp_path)

        assert (tmp_path / "chapters").is_dir()

    def test_files_named_correctly(self, merger, tmp_path):
        chapters = [
            _chapter("Introduction", 0, 0),
            _chapter("Background", 1, 1),
        ]
        pages = {0: "Intro text.", 1: "Background text."}

        merger.merge(chapters, pages, tmp_path)

        assert (tmp_path / "chapters" / "01_introduction.md").exists()
        assert (tmp_path / "chapters" / "02_background.md").exists()

    def test_file_content_is_utf8(self, merger, tmp_path):
        chapters = [_chapter("Unicode", 0, 0)]
        pages = {0: "Ueberblick: Stra\u00dfe \u2014 \u00e9l\u00e8ve \u2014 \u4e16\u754c"}

        merger.merge(chapters, pages, tmp_path)

        raw = (tmp_path / "chapters" / "01_unicode.md").read_bytes()
        decoded = raw.decode("utf-8")
        assert "Stra\u00dfe" in decoded
        assert "\u4e16\u754c" in decoded

    def test_returns_list_of_dicts_with_expected_keys(self, merger, tmp_path):
        chapters = [_chapter("Overview", 0, 2)]
        pages = {0: "A", 1: "B", 2: "C"}

        results = merger.merge(chapters, pages, tmp_path)

        assert len(results) == 1
        r = results[0]
        assert set(r.keys()) == {"filename", "title", "page_range", "size_kb"}
        assert r["filename"] == "01_overview.md"
        assert r["title"] == "Overview"
        assert isinstance(r["size_kb"], float)

    def test_page_range_is_1_indexed(self, merger, tmp_path):
        """page_range should be human-readable 1-indexed."""
        chapters = [_chapter("Chap", 0, 4)]
        pages = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}

        results = merger.merge(chapters, pages, tmp_path)

        assert results[0]["page_range"] == "1-5"

    def test_size_kb_is_reasonable(self, merger, tmp_path):
        content = "x" * 2048  # exactly 2 KB of ASCII
        chapters = [_chapter("# Sized", 0, 0)]
        pages = {0: content}

        results = merger.merge(chapters, pages, tmp_path)

        # size should be close to 2.0 KB (the content itself)
        assert results[0]["size_kb"] >= 2.0


# ===================================================================
# 3. merge edge cases
# ===================================================================

class TestMergeEdgeCases:
    """Boundary conditions and unusual inputs."""

    def test_empty_page_markdown_still_creates_file(self, merger, tmp_path):
        chapters = [_chapter("Empty", 0, 0)]
        pages = {0: ""}

        results = merger.merge(chapters, pages, tmp_path)

        filepath = tmp_path / "chapters" / "01_empty.md"
        assert filepath.exists()
        assert len(results) == 1

    def test_all_whitespace_pages_creates_file(self, merger, tmp_path):
        """Pages that are only whitespace are treated as empty (strip())."""
        chapters = [_chapter("Blank", 0, 1)]
        pages = {0: "   \n\n  ", 1: "\t\t"}

        results = merger.merge(chapters, pages, tmp_path)

        filepath = tmp_path / "chapters" / "01_blank.md"
        assert filepath.exists()
        # Content should be empty string because nothing has substance
        content = filepath.read_text(encoding="utf-8")
        assert content == ""

    def test_special_characters_sanitized_in_filename(self, merger, tmp_path):
        chapters = [_chapter("Section 3.1: Foo/Bar", 0, 0)]
        pages = {0: "Content."}

        results = merger.merge(chapters, pages, tmp_path)

        filename = results[0]["filename"]
        # Colons, dots, slashes should be stripped
        assert ":" not in filename
        assert "/" not in filename
        # Still parseable
        assert filename.startswith("01_")
        assert filename.endswith(".md")

    def test_very_long_title_truncated(self, merger, tmp_path):
        long_title = "A" * 200
        chapters = [_chapter(long_title, 0, 0)]
        pages = {0: "Content here."}

        results = merger.merge(chapters, pages, tmp_path)

        filename = results[0]["filename"]
        # Format: "01_" (3) + body + ".md" (3) => body should be <= 60 chars
        body = filename[3:-3]  # strip "01_" prefix and ".md" suffix
        assert len(body) <= 60

    def test_page_range_single_page(self, merger, tmp_path):
        chapters = [_chapter("Single", 0, 0)]
        pages = {0: "Only page."}

        results = merger.merge(chapters, pages, tmp_path)

        assert results[0]["page_range"] == "1-1"

    def test_no_chapters_produces_empty_results(self, merger, tmp_path):
        results = merger.merge([], {}, tmp_path)

        assert results == []
        # chapters/ directory still gets created
        assert (tmp_path / "chapters").is_dir()


# ===================================================================
# 4. merge warnings (capsys)
# ===================================================================

class TestMergeWarnings:
    """Warning messages for excessive chapters or oversized files."""

    def test_warns_when_chapter_count_exceeds_limit(self, merger, tmp_path, capsys):
        num = 101  # exceeds MAX_CHAPTER_COUNT (100)
        chapters = [_chapter(f"Ch{i}", i, i) for i in range(num)]
        pages = {i: f"Page {i}" for i in range(num)}

        merger.merge(chapters, pages, tmp_path)

        captured = capsys.readouterr()
        assert "WARNING" in captured.out
        assert "101" in captured.out

    def test_no_warning_at_exactly_100_chapters(self, merger, tmp_path, capsys):
        num = 100  # exactly at limit -> no warning
        chapters = [_chapter(f"Ch{i}", i, i) for i in range(num)]
        pages = {i: f"Page {i}" for i in range(num)}

        merger.merge(chapters, pages, tmp_path)

        captured = capsys.readouterr()
        assert "chapters detected" not in captured.out

    def test_warns_when_single_file_exceeds_size_limit(self, merger, tmp_path, capsys):
        # MAX_FILE_SIZE_KB = 200, create content > 200KB
        big_content = "x" * (201 * 1024)
        chapters = [_chapter("# Huge", 0, 0)]
        pages = {0: big_content}

        merger.merge(chapters, pages, tmp_path)

        captured = capsys.readouterr()
        assert "WARNING" in captured.out
        assert "KB" in captured.out

    def test_no_size_warning_under_limit(self, merger, tmp_path, capsys):
        small_content = "x" * 1024  # 1 KB
        chapters = [_chapter("Small", 0, 0)]
        pages = {0: small_content}

        merger.merge(chapters, pages, tmp_path)

        captured = capsys.readouterr()
        # Should not mention file size warning
        assert "exceeds" not in captured.out or "limit" not in captured.out


# ===================================================================
# 5. _format_filename
# ===================================================================

class TestFormatFilename:
    """Unit tests for the private _format_filename helper."""

    def test_normal_title(self, merger):
        assert merger._format_filename(1, "Introduction") == "01_introduction.md"

    def test_title_with_spaces(self, merger):
        result = merger._format_filename(1, "Architecture Overview")
        assert result == "01_architecture_overview.md"

    def test_title_with_special_chars(self, merger):
        result = merger._format_filename(1, "Section 3.1: Foo")
        # Colon and dot should be removed
        assert ":" not in result
        assert result.startswith("01_")
        assert result.endswith(".md")
        # "section" and "foo" should survive
        assert "section" in result
        assert "foo" in result

    def test_empty_title(self, merger):
        assert merger._format_filename(1, "") == "01_untitled.md"

    def test_whitespace_only_title(self, merger):
        assert merger._format_filename(1, "   ") == "01_untitled.md"

    def test_all_special_chars_title(self, merger):
        assert merger._format_filename(1, ":::///!!!") == "01_untitled.md"

    def test_very_long_title_truncated_to_60(self, merger):
        long = "a" * 100
        result = merger._format_filename(1, long)
        body = result[3:-3]  # strip "01_" and ".md"
        assert len(body) <= 60

    def test_truncation_does_not_end_with_underscore(self, merger):
        # A title whose 60th char boundary falls right after a space (-> underscore)
        title = ("abcde " * 20).strip()  # "abcde abcde ..."
        result = merger._format_filename(1, title)
        body = result[3:-3]
        assert not body.endswith("_")

    def test_index_zero_padded(self, merger):
        assert merger._format_filename(5, "Test") == "05_test.md"
        assert merger._format_filename(12, "Test") == "12_test.md"

    def test_large_index(self, merger):
        result = merger._format_filename(999, "Big")
        assert result == "999_big.md"

    def test_unicode_normalized(self, merger):
        # NFKD normalization: "fi" ligature -> "fi"
        result = merger._format_filename(1, "\ufb01nal")
        assert "fi" in result or "final" in result

    def test_hyphens_preserved(self, merger):
        result = merger._format_filename(1, "self-contained")
        assert "self-contained" in result

    def test_mixed_case_lowered(self, merger):
        result = merger._format_filename(1, "CamelCase Title")
        assert result == "01_camelcase_title.md"


# ===================================================================
# 6. Chapter heading
# ===================================================================

class TestChapterHeading:
    """Chapter title is prepended as H1 only when needed."""

    def test_heading_prepended_when_absent(self, merger, tmp_path):
        chapters = [_chapter("My Chapter", 0, 0)]
        pages = {0: "Some paragraph content."}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_my_chapter.md").read_text(encoding="utf-8")
        assert content.startswith("# My Chapter\n\n")
        assert "Some paragraph content." in content

    def test_no_duplicate_heading_when_present(self, merger, tmp_path):
        chapters = [_chapter("Existing", 0, 0)]
        pages = {0: "# Existing\n\nBody text here."}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_existing.md").read_text(encoding="utf-8")
        # Should NOT have a duplicate "# Existing"
        assert content.count("# Existing") == 1
        assert content.startswith("# Existing\n")

    def test_heading_not_prepended_with_leading_whitespace_before_hash(self, merger, tmp_path):
        """Content that has leading whitespace before '# ' should still get heading prepended,
        because lstrip() removes whitespace before the check."""
        chapters = [_chapter("Title", 0, 0)]
        pages = {0: "  # Already Titled\n\nBody."}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_title.md").read_text(encoding="utf-8")
        # lstrip() removes leading spaces, so "# Already Titled" is detected
        # -> no duplicate heading prepended
        assert content.count("#") == 1 or not content.startswith("# Title\n")

    def test_h2_heading_gets_h1_prepended(self, merger, tmp_path):
        """Content starting with ## should still get H1 prepended."""
        chapters = [_chapter("Main", 0, 0)]
        pages = {0: "## Sub-section\n\nDetails."}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_main.md").read_text(encoding="utf-8")
        assert content.startswith("# Main\n\n")
        assert "## Sub-section" in content

    def test_empty_content_no_heading(self, merger, tmp_path):
        """If all pages are empty/whitespace, no heading should be added."""
        chapters = [_chapter("Ghost", 0, 0)]
        pages = {0: ""}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_ghost.md").read_text(encoding="utf-8")
        # Empty content means no heading is prepended
        assert content == ""

    def test_heading_prepended_across_multipage_chapter(self, merger, tmp_path):
        """First page lacks heading; chapter title prepended once to merged content."""
        chapters = [_chapter("Multi", 0, 2)]
        pages = {0: "Part A.", 1: "Part B.", 2: "Part C."}

        merger.merge(chapters, pages, tmp_path)

        content = (tmp_path / "chapters" / "01_multi.md").read_text(encoding="utf-8")
        assert content.startswith("# Multi\n\n")
        # Should appear exactly once
        assert content.count("# Multi") == 1
