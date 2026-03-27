"""Tests for doc_to_markdown.config module."""

import pytest
from pathlib import Path

from doc_to_markdown import config


class TestPaths:
    """Tests for path-related constants."""

    def test_project_root_is_path(self):
        assert isinstance(config.PROJECT_ROOT, Path)

    def test_input_dir_under_project_root(self):
        # INPUT_DIR should be a child of PROJECT_ROOT
        assert config.INPUT_DIR == config.PROJECT_ROOT / "input"
        assert str(config.INPUT_DIR).startswith(str(config.PROJECT_ROOT))

    def test_output_dir_under_project_root(self):
        # OUTPUT_DIR should be a child of PROJECT_ROOT
        assert config.OUTPUT_DIR == config.PROJECT_ROOT / "output"
        assert str(config.OUTPUT_DIR).startswith(str(config.PROJECT_ROOT))

    def test_input_dir_is_path(self):
        assert isinstance(config.INPUT_DIR, Path)

    def test_output_dir_is_path(self):
        assert isinstance(config.OUTPUT_DIR, Path)


class TestVisionAPIConstants:
    """Tests for Vision API configuration constants."""

    def test_anthropic_api_key_is_string(self):
        assert isinstance(config.ANTHROPIC_API_KEY, str)

    def test_default_vision_model_is_string(self):
        assert isinstance(config.DEFAULT_VISION_MODEL, str)

    def test_default_vision_model_not_empty(self):
        assert len(config.DEFAULT_VISION_MODEL) > 0

    def test_max_retries_is_positive_int(self):
        assert isinstance(config.MAX_RETRIES, int)
        assert config.MAX_RETRIES > 0

    def test_retry_base_delay_is_positive(self):
        assert isinstance(config.RETRY_BASE_DELAY, (int, float))
        assert config.RETRY_BASE_DELAY > 0


class TestQualityThresholds:
    """Tests for quality threshold constants."""

    def test_garbled_char_threshold_in_range(self):
        assert isinstance(config.GARBLED_CHAR_THRESHOLD, float)
        assert 0.0 <= config.GARBLED_CHAR_THRESHOLD <= 1.0

    def test_min_page_content_length_is_positive(self):
        assert isinstance(config.MIN_PAGE_CONTENT_LENGTH, int)
        assert config.MIN_PAGE_CONTENT_LENGTH > 0

    def test_sampling_similarity_threshold_in_range(self):
        assert isinstance(config.SAMPLING_SIMILARITY_THRESHOLD, float)
        assert 0.0 <= config.SAMPLING_SIMILARITY_THRESHOLD <= 1.0

    def test_sampling_page_count_is_positive(self):
        assert isinstance(config.SAMPLING_PAGE_COUNT, int)
        assert config.SAMPLING_PAGE_COUNT > 0

    def test_category_fail_threshold_in_range(self):
        assert isinstance(config.CATEGORY_FAIL_THRESHOLD, float)
        assert 0.0 <= config.CATEGORY_FAIL_THRESHOLD <= 1.0


class TestChapterSplitting:
    """Tests for chapter splitting constants."""

    def test_max_chapter_pages_is_positive(self):
        assert isinstance(config.MAX_CHAPTER_PAGES, int)
        assert config.MAX_CHAPTER_PAGES > 0

    def test_min_chapter_pages_is_positive(self):
        assert isinstance(config.MIN_CHAPTER_PAGES, int)
        assert config.MIN_CHAPTER_PAGES > 0

    def test_min_less_than_max_chapter_pages(self):
        assert config.MIN_CHAPTER_PAGES < config.MAX_CHAPTER_PAGES

    def test_max_chapter_count_is_positive(self):
        assert isinstance(config.MAX_CHAPTER_COUNT, int)
        assert config.MAX_CHAPTER_COUNT > 0

    def test_max_file_size_kb_is_positive(self):
        assert isinstance(config.MAX_FILE_SIZE_KB, int)
        assert config.MAX_FILE_SIZE_KB > 0


class TestSteps:
    """Tests for the pipeline STEPS list."""

    def test_steps_has_exactly_8_entries(self):
        assert len(config.STEPS) == 8

    def test_steps_is_list(self):
        assert isinstance(config.STEPS, list)

    def test_steps_entries_are_strings(self):
        for step in config.STEPS:
            assert isinstance(step, str), f"Step {step!r} is not a string"

    def test_steps_entries_are_non_empty(self):
        for step in config.STEPS:
            assert len(step) > 0, "Found empty step name"

    def test_steps_expected_names(self):
        expected = [
            "pdf_parse", "marker_convert", "quality_rules",
            "quality_sampling", "vision_redo", "merge",
            "descriptions", "catalog",
        ]
        assert config.STEPS == expected


class TestAllConstantsExist:
    """Verify that all expected constants are defined in the module."""

    EXPECTED_CONSTANTS = [
        "PROJECT_ROOT",
        "INPUT_DIR",
        "OUTPUT_DIR",
        "ANTHROPIC_API_KEY",
        "DEFAULT_VISION_MODEL",
        "MAX_RETRIES",
        "RETRY_BASE_DELAY",
        "GARBLED_CHAR_THRESHOLD",
        "MIN_PAGE_CONTENT_LENGTH",
        "SAMPLING_SIMILARITY_THRESHOLD",
        "SAMPLING_PAGE_COUNT",
        "CATEGORY_FAIL_THRESHOLD",
        "MAX_CHAPTER_PAGES",
        "MIN_CHAPTER_PAGES",
        "MAX_CHAPTER_COUNT",
        "MAX_FILE_SIZE_KB",
        "STEPS",
    ]

    @pytest.mark.parametrize("name", EXPECTED_CONSTANTS)
    def test_constant_exists(self, name: str):
        assert hasattr(config, name), f"config.{name} does not exist"
