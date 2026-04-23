"""Configuration defaults for doc_to_markdown.

Two conversion modes are supported:

- ``cli`` (default): no API calls. The current Claude Code CLI session
  is the "vision model" - it Reads rendered PNGs and Writes Markdown.
  Use this for public / non-sensitive documents.

- ``api``: calls a Vision/LLM API. Two providers are supported:

    * ``anthropic`` - uses the public Anthropic API (needs ANTHROPIC_API_KEY).
    * ``openai-compatible`` - any OpenAI-compatible endpoint such as a
      company on-prem Qwen/LLaMA deployment (needs VISION_BASE_URL and
      VISION_API_KEY).

The defaults below can all be overridden via environment variables or
the corresponding CLI flags in ``main.py``.
"""
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent.parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

# ---------------------------------------------------------------------------
# Conversion mode: "cli" | "api"
# ---------------------------------------------------------------------------
CONVERSION_MODE = os.environ.get("DOC2MD_MODE", "cli")

# ---------------------------------------------------------------------------
# Vision / LLM API settings (only used when CONVERSION_MODE == "api")
# ---------------------------------------------------------------------------
# Provider: "anthropic" | "openai-compatible"
VISION_PROVIDER = os.environ.get("VISION_PROVIDER", "anthropic")

# Base URL for openai-compatible endpoints (e.g. internal AI gateway).
# Leave empty to use the default Anthropic / OpenAI cloud endpoint.
VISION_BASE_URL = os.environ.get("VISION_BASE_URL", "")

# Generic API key. Falls back to ANTHROPIC_API_KEY for backward compatibility.
VISION_API_KEY = (
    os.environ.get("VISION_API_KEY")
    or os.environ.get("ANTHROPIC_API_KEY", "")
)

# Default model name (override via --model flag or VISION_MODEL env var)
DEFAULT_VISION_MODEL = os.environ.get(
    "VISION_MODEL",
    "claude-sonnet-4-20250514",
)

# Backward-compatible alias
ANTHROPIC_API_KEY = VISION_API_KEY

MAX_RETRIES = 3
RETRY_BASE_DELAY = 30  # seconds

# ---------------------------------------------------------------------------
# Quality thresholds
# ---------------------------------------------------------------------------
GARBLED_CHAR_THRESHOLD = 0.05  # 5% non-printable = garbled
MIN_PAGE_CONTENT_LENGTH = 50   # chars
SAMPLING_SIMILARITY_THRESHOLD = 0.70  # 70%
SAMPLING_PAGE_COUNT = 30
CATEGORY_FAIL_THRESHOLD = 0.50  # 50% fail rate triggers full redo of that category

# ---------------------------------------------------------------------------
# Chapter splitting
# ---------------------------------------------------------------------------
MAX_CHAPTER_PAGES = 50
MIN_CHAPTER_PAGES = 2
MAX_CHAPTER_COUNT = 100
MAX_FILE_SIZE_KB = 200

# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------
STEPS = [
    "pdf_parse", "marker_convert", "quality_rules",
    "quality_sampling", "vision_redo", "merge",
    "descriptions", "catalog",
]
