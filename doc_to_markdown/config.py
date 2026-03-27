"""Configuration defaults for doc_to_markdown."""
import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Vision API
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
DEFAULT_VISION_MODEL = "claude-sonnet-4-20250514"
MAX_RETRIES = 3
RETRY_BASE_DELAY = 30  # seconds

# Quality thresholds
GARBLED_CHAR_THRESHOLD = 0.05  # 5% non-printable = garbled
MIN_PAGE_CONTENT_LENGTH = 50   # chars
SAMPLING_SIMILARITY_THRESHOLD = 0.70  # 70%
SAMPLING_PAGE_COUNT = 30
CATEGORY_FAIL_THRESHOLD = 0.50  # 50% fail rate triggers full redo of that category

# Chapter splitting
MAX_CHAPTER_PAGES = 50
MIN_CHAPTER_PAGES = 2
MAX_CHAPTER_COUNT = 100
MAX_FILE_SIZE_KB = 200

# Pipeline steps
STEPS = [
    "pdf_parse", "marker_convert", "quality_rules",
    "quality_sampling", "vision_redo", "merge",
    "descriptions", "catalog"
]
