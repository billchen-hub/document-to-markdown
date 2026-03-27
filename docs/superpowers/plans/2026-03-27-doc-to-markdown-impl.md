# Doc to Markdown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a CLI tool that converts technical PDF specs to high-quality Markdown for RAG, using Marker as the primary converter with Claude Vision API for quality enhancement.

**Architecture:** Hybrid pipeline — Marker converts all pages first, rule-based quality checks flag bad pages, Claude Vision API re-does flagged pages and generates image descriptions. Output is split by chapter with auto-generated descriptions for RAG ingestion.

**Tech Stack:** Python 3.10+, marker-pdf, PyMuPDF (fitz), anthropic SDK, click, Pillow

---

## File Structure

All source files live under `doc_to_markdown/` in the project root:

| File | Responsibility |
|------|---------------|
| `doc_to_markdown/config.py` | All thresholds, defaults, paths |
| `doc_to_markdown/pdf_parser.py` | PDF metadata: TOC, chapters, image regions, page rendering |
| `doc_to_markdown/marker_converter.py` | Wrapper around marker-pdf for batch page conversion |
| `doc_to_markdown/quality_checker.py` | Rule-based scanning + Vision API sampling comparison |
| `doc_to_markdown/vision_converter.py` | Claude Vision API: page redo + image description |
| `doc_to_markdown/merger.py` | Assemble per-page markdown into per-chapter .md files |
| `doc_to_markdown/desc_generator.py` | Generate description + keywords per chapter via Claude API |
| `doc_to_markdown/main.py` | Click CLI + 8-step pipeline orchestrator with progress tracking |
| `doc_to_markdown/__init__.py` | Package marker |
| `requirements.txt` | All dependencies |
| `USAGE.md` | User manual |
| `tests/test_config.py` | Config tests |
| `tests/test_pdf_parser.py` | PDF parser tests |
| `tests/test_quality_checker.py` | Quality checker rule tests |
| `tests/test_merger.py` | Merger tests |

---

### Task 1: Project Setup & Configuration

**Files:**
- Create: `doc_to_markdown/__init__.py`
- Create: `doc_to_markdown/config.py`
- Create: `requirements.txt`
- Create: `tests/__init__.py`
- Create: `tests/test_config.py`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p doc_to_markdown tests input output
```

- [ ] **Step 2: Write requirements.txt**

```
marker-pdf>=1.10.0
PyMuPDF>=1.25.0
anthropic>=0.80.0
click>=8.0.0
Pillow>=10.0.0
```

- [ ] **Step 3: Write config.py**

```python
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
CATEGORY_FAIL_THRESHOLD = 0.50  # 50% fail rate triggers full redo

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
```

- [ ] **Step 4: Write test_config.py and run**

```python
from doc_to_markdown.config import *

def test_defaults_exist():
    assert GARBLED_CHAR_THRESHOLD == 0.05
    assert len(STEPS) == 8
    assert MAX_CHAPTER_COUNT == 100
```

- [ ] **Step 5: Install dependencies**

```bash
pip install marker-pdf PyMuPDF anthropic click Pillow
```

- [ ] **Step 6: Commit**

---

### Task 2: PDF Parser

**Files:**
- Create: `doc_to_markdown/pdf_parser.py`
- Create: `tests/test_pdf_parser.py`

- [ ] **Step 1: Write pdf_parser.py**

Core class `PdfInfo` that extracts:
- Page count
- TOC (table of contents) from PDF metadata
- Chapter boundaries (page ranges per chapter)
- Image regions per page (bounding boxes)
- Render specific pages to PIL Images

Key methods:
```python
class PdfInfo:
    def __init__(self, pdf_path: str)
    def get_toc(self) -> list[dict]            # [{title, level, page_num}]
    def get_chapters(self) -> list[dict]       # [{title, start_page, end_page}]
    def get_page_image_regions(self, page_num: int) -> list[dict]  # [{bbox, area}]
    def has_text_layer(self, page_num: int) -> bool
    def render_page(self, page_num: int, dpi: int = 200) -> PIL.Image
    def is_encrypted(self) -> bool
```

Chapter splitting logic:
1. Read TOC, use top-level entries as chapter boundaries
2. If no TOC: scan for large-font text on each page, use as headings
3. Split chapters > 50 pages by next-level headings
4. Merge chapters < 2 pages with neighbors
5. Appendices always separate
6. Warn if > 100 chapters

- [ ] **Step 2: Write tests with the real UFS PDF**

```python
def test_parse_ufs_pdf():
    info = PdfInfo("UFS 4.1JESD220G.PDF")
    assert info.page_count > 500
    chapters = info.get_chapters()
    assert 10 < len(chapters) < 100

def test_render_page():
    info = PdfInfo("UFS 4.1JESD220G.PDF")
    img = info.render_page(0)
    assert img.width > 0 and img.height > 0
```

- [ ] **Step 3: Run tests and verify**

- [ ] **Step 4: Commit**

---

### Task 3: Marker Converter

**Files:**
- Create: `doc_to_markdown/marker_converter.py`

- [ ] **Step 1: Write marker_converter.py**

Wraps marker-pdf. Converts all pages, returns per-page markdown. Uses paginated output to split back into per-page results.

```python
class MarkerConverter:
    def __init__(self)                         # loads models once
    def convert_all(self, pdf_path: str, progress_callback=None) -> dict[int, str]
        # Returns {page_num: markdown_text}
    def convert_pages(self, pdf_path: str, page_nums: list[int]) -> dict[int, str]
```

Strategy:
- Use `paginate_output=True` to get page separators
- Split output by page separator markers
- Map back to page numbers

- [ ] **Step 2: Smoke test with a few pages of the UFS PDF**

- [ ] **Step 3: Commit**

---

### Task 4: Quality Checker

**Files:**
- Create: `doc_to_markdown/quality_checker.py`
- Create: `tests/test_quality_checker.py`

- [ ] **Step 1: Write quality_checker.py**

Two layers:

**Layer 1 - Rule-based (no API):**
```python
class QualityChecker:
    def check_page(self, page_num: int, markdown: str, has_images: bool, has_tables: bool) -> dict:
        # Returns {"pass": bool, "issues": [{"reason": str, "action": "redo"|"vision_describe"}]}

    def check_garbled(self, text: str) -> bool        # non-printable ratio > 5%
    def check_empty_table(self, text: str) -> bool     # table header only
    def check_image_missing(self, text: str, has_images: bool) -> bool
    def check_too_short(self, text: str) -> bool       # < 50 chars
    def check_format_broken(self, text: str) -> bool   # unclosed tables, broken headings
```

**Layer 2 - Sampling comparison (uses Vision API):**
```python
    def sample_and_compare(self, pdf_info, marker_results, vision_converter, sample_count=30) -> dict:
        # Random sample pages, get Vision output, compare structure
        # Returns {"flagged_pages": [...], "category_redo": {"table": bool, "image": bool}}
```

Comparison metrics: heading count, table row count, content length ratio.

- [ ] **Step 2: Write tests for rule-based checks**

```python
def test_garbled_detection():
    checker = QualityChecker()
    assert checker.check_garbled("normal text") == False
    assert checker.check_garbled("a\x00\x01\x02\x03\x04bcd") == True

def test_empty_table():
    checker = QualityChecker()
    assert checker.check_empty_table("| Header |\n|---|\n") == True
    assert checker.check_empty_table("| H |\n|---|\n| data |") == False

def test_too_short():
    checker = QualityChecker()
    assert checker.check_too_short("short") == True
    assert checker.check_too_short("x" * 100) == False
```

- [ ] **Step 3: Run tests**

- [ ] **Step 4: Commit**

---

### Task 5: Vision Converter

**Files:**
- Create: `doc_to_markdown/vision_converter.py`

- [ ] **Step 1: Write vision_converter.py**

```python
class VisionConverter:
    def __init__(self, model: str = None, api_key: str = None)

    def convert_page(self, image: PIL.Image, page_num: int) -> str:
        # Send page image to Claude Vision, get markdown back
        # Handles rate limiting with exponential backoff

    def describe_image(self, image: PIL.Image, context: str = "") -> str:
        # Get text description of a figure/diagram for RAG

    def compare_outputs(self, image: PIL.Image, marker_md: str) -> dict:
        # Ask Vision to evaluate marker output quality
        # Returns {"similarity": float, "issues": [...]}
```

Prompts:
- Page conversion: "Convert this PDF page to Markdown. Preserve all text, tables, and structure exactly."
- Image description: "Describe this technical diagram/figure for a RAG knowledge base."
- Comparison: "Compare this markdown against the page image. Rate structural similarity 0-1."

Error handling:
- 429 rate limit: exponential backoff (30s, 60s, 120s), then save progress and stop
- Invalid API key: raise immediately
- Token overflow: split page image into top/bottom halves

- [ ] **Step 2: Test with one page from UFS PDF**

- [ ] **Step 3: Commit**

---

### Task 6: Chapter Merger

**Files:**
- Create: `doc_to_markdown/merger.py`
- Create: `tests/test_merger.py`

- [ ] **Step 1: Write merger.py**

```python
class ChapterMerger:
    def merge(self, chapters: list[dict], page_markdowns: dict[int, str],
              output_dir: Path) -> list[dict]:
        # For each chapter: concatenate page markdowns, write to chapters/ dir
        # Returns [{filename, title, page_range, size_kb}]
        # Warns if any file > 200KB
        # Warns if > 100 files

    def _format_filename(self, index: int, title: str) -> str:
        # "01_introduction.md", "02_ufs_architecture.md", etc.
```

- [ ] **Step 2: Write tests**

```python
def test_merge_basic():
    merger = ChapterMerger()
    chapters = [{"title": "Intro", "start_page": 0, "end_page": 2}]
    pages = {0: "# Intro\n", 1: "Page 1 content\n", 2: "Page 2 content\n"}
    result = merger.merge(chapters, pages, tmp_path / "out")
    assert len(result) == 1
    assert (tmp_path / "out" / "chapters" / "01_intro.md").exists()
```

- [ ] **Step 3: Run tests**

- [ ] **Step 4: Commit**

---

### Task 7: Description Generator

**Files:**
- Create: `doc_to_markdown/desc_generator.py`

- [ ] **Step 1: Write desc_generator.py**

```python
class DescGenerator:
    def __init__(self, model: str = None, api_key: str = None)

    def generate(self, md_content: str, filename: str, title: str, page_range: str) -> dict:
        # Send chapter markdown to Claude API
        # Returns {"file", "title", "description", "keywords", "page_range"}

    def generate_catalog(self, descriptions: list[dict], output_dir: Path) -> None:
        # Write catalog.json with all descriptions

    def generate_readme(self, descriptions: list[dict], stats: dict, output_dir: Path) -> None:
        # Write README.md summary of conversion results
```

Prompt for description: "Read this markdown chapter from a UFS storage specification. Generate: 1) A description in Traditional Chinese (2-3 sentences) for RAG retrieval, 2) 3-6 English keywords. Output JSON format."

- [ ] **Step 2: Test with a small markdown sample**

- [ ] **Step 3: Commit**

---

### Task 8: Main Pipeline & CLI

**Files:**
- Create: `doc_to_markdown/main.py`

- [ ] **Step 1: Write main.py with Click CLI**

```python
@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
@click.option("-o", "--output", "output_dir", default=None)
@click.option("--model", default=None)
@click.option("--full-vision", is_flag=True)
@click.option("--resume", is_flag=True)
@click.option("--desc-only", is_flag=True)
def main(pdf_path, output_dir, model, full_vision, resume, desc_only):
```

Pipeline orchestration — 8 steps with progress tracking:
1. PDF parse → get chapters, image regions
2. Marker convert → all pages (or skip if --full-vision)
3. Quality rules → scan each page
4. Quality sampling → Vision API comparison on ~30 pages
5. Vision redo → re-convert flagged pages + image descriptions
6. Merge → assemble chapters
7. Descriptions → generate per-chapter
8. Catalog → write catalog.json, README.md

Progress tracking:
- Write `progress.json` after each page/step
- `--resume` reads progress, skips completed work
- Console output: `[Step N/8] description: progress ✓`

- [ ] **Step 2: Test CLI with --help**

- [ ] **Step 3: Integration test with real UFS PDF (first 3 chapters)**

- [ ] **Step 4: Full run with UFS PDF**

- [ ] **Step 5: Commit**

---

### Task 9: Documentation & Final Verification

**Files:**
- Create: `USAGE.md`

- [ ] **Step 1: Write USAGE.md**

Cover: installation, basic usage, all CLI options, output structure, cost expectations, troubleshooting.

- [ ] **Step 2: Verify full pipeline output quality**

Check:
- All chapters generated with correct content
- Tables rendered properly
- Image descriptions present
- catalog.json complete
- No garbled text in output

- [ ] **Step 3: Final commit**

---

## Execution Notes

- **Installation order matters:** Install PyMuPDF first, then marker-pdf (marker-pdf may have conflicting deps)
- **First marker-pdf run:** Will download ~2GB of model weights (surya OCR models)
- **Memory:** marker-pdf needs ~5GB VRAM (GPU) or significant RAM (CPU mode)
- **API key:** Must have `ANTHROPIC_API_KEY` env var set for Vision API steps
- **The UFS PDF** is at project root: `UFS 4.1JESD220G.PDF`
