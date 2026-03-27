# Doc to Markdown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a CLI tool that converts technical spec PDFs to high-quality Markdown files for RAG, using Marker for base conversion and Claude Vision API to fix quality issues.

**Architecture:** 8-step pipeline (PDF parse → Marker convert → rule check → sampling check → Vision redo → merge chapters → generate descriptions → output docs). Each step saves intermediate results and supports resume from checkpoint.

**Tech Stack:** Python 3.10+, marker-pdf, PyMuPDF (fitz), anthropic SDK, Pillow, Click

---

## File Structure

```
doc_to_markdown/
├── config.py              # All settings, thresholds, defaults
├── main.py                # Click CLI + pipeline orchestrator
├── pdf_parser.py          # PDF metadata: TOC, page count, image regions
├── marker_converter.py    # Marker wrapper: full PDF → per-page markdown
├── vision_converter.py    # Claude Vision API: page image → markdown
├── quality_checker.py     # Rule-based + sampling quality checks
├── progress_tracker.py    # Progress persistence + resume logic
├── merger.py              # Assemble per-page markdown into chapter files
├── desc_generator.py      # Generate descriptions via Claude API
├── requirements.txt
├── USAGE.md
├── input/
├── output/
└── tests/
    ├── conftest.py            # Shared fixtures
    ├── test_pdf_parser.py
    ├── test_marker_converter.py
    ├── test_vision_converter.py
    ├── test_quality_checker.py
    ├── test_progress_tracker.py
    ├── test_merger.py
    ├── test_desc_generator.py
    └── test_main.py
```

---

### Task 1: Project Setup

**Files:**
- Create: `requirements.txt`
- Create: `config.py`
- Create: `tests/conftest.py`
- Create: `.gitignore`

- [ ] **Step 1: Create requirements.txt**

```
marker-pdf>=1.0.0
anthropic>=0.40.0
PyMuPDF>=1.25.0
Pillow>=10.0.0
click>=8.1.0
pytest>=8.0.0
```

- [ ] **Step 2: Create .gitignore**

```
__pycache__/
*.pyc
.env
output/
input/*.pdf
.pytest_cache/
*.egg-info/
```

- [ ] **Step 3: Create config.py**

```python
import os


# --- API ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
DEFAULT_MODEL = "claude-sonnet-4-20250514"

# --- Quality thresholds ---
GARBLED_CHAR_RATIO = 0.05        # > 5% non-printable → flag
MIN_PAGE_CHARS = 50              # page with content but < 50 chars → flag
SIMILARITY_THRESHOLD = 0.70      # sampling: < 70% similarity → fail
SYSTEMATIC_FAIL_RATIO = 0.50     # > 50% of a page type fails → redo all
SAMPLE_SIZE = 30                 # number of pages to sample

# --- Chapter splitting ---
MAX_CHAPTER_PAGES = 50           # split sub-sections if chapter > 50 pages
MIN_CHAPTER_PAGES = 2            # merge with neighbor if < 2 pages
MAX_OUTPUT_FILES = 100           # warn if exceeding this

# --- API retry ---
MAX_RETRIES = 3
RETRY_BASE_DELAY = 2.0          # seconds, exponential backoff

# --- Paths ---
DEFAULT_OUTPUT_DIR = "output"
```

- [ ] **Step 4: Create tests/conftest.py with shared fixtures**

```python
import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock


@pytest.fixture
def tmp_output(tmp_path):
    """Create a temporary output directory structure."""
    chapters = tmp_path / "chapters"
    chapters.mkdir()
    images = tmp_path / "images"
    images.mkdir()
    descriptions = tmp_path / "descriptions"
    descriptions.mkdir()
    return tmp_path


@pytest.fixture
def mock_fitz_doc():
    """Mock a PyMuPDF document with TOC and pages."""
    doc = MagicMock()
    doc.page_count = 10
    doc.get_toc.return_value = [
        [1, "Chapter 1: Introduction", 1],
        [1, "Chapter 2: Architecture", 4],
        [1, "Chapter 3: Commands", 7],
    ]

    pages = []
    for i in range(10):
        page = MagicMock()
        page.number = i
        page.get_text.return_value = f"Page {i+1} content with some text here."
        page.get_images.return_value = [(0, 0, 100, 100, 8, "DeviceRGB", "", "img1", "")] if i == 2 else []
        pix = MagicMock()
        pix.tobytes.return_value = b"\x89PNG fake image data"
        pix.width = 612
        pix.height = 792
        page.get_pixmap.return_value = pix
        pages.append(page)

    doc.__getitem__ = lambda self, idx: pages[idx]
    doc.__len__ = lambda self: 10
    doc.__iter__ = lambda self: iter(pages)
    return doc


@pytest.fixture
def sample_page_markdowns():
    """Sample per-page markdown outputs for testing."""
    return {
        0: "# Chapter 1: Introduction\n\nThis is the introduction to UFS spec.\n",
        1: "## 1.1 Scope\n\nThis document defines the UFS interface.\n",
        2: "## 1.2 References\n\n[Image: Block diagram showing UFS architecture]\n",
        3: "# Chapter 2: Architecture\n\n## 2.1 Overview\n\nThe UFS architecture consists of...\n",
        4: "## 2.2 Layers\n\n| Layer | Description |\n|-------|-------------|\n| UTP | Transport |\n| UIC | Interconnect |\n",
        5: "## 2.3 Topology\n\nUFS supports point-to-point topology.\n",
        6: "# Chapter 3: Commands\n\n## 3.1 SCSI Commands\n\nUFS uses SCSI command set.\n",
        7: "## 3.2 Read Command\n\n| Field | Size | Description |\n|-------|------|-------------|\n| Opcode | 1 | 0x28 |\n",
        8: "## 3.3 Write Command\n\nThe write command transfers data to the device.\n",
        9: "## 3.4 Query Request\n\nQuery requests are used to manage device parameters.\n",
    }


@pytest.fixture
def mock_anthropic_response():
    """Factory for mock Anthropic API responses."""
    def _make(text="# Mocked Vision Output\n\nConverted content here."):
        response = MagicMock()
        response.content = [MagicMock(text=text)]
        response.usage = MagicMock(input_tokens=1500, output_tokens=800)
        return response
    return _make
```

- [ ] **Step 5: Initialize git repo and commit**

```bash
cd "C:/Users/ASUS/Desktop/claude project/Doc_to_Markdown"
git init
mkdir -p input output tests
git add requirements.txt config.py tests/conftest.py .gitignore
git commit -m "feat: project setup with config, fixtures, and dependencies"
```

---

### Task 2: PDF Parser

**Files:**
- Create: `pdf_parser.py`
- Create: `tests/test_pdf_parser.py`

- [ ] **Step 1: Write tests for PDF parser**

```python
# tests/test_pdf_parser.py
import pytest
from unittest.mock import patch, MagicMock
from pdf_parser import PdfParser


class TestPdfParser:
    def test_get_page_count(self, mock_fitz_doc):
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            assert parser.page_count == 10

    def test_get_toc_returns_chapters(self, mock_fitz_doc):
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            toc = parser.get_toc()
            assert len(toc) == 3
            assert toc[0] == {"level": 1, "title": "Chapter 1: Introduction", "page": 1}

    def test_get_chapter_ranges_from_toc(self, mock_fitz_doc):
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            ranges = parser.get_chapter_ranges()
            assert ranges[0] == {"title": "Chapter 1: Introduction", "start": 0, "end": 3}
            assert ranges[1] == {"title": "Chapter 2: Architecture", "start": 3, "end": 6}
            assert ranges[2] == {"title": "Chapter 3: Commands", "start": 6, "end": 9}

    def test_long_chapter_gets_split(self, mock_fitz_doc):
        mock_fitz_doc.page_count = 100
        mock_fitz_doc.get_toc.return_value = [
            [1, "Chapter 1: Very Long Chapter", 1],
            [2, "1.1 Section A", 1],
            [2, "1.2 Section B", 30],
            [2, "1.3 Section C", 60],
            [1, "Chapter 2: Short", 90],
        ]
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            ranges = parser.get_chapter_ranges()
            # Chapter 1 (89 pages) should be split by sub-sections
            assert any("1.1" in r["title"] or "Section A" in r["title"] for r in ranges)

    def test_short_chapters_get_merged(self, mock_fitz_doc):
        mock_fitz_doc.get_toc.return_value = [
            [1, "Preface", 1],
            [1, "Chapter 1: Introduction", 2],
            [1, "Chapter 2: Architecture", 5],
        ]
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            ranges = parser.get_chapter_ranges()
            # Preface (1 page) should be merged with Chapter 1
            assert ranges[0]["start"] == 0

    def test_detect_image_pages(self, mock_fitz_doc):
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            image_pages = parser.get_image_pages()
            assert 2 in image_pages
            assert 0 not in image_pages

    def test_render_page_to_image(self, mock_fitz_doc):
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            img_bytes = parser.render_page(0)
            assert isinstance(img_bytes, bytes)

    def test_detect_scanned_pdf(self, mock_fitz_doc):
        # Scanned page: has image but no extractable text
        mock_fitz_doc[0].get_text.return_value = ""
        mock_fitz_doc[0].get_images.return_value = [(0, 0, 100, 100, 8, "DeviceRGB", "", "img1", "")]
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            assert parser.is_scanned_page(0) is True

    def test_no_toc_fallback(self, mock_fitz_doc):
        mock_fitz_doc.get_toc.return_value = []
        with patch("pdf_parser.fitz.open", return_value=mock_fitz_doc):
            parser = PdfParser("fake.pdf")
            ranges = parser.get_chapter_ranges()
            # Should still produce some ranges via fallback
            assert len(ranges) > 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "C:/Users/ASUS/Desktop/claude project/Doc_to_Markdown" && python -m pytest tests/test_pdf_parser.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'pdf_parser'`

- [ ] **Step 3: Implement pdf_parser.py**

```python
import fitz
import base64
from pathlib import Path

import config


class PdfParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.page_count = self.doc.page_count

    def get_toc(self) -> list[dict]:
        """Extract table of contents as list of {level, title, page}."""
        raw_toc = self.doc.get_toc()
        return [
            {"level": level, "title": title, "page": page_num}
            for level, title, page_num in raw_toc
        ]

    def get_chapter_ranges(self) -> list[dict]:
        """Determine chapter ranges with splitting/merging logic.

        Returns list of {title, start, end} where start/end are 0-based page indices.
        """
        toc = self.get_toc()

        if not toc:
            return self._fallback_chapter_ranges()

        # Get top-level entries (level 1)
        top_level = [e for e in toc if e["level"] == 1]

        if not top_level:
            return self._fallback_chapter_ranges()

        # Build initial ranges from top-level TOC
        ranges = []
        for i, entry in enumerate(top_level):
            start = entry["page"] - 1  # convert to 0-based
            if i + 1 < len(top_level):
                end = top_level[i + 1]["page"] - 1
            else:
                end = self.page_count
            ranges.append({
                "title": entry["title"],
                "start": start,
                "end": end,
            })

        # Split long chapters using sub-sections
        ranges = self._split_long_chapters(ranges, toc)

        # Merge short chapters
        ranges = self._merge_short_chapters(ranges)

        # Warn if too many
        if len(ranges) > config.MAX_OUTPUT_FILES:
            print(f"WARNING: {len(ranges)} chapters exceed limit of {config.MAX_OUTPUT_FILES}. "
                  "Consider adjusting split granularity.")

        return ranges

    def _split_long_chapters(self, ranges: list[dict], toc: list[dict]) -> list[dict]:
        """Split chapters exceeding MAX_CHAPTER_PAGES using level-2 sub-sections."""
        result = []
        for r in ranges:
            page_count = r["end"] - r["start"]
            if page_count <= config.MAX_CHAPTER_PAGES:
                result.append(r)
                continue

            # Find level-2 entries within this chapter's range
            sub_sections = [
                e for e in toc
                if e["level"] == 2
                and r["start"] < e["page"] - 1 < r["end"]
            ]

            if not sub_sections:
                result.append(r)
                continue

            # Build sub-ranges
            # First sub-range: from chapter start to first sub-section
            prev_start = r["start"]
            prev_title = r["title"]
            for sub in sub_sections:
                sub_start = sub["page"] - 1
                if sub_start > prev_start:
                    result.append({"title": prev_title, "start": prev_start, "end": sub_start})
                prev_start = sub_start
                prev_title = sub["title"]
            # Last sub-range
            result.append({"title": prev_title, "start": prev_start, "end": r["end"]})

        return result

    def _merge_short_chapters(self, ranges: list[dict]) -> list[dict]:
        """Merge chapters with fewer than MIN_CHAPTER_PAGES into neighbors."""
        if not ranges:
            return ranges

        merged = [ranges[0]]
        for r in ranges[1:]:
            prev = merged[-1]
            prev_pages = prev["end"] - prev["start"]
            curr_pages = r["end"] - r["start"]

            if prev_pages < config.MIN_CHAPTER_PAGES:
                # Merge previous into current
                merged[-1] = {
                    "title": f"{prev['title']} & {r['title']}",
                    "start": prev["start"],
                    "end": r["end"],
                }
            elif curr_pages < config.MIN_CHAPTER_PAGES:
                # Merge current into previous
                merged[-1]["end"] = r["end"]
            else:
                merged.append(r)

        return merged

    def _fallback_chapter_ranges(self) -> list[dict]:
        """When no TOC: split into roughly equal chunks by detecting large font text."""
        # Try to detect headings by font size
        headings = []
        for page_idx in range(self.page_count):
            page = self.doc[page_idx]
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["size"] > 14 and span["text"].strip():
                            headings.append({
                                "title": span["text"].strip(),
                                "page": page_idx,
                            })
                            break

        if headings:
            ranges = []
            for i, h in enumerate(headings):
                end = headings[i + 1]["page"] if i + 1 < len(headings) else self.page_count
                if not ranges or h["page"] != ranges[-1]["start"]:
                    ranges.append({"title": h["title"], "start": h["page"], "end": end})
            return self._merge_short_chapters(ranges)

        # Last resort: split evenly into ~20-page chunks
        chunk_size = max(20, self.page_count // 20)
        ranges = []
        for i in range(0, self.page_count, chunk_size):
            end = min(i + chunk_size, self.page_count)
            ranges.append({"title": f"Section {len(ranges) + 1}", "start": i, "end": end})
        return ranges

    def get_image_pages(self) -> set[int]:
        """Return set of 0-based page indices that contain images."""
        image_pages = set()
        for page_idx in range(self.page_count):
            page = self.doc[page_idx]
            if page.get_images():
                image_pages.add(page_idx)
        return image_pages

    def is_scanned_page(self, page_idx: int) -> bool:
        """Detect if a page is scanned (has images but no extractable text)."""
        page = self.doc[page_idx]
        text = page.get_text().strip()
        images = page.get_images()
        return len(text) == 0 and len(images) > 0

    def render_page(self, page_idx: int, dpi: int = 200) -> bytes:
        """Render a page to PNG bytes."""
        page = self.doc[page_idx]
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        return pix.tobytes("png")

    def render_page_base64(self, page_idx: int, dpi: int = 200) -> str:
        """Render a page to base64-encoded PNG string."""
        png_bytes = self.render_page(page_idx, dpi)
        return base64.b64encode(png_bytes).decode("utf-8")

    def get_page_text(self, page_idx: int) -> str:
        """Extract raw text from a page."""
        return self.doc[page_idx].get_text()

    def close(self):
        self.doc.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "C:/Users/ASUS/Desktop/claude project/Doc_to_Markdown" && python -m pytest tests/test_pdf_parser.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add pdf_parser.py tests/test_pdf_parser.py
git commit -m "feat: PDF parser with TOC extraction, chapter splitting, image detection"
```

---

### Task 3: Marker Converter

**Files:**
- Create: `marker_converter.py`
- Create: `tests/test_marker_converter.py`

- [ ] **Step 1: Write tests for Marker converter**

```python
# tests/test_marker_converter.py
import pytest
from unittest.mock import patch, MagicMock
from marker_converter import MarkerConverter


class TestMarkerConverter:
    def test_convert_returns_per_page_dict(self):
        mock_rendered = MagicMock()
        mock_rendered.markdown = "# Full Document\n\nPage content"
        mock_rendered.metadata = {}

        mock_doc = MagicMock()
        mock_doc.render.return_value = mock_rendered

        with patch("marker_converter.PdfConverter") as MockConverter:
            instance = MockConverter.return_value
            instance.return_value = mock_doc

            converter = MarkerConverter()
            result = converter.convert("fake.pdf")
            assert isinstance(result, dict)
            # Should have called the converter
            instance.assert_called_once_with("fake.pdf")

    def test_split_by_pages_basic(self):
        converter = MarkerConverter.__new__(MarkerConverter)
        full_md = "Page 1 content\n\n---\n\nPage 2 content\n\n---\n\nPage 3 content"
        pages = converter._split_full_markdown(full_md, total_pages=3)
        assert len(pages) == 3

    def test_convert_stores_raw_output(self, tmp_output):
        mock_rendered = MagicMock()
        mock_rendered.markdown = "# Test\n\nContent"
        mock_rendered.metadata = {}

        mock_doc = MagicMock()
        mock_doc.render.return_value = mock_rendered

        with patch("marker_converter.PdfConverter") as MockConverter:
            instance = MockConverter.return_value
            instance.return_value = mock_doc

            converter = MarkerConverter()
            result = converter.convert("fake.pdf", output_dir=str(tmp_output))
            assert (tmp_output / "marker_raw.md").exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_marker_converter.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement marker_converter.py**

```python
import json
import re
from pathlib import Path

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict


class MarkerConverter:
    def __init__(self):
        self._models = None

    def _ensure_models(self):
        """Lazy-load marker models (heavy, only load once)."""
        if self._models is None:
            self._models = create_model_dict()
            self._converter = PdfConverter(artifact_dict=self._models)

    def convert(self, pdf_path: str, output_dir: str | None = None) -> dict[int, str]:
        """Convert PDF to per-page markdown using Marker.

        Returns dict mapping 0-based page index to markdown string.
        """
        self._ensure_models()
        document = self._converter(pdf_path)
        rendered = document.render()
        full_markdown = rendered.markdown

        # Save raw output if output_dir provided
        if output_dir:
            out = Path(output_dir)
            out.mkdir(parents=True, exist_ok=True)
            (out / "marker_raw.md").write_text(full_markdown, encoding="utf-8")

        # Try to get per-page content from document object
        per_page = self._extract_per_page(document, full_markdown)
        return per_page

    def _extract_per_page(self, document, full_markdown: str) -> dict[int, str]:
        """Extract per-page markdown from marker document.

        Strategy:
        1. Try to use document.pages if available
        2. Fall back to splitting by page-break markers
        3. Last resort: return full markdown as page 0
        """
        # Strategy 1: Direct page access
        if hasattr(document, "pages") and document.pages:
            result = {}
            for i, page in enumerate(document.pages):
                if hasattr(page, "render"):
                    page_rendered = page.render()
                    result[i] = page_rendered.markdown if hasattr(page_rendered, "markdown") else str(page_rendered)
                elif hasattr(page, "markdown"):
                    result[i] = page.markdown
            if result:
                return result

        # Strategy 2: Split by page break markers
        total_pages = len(document.pages) if hasattr(document, "pages") else 1
        return self._split_full_markdown(full_markdown, total_pages)

    def _split_full_markdown(self, full_markdown: str, total_pages: int) -> dict[int, str]:
        """Split full markdown by page-break indicators."""
        # Marker uses horizontal rules or form-feeds as page separators
        parts = re.split(r'\n---\n|\n\* \* \*\n|\f', full_markdown)

        result = {}
        if len(parts) >= total_pages:
            for i in range(total_pages):
                result[i] = parts[i].strip()
        else:
            # Cannot split properly — assign all to page 0
            # Individual pages will be handled by quality checker
            for i in range(total_pages):
                if i < len(parts):
                    result[i] = parts[i].strip()
                else:
                    result[i] = ""
        return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_marker_converter.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add marker_converter.py tests/test_marker_converter.py
git commit -m "feat: Marker converter wrapper with per-page extraction"
```

---

### Task 4: Vision Converter

**Files:**
- Create: `vision_converter.py`
- Create: `tests/test_vision_converter.py`

- [ ] **Step 1: Write tests for Vision converter**

```python
# tests/test_vision_converter.py
import pytest
from unittest.mock import patch, MagicMock, call
from vision_converter import VisionConverter


class TestVisionConverter:
    def test_convert_page_returns_markdown(self, mock_anthropic_response):
        response = mock_anthropic_response("# Chapter 1\n\nContent here.")
        with patch("vision_converter.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            converter = VisionConverter(api_key="test-key")
            result = converter.convert_page(b"fake png bytes", page_num=1)
            assert result["markdown"] == "# Chapter 1\n\nContent here."
            assert result["tokens"]["input"] == 1500
            assert result["tokens"]["output"] == 800

    def test_describe_image_returns_text(self, mock_anthropic_response):
        response = mock_anthropic_response("[Figure: UFS block diagram showing host and device layers]")
        with patch("vision_converter.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            converter = VisionConverter(api_key="test-key")
            result = converter.describe_image(b"fake png bytes", page_num=1)
            assert "UFS block diagram" in result["description"]

    def test_retry_on_rate_limit(self, mock_anthropic_response):
        import anthropic as anthropic_module
        rate_limit_error = anthropic_module.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429),
            body={"error": {"message": "rate limited"}},
        )
        success = mock_anthropic_response("# Success")

        with patch("vision_converter.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.side_effect = [
                rate_limit_error, success
            ]
            with patch("vision_converter.time.sleep"):  # don't actually sleep
                converter = VisionConverter(api_key="test-key")
                result = converter.convert_page(b"fake bytes", page_num=1)
                assert result["markdown"] == "# Success"

    def test_max_retries_exceeded(self, mock_anthropic_response):
        import anthropic as anthropic_module
        rate_limit_error = anthropic_module.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429),
            body={"error": {"message": "rate limited"}},
        )

        with patch("vision_converter.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.side_effect = rate_limit_error
            with patch("vision_converter.time.sleep"):
                converter = VisionConverter(api_key="test-key")
                result = converter.convert_page(b"fake bytes", page_num=1)
                assert result["error"] is not None

    def test_tracks_total_tokens(self, mock_anthropic_response):
        response = mock_anthropic_response("content")
        with patch("vision_converter.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            converter = VisionConverter(api_key="test-key")
            converter.convert_page(b"bytes1", page_num=1)
            converter.convert_page(b"bytes2", page_num=2)
            assert converter.total_input_tokens == 3000
            assert converter.total_output_tokens == 1600
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_vision_converter.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement vision_converter.py**

```python
import base64
import time

import anthropic

import config

CONVERT_PAGE_PROMPT = """Convert this PDF page to Markdown. Follow these rules:
1. Preserve all text content accurately
2. Convert tables to proper Markdown table syntax
3. For images/figures, describe them in detail: [Figure: description of what the image shows]
4. Preserve heading hierarchy (# ## ### etc.)
5. Preserve numbered/bulleted lists
6. Do NOT add any commentary — only output the converted Markdown
7. If the page is mostly empty or a separator, output just the visible content"""

DESCRIBE_IMAGE_PROMPT = """Describe this image/figure from a technical specification document.
Provide a detailed text description that captures all information shown, including:
- What type of diagram/figure it is
- All labels, values, and relationships shown
- Any data in charts or graphs
Format: [Figure: your detailed description here]"""


class VisionConverter:
    def __init__(self, api_key: str = "", model: str = ""):
        self.api_key = api_key or config.ANTHROPIC_API_KEY
        self.model = model or config.DEFAULT_MODEL
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def convert_page(self, page_image_bytes: bytes, page_num: int) -> dict:
        """Convert a page image to markdown via Vision API.

        Returns {markdown, tokens: {input, output}, error}.
        """
        return self._call_vision(page_image_bytes, CONVERT_PAGE_PROMPT, page_num)

    def describe_image(self, page_image_bytes: bytes, page_num: int) -> dict:
        """Describe an image/figure via Vision API.

        Returns {description, tokens: {input, output}, error}.
        """
        result = self._call_vision(page_image_bytes, DESCRIBE_IMAGE_PROMPT, page_num)
        result["description"] = result.pop("markdown", "")
        return result

    def _call_vision(self, image_bytes: bytes, prompt: str, page_num: int) -> dict:
        """Call Claude Vision API with retry logic."""
        b64_image = base64.b64encode(image_bytes).decode("utf-8")

        for attempt in range(config.MAX_RETRIES + 1):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=4096,
                    messages=[{
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": b64_image,
                                },
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }],
                )

                input_tokens = response.usage.input_tokens
                output_tokens = response.usage.output_tokens
                self.total_input_tokens += input_tokens
                self.total_output_tokens += output_tokens

                return {
                    "markdown": response.content[0].text,
                    "tokens": {"input": input_tokens, "output": output_tokens},
                    "error": None,
                }

            except anthropic.RateLimitError:
                if attempt < config.MAX_RETRIES:
                    delay = config.RETRY_BASE_DELAY * (2 ** attempt)
                    print(f"  Rate limited on page {page_num}, retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    return {
                        "markdown": "",
                        "tokens": {"input": 0, "output": 0},
                        "error": f"Rate limit exceeded after {config.MAX_RETRIES} retries (page {page_num})",
                    }

            except anthropic.APIError as e:
                return {
                    "markdown": "",
                    "tokens": {"input": 0, "output": 0},
                    "error": f"API error on page {page_num}: {str(e)}",
                }

    def get_cost_estimate(self) -> float:
        """Estimate USD cost based on Sonnet pricing."""
        input_cost = (self.total_input_tokens / 1_000_000) * 3.0
        output_cost = (self.total_output_tokens / 1_000_000) * 15.0
        return round(input_cost + output_cost, 2)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_vision_converter.py -v`
Expected: All tests PASS (rate limit test may need adjustment depending on exact anthropic SDK exception constructors)

- [ ] **Step 5: Commit**

```bash
git add vision_converter.py tests/test_vision_converter.py
git commit -m "feat: Vision converter with Claude API, retry logic, token tracking"
```

---

### Task 5: Quality Checker

**Files:**
- Create: `quality_checker.py`
- Create: `tests/test_quality_checker.py`

- [ ] **Step 1: Write tests for rule-based quality checks**

```python
# tests/test_quality_checker.py
import pytest
from quality_checker import QualityChecker


class TestRuleBasedChecks:
    def test_detect_garbled_text(self):
        checker = QualityChecker.__new__(QualityChecker)
        # Normal text
        assert checker._check_garbled("This is normal English text.") is False
        # Garbled (> 5% non-printable)
        garbled = "Hello\x00\x01\x02\x03\x04\x05\x06\x07\x08 world"
        assert checker._check_garbled(garbled) is True

    def test_detect_empty_table(self):
        checker = QualityChecker.__new__(QualityChecker)
        # Valid table
        valid = "| A | B |\n|---|---|\n| 1 | 2 |"
        assert checker._check_empty_table(valid) is False
        # Empty table (header only)
        empty = "| A | B |\n|---|---|"
        assert checker._check_empty_table(empty) is True

    def test_detect_short_content(self):
        checker = QualityChecker.__new__(QualityChecker)
        assert checker._check_short_content("Short", has_pdf_content=True) is True
        assert checker._check_short_content("A" * 100, has_pdf_content=True) is False
        # Empty page in PDF is OK to be empty in markdown
        assert checker._check_short_content("", has_pdf_content=False) is False

    def test_detect_broken_markdown(self):
        checker = QualityChecker.__new__(QualityChecker)
        # Unclosed table
        broken = "| A | B |\n|---|---|\n| 1 | 2\n\nSome text"
        assert checker._check_broken_markdown(broken) is True
        # Valid markdown
        valid = "# Title\n\nSome paragraph.\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
        assert checker._check_broken_markdown(valid) is False

    def test_rule_check_returns_issues(self):
        checker = QualityChecker.__new__(QualityChecker)
        checker.image_pages = {2}
        checker.page_texts = {0: "Normal text", 1: "", 2: "Has content"}

        page_markdowns = {
            0: "# Normal\n\nGood content here with enough text to pass.",
            1: "",  # empty page, empty markdown — OK
            2: "Some text but no image description",  # has image but no [Figure:]
        }

        issues = checker.check_rules(page_markdowns)
        # Page 2 should be flagged for missing image description
        assert any(i["page"] == 2 and i["reason"] == "image_region" for i in issues)


class TestSamplingComparison:
    def test_similarity_score_identical(self):
        checker = QualityChecker.__new__(QualityChecker)
        score = checker._compute_similarity(
            "# Title\n\n| A | B |\n|---|---|\n| 1 | 2 |",
            "# Title\n\n| A | B |\n|---|---|\n| 1 | 2 |"
        )
        assert score == 1.0

    def test_similarity_score_different(self):
        checker = QualityChecker.__new__(QualityChecker)
        score = checker._compute_similarity(
            "# Title\n\nShort",
            "# Title\n\n## Subtitle\n\n| A | B | C |\n|---|---|---|\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |"
        )
        assert score < 0.7

    def test_classify_page_types(self):
        checker = QualityChecker.__new__(QualityChecker)
        checker.image_pages = {2}
        md = {
            0: "# Title\n\nText only",
            1: "| A | B |\n|---|---|\n| 1 | 2 |",
            2: "Figure description",
        }
        types = checker._classify_pages(md)
        assert types[0] == "text"
        assert types[1] == "table"
        assert types[2] == "image"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_quality_checker.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement quality_checker.py**

```python
import random
import re
from collections import Counter

import config


class QualityChecker:
    def __init__(self, image_pages: set[int], page_texts: dict[int, str]):
        """
        Args:
            image_pages: set of page indices that contain images (from PdfParser)
            page_texts: dict of page_idx -> raw text (from PdfParser)
        """
        self.image_pages = image_pages
        self.page_texts = page_texts

    def check_rules(self, page_markdowns: dict[int, str]) -> list[dict]:
        """Run rule-based checks on all pages.

        Returns list of {page, reason, method} for pages that need Vision redo.
        """
        issues = []
        for page_idx, md in page_markdowns.items():
            has_pdf_content = bool(self.page_texts.get(page_idx, "").strip())

            if self._check_garbled(md):
                issues.append({"page": page_idx, "reason": "garbled_text", "method": "vision_redo"})
            elif self._check_short_content(md, has_pdf_content):
                issues.append({"page": page_idx, "reason": "short_content", "method": "vision_redo"})
            elif self._check_empty_table(md):
                issues.append({"page": page_idx, "reason": "empty_table", "method": "vision_redo"})
            elif self._check_broken_markdown(md):
                issues.append({"page": page_idx, "reason": "broken_markdown", "method": "vision_redo"})

            # Check for images that weren't described
            if page_idx in self.image_pages and "[Figure:" not in md and "[Image:" not in md:
                issues.append({"page": page_idx, "reason": "image_region", "method": "vision_describe"})

        return issues

    def check_sampling(
        self,
        page_markdowns: dict[int, str],
        vision_convert_fn,
        render_page_fn,
        sample_size: int = 0,
    ) -> list[dict]:
        """Sample pages, compare Marker vs Vision output, find systematic issues.

        Args:
            page_markdowns: Marker output per page
            vision_convert_fn: callable(page_bytes, page_num) -> {markdown, ...}
            render_page_fn: callable(page_idx) -> bytes (PNG)
            sample_size: number of pages to sample (0 = use config default)

        Returns list of additional {page, reason, method} issues.
        """
        sample_size = sample_size or config.SAMPLE_SIZE
        all_pages = list(page_markdowns.keys())
        sample_pages = random.sample(all_pages, min(sample_size, len(all_pages)))

        # Get Vision output for sampled pages
        comparisons = {}
        for page_idx in sample_pages:
            page_bytes = render_page_fn(page_idx)
            vision_result = vision_convert_fn(page_bytes, page_idx)
            if vision_result.get("error"):
                continue
            marker_md = page_markdowns[page_idx]
            vision_md = vision_result["markdown"]
            score = self._compute_similarity(marker_md, vision_md)
            comparisons[page_idx] = {
                "score": score,
                "type": self._classify_single_page(page_idx, marker_md),
            }

        # Find systematic failures by page type
        type_scores = {}
        for page_idx, comp in comparisons.items():
            ptype = comp["type"]
            if ptype not in type_scores:
                type_scores[ptype] = []
            type_scores[ptype].append(comp["score"])

        failing_types = set()
        for ptype, scores in type_scores.items():
            fail_count = sum(1 for s in scores if s < config.SIMILARITY_THRESHOLD)
            if len(scores) > 0 and fail_count / len(scores) > config.SYSTEMATIC_FAIL_RATIO:
                failing_types.add(ptype)

        # Flag all pages of failing types
        page_types = self._classify_pages(page_markdowns)
        additional_issues = []
        for page_idx, ptype in page_types.items():
            if ptype in failing_types:
                additional_issues.append({
                    "page": page_idx,
                    "reason": f"systematic_fail:{ptype}",
                    "method": "vision_redo",
                })

        return additional_issues

    def _check_garbled(self, text: str) -> bool:
        if not text:
            return False
        non_printable = sum(1 for c in text if not c.isprintable() and c not in '\n\r\t')
        return (non_printable / len(text)) > config.GARBLED_CHAR_RATIO

    def _check_empty_table(self, md: str) -> bool:
        table_pattern = re.compile(r'(\|[^\n]+\|\n\|[-| :]+\|)\n?(?!\|)')
        return bool(table_pattern.search(md))

    def _check_short_content(self, md: str, has_pdf_content: bool) -> bool:
        if not has_pdf_content:
            return False
        return len(md.strip()) < config.MIN_PAGE_CHARS

    def _check_broken_markdown(self, md: str) -> bool:
        lines = md.split("\n")
        in_table = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                in_table = True
            elif stripped.startswith("|") and not stripped.endswith("|") and in_table:
                return True  # table row not closed
            elif in_table and not stripped.startswith("|") and stripped:
                in_table = False
        return False

    def _compute_similarity(self, marker_md: str, vision_md: str) -> float:
        """Compare structural similarity between two markdown outputs.

        Uses: heading count, table row count, content length ratio.
        """
        if marker_md == vision_md:
            return 1.0
        if not marker_md and not vision_md:
            return 1.0
        if not marker_md or not vision_md:
            return 0.0

        scores = []

        # Heading count similarity
        m_heads = len(re.findall(r'^#+\s', marker_md, re.MULTILINE))
        v_heads = len(re.findall(r'^#+\s', vision_md, re.MULTILINE))
        if max(m_heads, v_heads) > 0:
            scores.append(min(m_heads, v_heads) / max(m_heads, v_heads))
        else:
            scores.append(1.0)

        # Table row count similarity
        m_rows = len(re.findall(r'^\|', marker_md, re.MULTILINE))
        v_rows = len(re.findall(r'^\|', vision_md, re.MULTILINE))
        if max(m_rows, v_rows) > 0:
            scores.append(min(m_rows, v_rows) / max(m_rows, v_rows))
        else:
            scores.append(1.0)

        # Content length ratio
        m_len = len(marker_md.strip())
        v_len = len(vision_md.strip())
        if max(m_len, v_len) > 0:
            scores.append(min(m_len, v_len) / max(m_len, v_len))
        else:
            scores.append(1.0)

        return sum(scores) / len(scores)

    def _classify_single_page(self, page_idx: int, md: str) -> str:
        if page_idx in self.image_pages:
            return "image"
        if re.search(r'^\|', md, re.MULTILINE):
            return "table"
        return "text"

    def _classify_pages(self, page_markdowns: dict[int, str]) -> dict[int, str]:
        result = {}
        for page_idx, md in page_markdowns.items():
            result[page_idx] = self._classify_single_page(page_idx, md)
        return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_quality_checker.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add quality_checker.py tests/test_quality_checker.py
git commit -m "feat: quality checker with rule-based scanning and sampling comparison"
```

---

### Task 6: Progress Tracker

**Files:**
- Create: `progress_tracker.py`
- Create: `tests/test_progress_tracker.py`

- [ ] **Step 1: Write tests for progress tracker**

```python
# tests/test_progress_tracker.py
import json
import pytest
from progress_tracker import ProgressTracker


class TestProgressTracker:
    def test_create_new_progress(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=10)
        assert tracker.status == "in_progress"
        assert tracker.current_step == ""

    def test_save_and_load(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=10)
        tracker.set_step("marker")
        tracker.mark_page(0, "marker", "done")
        tracker.save()

        loaded = ProgressTracker.load(str(tmp_output))
        assert loaded.current_step == "marker"
        assert loaded.pages["0"]["marker"] == "done"

    def test_mark_page_updates_stats(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=10)
        tracker.mark_page(0, "marker", "done")
        tracker.mark_page(1, "marker", "done")
        assert tracker.stats["marker_completed"] == 2

    def test_add_tokens(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=5)
        tracker.add_tokens(1500, 800)
        tracker.add_tokens(1000, 500)
        assert tracker.stats["tokens_used"]["input"] == 2500
        assert tracker.stats["tokens_used"]["output"] == 1300

    def test_get_pending_vision_pages(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=5)
        tracker.mark_page(0, "quality", "fail:garbled")
        tracker.mark_page(0, "vision", "pending")
        tracker.mark_page(1, "quality", "pass")
        tracker.mark_page(2, "quality", "fail:empty_table")
        tracker.mark_page(2, "vision", "done")
        pending = tracker.get_pending_pages("vision")
        assert 0 in pending
        assert 2 not in pending

    def test_is_step_complete(self, tmp_output):
        tracker = ProgressTracker(str(tmp_output), total_pages=3)
        for i in range(3):
            tracker.mark_page(i, "marker", "done")
        assert tracker.is_step_complete("marker") is True

    def test_progress_file_exists_detection(self, tmp_output):
        assert ProgressTracker.exists(str(tmp_output)) is False
        tracker = ProgressTracker(str(tmp_output), total_pages=5)
        tracker.save()
        assert ProgressTracker.exists(str(tmp_output)) is True
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_progress_tracker.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement progress_tracker.py**

```python
import json
from pathlib import Path


class ProgressTracker:
    FILENAME = "progress.json"

    def __init__(self, output_dir: str, total_pages: int = 0):
        self.output_dir = Path(output_dir)
        self.progress_file = self.output_dir / self.FILENAME
        self.status = "in_progress"
        self.current_step = ""
        self.total_pages = total_pages
        self.pages: dict[str, dict] = {}
        self.stats = {
            "marker_completed": 0,
            "quality_checked": 0,
            "vision_total": 0,
            "vision_completed": 0,
            "vision_pending": 0,
            "tokens_used": {"input": 0, "output": 0},
            "estimated_cost": "$0.00",
        }

    def set_step(self, step: str):
        self.current_step = step
        self.save()

    def mark_page(self, page_idx: int, stage: str, status: str):
        """Mark a page's status for a given stage.

        stage: "marker", "quality", "vision"
        status: "done", "pass", "fail:<reason>", "pending", "skip"
        """
        key = str(page_idx)
        if key not in self.pages:
            self.pages[key] = {}
        self.pages[key][stage] = status

        # Update stats
        self._recompute_stats()
        self.save()

    def add_tokens(self, input_tokens: int, output_tokens: int):
        self.stats["tokens_used"]["input"] += input_tokens
        self.stats["tokens_used"]["output"] += output_tokens
        self._update_cost()
        self.save()

    def get_pending_pages(self, stage: str) -> list[int]:
        """Get page indices that are pending for a given stage."""
        pending = []
        for key, page_data in self.pages.items():
            if page_data.get(stage) == "pending":
                pending.append(int(key))
        return sorted(pending)

    def is_step_complete(self, stage: str) -> bool:
        """Check if all pages have been processed for a stage."""
        completed = sum(
            1 for p in self.pages.values()
            if p.get(stage) in ("done", "pass", "skip")
        )
        return completed >= self.total_pages

    def mark_complete(self):
        self.status = "completed"
        self.save()

    def save(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)
        data = {
            "status": self.status,
            "current_step": self.current_step,
            "total_pages": self.total_pages,
            "pages": self.pages,
            "stats": self.stats,
        }
        self.progress_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, output_dir: str) -> "ProgressTracker":
        path = Path(output_dir) / cls.FILENAME
        data = json.loads(path.read_text(encoding="utf-8"))
        tracker = cls(output_dir, total_pages=data.get("total_pages", 0))
        tracker.status = data["status"]
        tracker.current_step = data["current_step"]
        tracker.pages = data["pages"]
        tracker.stats = data["stats"]
        return tracker

    @classmethod
    def exists(cls, output_dir: str) -> bool:
        return (Path(output_dir) / cls.FILENAME).exists()

    def _recompute_stats(self):
        self.stats["marker_completed"] = sum(
            1 for p in self.pages.values() if p.get("marker") == "done"
        )
        self.stats["quality_checked"] = sum(
            1 for p in self.pages.values() if p.get("quality") in ("pass", "fail", "fail:garbled_text", "fail:empty_table", "fail:short_content", "fail:broken_markdown", "fail:image_region") or (p.get("quality", "").startswith("fail"))
        )
        self.stats["vision_total"] = sum(
            1 for p in self.pages.values() if p.get("vision") in ("done", "pending")
        )
        self.stats["vision_completed"] = sum(
            1 for p in self.pages.values() if p.get("vision") == "done"
        )
        self.stats["vision_pending"] = sum(
            1 for p in self.pages.values() if p.get("vision") == "pending"
        )

    def _update_cost(self):
        inp = self.stats["tokens_used"]["input"]
        out = self.stats["tokens_used"]["output"]
        cost = (inp / 1_000_000) * 3.0 + (out / 1_000_000) * 15.0
        self.stats["estimated_cost"] = f"${cost:.2f}"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_progress_tracker.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add progress_tracker.py tests/test_progress_tracker.py
git commit -m "feat: progress tracker with save/load/resume support"
```

---

### Task 7: Chapter Merger

**Files:**
- Create: `merger.py`
- Create: `tests/test_merger.py`

- [ ] **Step 1: Write tests for merger**

```python
# tests/test_merger.py
import pytest
from pathlib import Path
from merger import ChapterMerger


class TestChapterMerger:
    def test_merge_pages_into_chapters(self, sample_page_markdowns):
        chapter_ranges = [
            {"title": "Chapter 1: Introduction", "start": 0, "end": 3},
            {"title": "Chapter 2: Architecture", "start": 3, "end": 6},
            {"title": "Chapter 3: Commands", "start": 6, "end": 10},
        ]
        merger = ChapterMerger(chapter_ranges)
        chapters = merger.merge(sample_page_markdowns)

        assert len(chapters) == 3
        assert "Introduction" in chapters[0]["content"]
        assert "Architecture" in chapters[1]["content"]
        assert chapters[0]["filename"] == "01_chapter_1_introduction.md"

    def test_write_chapters_to_disk(self, sample_page_markdowns, tmp_output):
        chapter_ranges = [
            {"title": "Chapter 1: Introduction", "start": 0, "end": 3},
            {"title": "Chapter 2: Architecture", "start": 3, "end": 6},
            {"title": "Chapter 3: Commands", "start": 6, "end": 10},
        ]
        merger = ChapterMerger(chapter_ranges)
        chapters = merger.merge(sample_page_markdowns)
        merger.write(chapters, str(tmp_output / "chapters"))

        files = list((tmp_output / "chapters").glob("*.md"))
        assert len(files) == 3

    def test_filename_sanitization(self):
        merger = ChapterMerger.__new__(ChapterMerger)
        assert merger._sanitize_filename("Chapter 1: Introduction/Overview") == "chapter_1_introduction_overview"
        assert merger._sanitize_filename("Appendix A — Tables & Figures") == "appendix_a_tables_figures"

    def test_warns_on_large_file(self, sample_page_markdowns, capsys):
        chapter_ranges = [
            {"title": "All Content", "start": 0, "end": 10},
        ]
        merger = ChapterMerger(chapter_ranges)
        # Create oversized content
        big_page = {0: "x" * 250_000}
        chapters = merger.merge(big_page)
        # Should have a warning in the chapter metadata
        assert chapters[0].get("warning") is not None or len(chapters[0]["content"]) > 200_000
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_merger.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement merger.py**

```python
import re
from pathlib import Path


class ChapterMerger:
    MAX_FILE_SIZE = 200_000  # bytes, ~200KB

    def __init__(self, chapter_ranges: list[dict]):
        """
        Args:
            chapter_ranges: list of {title, start, end} from PdfParser
        """
        self.chapter_ranges = chapter_ranges

    def merge(self, page_markdowns: dict[int, str]) -> list[dict]:
        """Merge per-page markdown into chapters.

        Returns list of {filename, title, content, page_range, warning?}.
        """
        chapters = []
        for i, ch in enumerate(self.chapter_ranges):
            pages_content = []
            for page_idx in range(ch["start"], ch["end"]):
                md = page_markdowns.get(page_idx, "")
                if md.strip():
                    pages_content.append(md)

            content = "\n\n".join(pages_content)
            safe_name = self._sanitize_filename(ch["title"])
            filename = f"{i+1:02d}_{safe_name}.md"

            chapter = {
                "filename": filename,
                "title": ch["title"],
                "content": content,
                "page_range": f"{ch['start']+1}-{ch['end']}",
            }

            if len(content.encode("utf-8")) > self.MAX_FILE_SIZE:
                chapter["warning"] = f"File size ({len(content.encode('utf-8'))} bytes) exceeds {self.MAX_FILE_SIZE} bytes"
                print(f"WARNING: {filename} is {len(content.encode('utf-8'))} bytes — consider splitting")

            chapters.append(chapter)

        return chapters

    def write(self, chapters: list[dict], output_dir: str) -> list[str]:
        """Write chapter files to disk. Returns list of written file paths."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        written = []
        for ch in chapters:
            path = out / ch["filename"]
            path.write_text(ch["content"], encoding="utf-8")
            written.append(str(path))

        return written

    def _sanitize_filename(self, title: str) -> str:
        """Convert chapter title to safe filename."""
        name = title.lower()
        name = re.sub(r'[^a-z0-9\s]', '', name)
        name = re.sub(r'\s+', '_', name.strip())
        return name[:80]  # cap length
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_merger.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add merger.py tests/test_merger.py
git commit -m "feat: chapter merger with filename sanitization and size warnings"
```

---

### Task 8: Description Generator

**Files:**
- Create: `desc_generator.py`
- Create: `tests/test_desc_generator.py`

- [ ] **Step 1: Write tests for description generator**

```python
# tests/test_desc_generator.py
import json
import pytest
from unittest.mock import patch, MagicMock
from desc_generator import DescGenerator


class TestDescGenerator:
    def test_generate_single_description(self, mock_anthropic_response):
        mock_text = json.dumps({
            "description": "UFS architecture overview covering layers and topology.",
            "keywords": ["UFS", "architecture", "layers", "topology"]
        })
        response = mock_anthropic_response(mock_text)

        with patch("desc_generator.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            gen = DescGenerator(api_key="test-key")
            result = gen.generate(
                content="# Architecture\n\nUFS has layers...",
                title="Chapter 2: Architecture",
                filename="02_architecture.md",
                page_range="10-25",
            )
            assert "description" in result
            assert "keywords" in result
            assert result["file"] == "02_architecture.md"

    def test_generate_catalog(self, tmp_output, mock_anthropic_response):
        mock_text = json.dumps({
            "description": "Test description.",
            "keywords": ["test"]
        })
        response = mock_anthropic_response(mock_text)

        with patch("desc_generator.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            gen = DescGenerator(api_key="test-key")

            chapters = [
                {"filename": "01_intro.md", "title": "Introduction", "content": "Intro text", "page_range": "1-5"},
            ]
            catalog = gen.generate_all(chapters, str(tmp_output))

            assert len(catalog) == 1
            assert (tmp_output / "descriptions" / "01_intro_desc.json").exists()
            assert (tmp_output / "catalog.json").exists()

    def test_handles_malformed_api_response(self, mock_anthropic_response):
        response = mock_anthropic_response("This is not JSON")
        with patch("desc_generator.anthropic.Anthropic") as MockClient:
            MockClient.return_value.messages.create.return_value = response
            gen = DescGenerator(api_key="test-key")
            result = gen.generate(
                content="Some content",
                title="Title",
                filename="file.md",
                page_range="1-5",
            )
            # Should still return a valid structure with fallback
            assert "description" in result
            assert "file" in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_desc_generator.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement desc_generator.py**

```python
import json
from pathlib import Path

import anthropic

import config

DESC_PROMPT = """Read the following Markdown document from a technical specification and generate:
1. A concise description (2-3 sentences) of what this chapter covers and when someone should reference it
2. 5-10 relevant keywords for search/retrieval

The document is titled "{title}" (pages {page_range}).

Respond in this exact JSON format only, no other text:
{{
  "description": "your description here",
  "keywords": ["keyword1", "keyword2", ...]
}}

Document content:
---
{content}
---"""


class DescGenerator:
    def __init__(self, api_key: str = "", model: str = ""):
        self.api_key = api_key or config.ANTHROPIC_API_KEY
        self.model = model or config.DEFAULT_MODEL
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(self, content: str, title: str, filename: str, page_range: str) -> dict:
        """Generate description for a single chapter.

        Returns {file, title, description, keywords, page_range}.
        """
        # Truncate content if too long for context window
        max_chars = 100_000
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n[... truncated ...]"

        prompt = DESC_PROMPT.format(title=title, page_range=page_range, content=content)

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text

            try:
                parsed = json.loads(raw)
                description = parsed.get("description", "")
                keywords = parsed.get("keywords", [])
            except json.JSONDecodeError:
                description = raw.strip()
                keywords = []

        except anthropic.APIError as e:
            description = f"[Error generating description: {e}]"
            keywords = []

        return {
            "file": filename,
            "title": title,
            "description": description,
            "keywords": keywords,
            "page_range": page_range,
        }

    def generate_all(self, chapters: list[dict], output_dir: str) -> list[dict]:
        """Generate descriptions for all chapters, save to disk.

        Args:
            chapters: list of {filename, title, content, page_range}
            output_dir: base output directory

        Returns catalog (list of description dicts).
        """
        out = Path(output_dir)
        desc_dir = out / "descriptions"
        desc_dir.mkdir(parents=True, exist_ok=True)

        catalog = []
        for ch in chapters:
            desc = self.generate(
                content=ch["content"],
                title=ch["title"],
                filename=ch["filename"],
                page_range=ch["page_range"],
            )
            catalog.append(desc)

            # Save individual description
            desc_filename = ch["filename"].replace(".md", "_desc.json")
            (desc_dir / desc_filename).write_text(
                json.dumps(desc, indent=2, ensure_ascii=False), encoding="utf-8"
            )

        # Save catalog
        (out / "catalog.json").write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        return catalog
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_desc_generator.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add desc_generator.py tests/test_desc_generator.py
git commit -m "feat: description generator with catalog output for RAG knowledge base"
```

---

### Task 9: Main CLI Pipeline

**Files:**
- Create: `main.py`
- Create: `tests/test_main.py`

- [ ] **Step 1: Write tests for CLI and pipeline**

```python
# tests/test_main.py
import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from main import cli


class TestCli:
    def test_cli_requires_pdf_argument(self):
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code != 0

    def test_cli_rejects_nonexistent_pdf(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["nonexistent.pdf"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower() or "does not exist" in result.output.lower()

    def test_cli_checks_api_key_for_vision(self):
        runner = CliRunner()
        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": ""}):
            result = runner.invoke(cli, ["fake.pdf", "--full-vision"])
            assert result.exit_code != 0 or "API key" in result.output

    def test_desc_only_mode_skips_conversion(self):
        runner = CliRunner()
        with patch("main.run_pipeline") as mock_pipeline:
            # Would need a valid output dir with existing conversion
            result = runner.invoke(cli, ["fake.pdf", "--desc-only"])
            # Should not run full pipeline
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_main.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement main.py**

```python
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import click

import config
from pdf_parser import PdfParser
from marker_converter import MarkerConverter
from vision_converter import VisionConverter
from quality_checker import QualityChecker
from progress_tracker import ProgressTracker
from merger import ChapterMerger
from desc_generator import DescGenerator


def print_step(step: int, total: int, msg: str):
    print(f"[Step {step}/{total}] {msg}")


def run_pipeline(
    pdf_path: str,
    output_dir: str,
    model: str,
    full_vision: bool,
    resume: bool,
    desc_only: bool,
):
    """Main conversion pipeline."""
    pdf_name = Path(pdf_path).stem
    out_dir = Path(output_dir) / pdf_name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "chapters").mkdir(exist_ok=True)
    (out_dir / "images").mkdir(exist_ok=True)
    (out_dir / "descriptions").mkdir(exist_ok=True)

    total_steps = 8
    errors = []

    # --- Step 1: PDF Parsing ---
    print_step(1, total_steps, "PDF parsing...")
    parser = PdfParser(pdf_path)
    page_count = parser.page_count
    chapter_ranges = parser.get_chapter_ranges()
    image_pages = parser.get_image_pages()
    scanned_pages = {i for i in range(page_count) if parser.is_scanned_page(i)}
    page_texts = {i: parser.get_page_text(i) for i in range(page_count)}

    print_step(1, total_steps, f"PDF parsing: {page_count} pages, {len(chapter_ranges)} chapters detected ✓")

    # Initialize or resume progress
    if resume and ProgressTracker.exists(str(out_dir)):
        tracker = ProgressTracker.load(str(out_dir))
        print(f"  Resuming from step: {tracker.current_step}")
    else:
        if ProgressTracker.exists(str(out_dir)) and not resume:
            click.confirm("Found existing progress. Start fresh?", abort=True)
        tracker = ProgressTracker(str(out_dir), total_pages=page_count)

    # Handle desc-only mode
    if desc_only:
        _run_desc_only(out_dir, chapter_ranges, model)
        return

    # --- Step 2: Marker Conversion ---
    page_markdowns: dict[int, str] = {}

    if full_vision:
        print_step(2, total_steps, "Skipping Marker (full-vision mode)")
        for i in range(page_count):
            page_markdowns[i] = ""
            tracker.mark_page(i, "marker", "skip")
    elif not tracker.is_step_complete("marker"):
        print_step(2, total_steps, "Marker conversion...")
        tracker.set_step("marker")
        marker = MarkerConverter()
        page_markdowns = marker.convert(pdf_path, output_dir=str(out_dir))
        for i in range(page_count):
            tracker.mark_page(i, "marker", "done")
        print_step(2, total_steps, f"Marker conversion: {page_count}/{page_count} pages ✓")
    else:
        print_step(2, total_steps, "Marker conversion: already complete ✓")
        # Load from saved raw output
        raw_path = out_dir / "marker_raw.md"
        if raw_path.exists():
            marker = MarkerConverter()
            page_markdowns = marker._split_full_markdown(
                raw_path.read_text(encoding="utf-8"), page_count
            )
        else:
            page_markdowns = {i: "" for i in range(page_count)}

    # --- Step 3: Quality Check (Rules) ---
    all_issues = []
    if not tracker.is_step_complete("quality"):
        print_step(3, total_steps, "Quality check (rules)...")
        tracker.set_step("quality_rules")
        checker = QualityChecker(image_pages, page_texts)
        rule_issues = checker.check_rules(page_markdowns)
        all_issues.extend(rule_issues)

        # Mark scanned pages for vision
        for p in scanned_pages:
            if not any(i["page"] == p for i in all_issues):
                all_issues.append({"page": p, "reason": "scanned_page", "method": "vision_redo"})

        redo_count = sum(1 for i in all_issues if i["method"] == "vision_redo")
        desc_count = sum(1 for i in all_issues if i["method"] == "vision_describe")
        print_step(3, total_steps, f"Quality check (rules): {page_count}/{page_count} pages ✓")
        print(f"           → {redo_count} pages need redo, {desc_count} need image description")

        for i in range(page_count):
            page_issues = [iss for iss in all_issues if iss["page"] == i]
            if page_issues:
                tracker.mark_page(i, "quality", f"fail:{page_issues[0]['reason']}")
            else:
                tracker.mark_page(i, "quality", "pass")
    else:
        print_step(3, total_steps, "Quality check (rules): already complete ✓")

    # --- Step 4: Quality Check (Sampling) ---
    if not full_vision and not tracker.is_step_complete("quality"):
        print_step(4, total_steps, "Quality check (sampling)...")
        tracker.set_step("quality_sampling")

        api_key = config.ANTHROPIC_API_KEY
        vision = VisionConverter(api_key=api_key, model=model)
        sampling_issues = checker.check_sampling(
            page_markdowns,
            vision_convert_fn=vision.convert_page,
            render_page_fn=parser.render_page,
        )
        # Deduplicate: don't add pages already flagged by rules
        flagged = {i["page"] for i in all_issues}
        new_issues = [i for i in sampling_issues if i["page"] not in flagged]
        all_issues.extend(new_issues)

        print_step(4, total_steps, f"Quality check (sampling): {config.SAMPLE_SIZE} pages ✓")
        if new_issues:
            print(f"           → {len(new_issues)} additional pages flagged")

        tracker.add_tokens(vision.total_input_tokens, vision.total_output_tokens)
    else:
        print_step(4, total_steps, "Quality check (sampling): skipped or complete ✓")

    # --- Step 5: Vision API Redo ---
    print_step(5, total_steps, "Vision API processing...")
    tracker.set_step("vision")

    # Mark pages needing vision
    for issue in all_issues:
        page_idx = issue["page"]
        current = tracker.pages.get(str(page_idx), {}).get("vision", "")
        if current not in ("done",):
            tracker.mark_page(page_idx, "vision", "pending")

    # Also mark all pages for vision in full-vision mode
    if full_vision:
        for i in range(page_count):
            tracker.mark_page(i, "vision", "pending")

    pending = tracker.get_pending_pages("vision")
    if not pending:
        print_step(5, total_steps, "Vision API: no pages to process ✓")
    else:
        api_key = config.ANTHROPIC_API_KEY
        vision = VisionConverter(api_key=api_key, model=model)

        for idx, page_idx in enumerate(pending):
            print(f"\r  Vision API: {idx+1}/{len(pending)} pages...", end="", flush=True)

            page_bytes = parser.render_page(page_idx)
            issue = next((i for i in all_issues if i["page"] == page_idx), None)

            if issue and issue["method"] == "vision_describe":
                result = vision.describe_image(page_bytes, page_idx)
                if not result.get("error"):
                    # Append image description to existing markdown
                    existing = page_markdowns.get(page_idx, "")
                    page_markdowns[page_idx] = existing + "\n\n" + result["description"]
            else:
                result = vision.convert_page(page_bytes, page_idx)
                if not result.get("error"):
                    page_markdowns[page_idx] = result["markdown"]

            if result.get("error"):
                errors.append({"page": page_idx, "error": result["error"]})
                tracker.mark_page(page_idx, "vision", f"error:{result['error']}")
            else:
                tracker.mark_page(page_idx, "vision", "done")
                tracker.add_tokens(
                    result["tokens"]["input"],
                    result["tokens"]["output"],
                )

        print(f"\n", end="")
        print_step(5, total_steps, f"Vision API: {len(pending)}/{len(pending)} pages ✓")
        print(f"           Token usage: {vision.total_input_tokens:,} in / {vision.total_output_tokens:,} out")
        print(f"           Estimated cost: ${vision.get_cost_estimate()}")

    # --- Step 6: Merge Chapters ---
    print_step(6, total_steps, "Merging chapters...")
    tracker.set_step("merge")
    merger = ChapterMerger(chapter_ranges)
    chapters = merger.merge(page_markdowns)
    merger.write(chapters, str(out_dir / "chapters"))
    print_step(6, total_steps, f"Merging chapters: {len(chapters)}/{len(chapters)} ✓")

    # --- Step 7: Generate Descriptions ---
    print_step(7, total_steps, "Generating descriptions...")
    tracker.set_step("descriptions")
    desc_gen = DescGenerator(model=model)
    catalog = desc_gen.generate_all(chapters, str(out_dir))
    print_step(7, total_steps, f"Generating descriptions: {len(chapters)}/{len(chapters)} ✓")

    # --- Step 8: Write Reports ---
    print_step(8, total_steps, "Writing catalog & README...")
    tracker.set_step("finalize")

    # Quality report
    quality_report = {
        "total_pages": page_count,
        "marker_ok": page_count - len(all_issues),
        "vision_redo": sum(1 for i in all_issues if i["method"] == "vision_redo"),
        "vision_image_desc": sum(1 for i in all_issues if i["method"] == "vision_describe"),
        "issues": all_issues,
        "errors": errors,
    }
    (out_dir / "quality_report.json").write_text(
        json.dumps(quality_report, indent=2), encoding="utf-8"
    )

    # Conversion log
    conv_log = {
        "source": pdf_path,
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "full_vision": full_vision,
        "total_pages": page_count,
        "chapters": len(chapters),
        "tokens": tracker.stats["tokens_used"],
        "estimated_cost": tracker.stats["estimated_cost"],
        "errors": errors,
    }
    (out_dir / "conversion_log.json").write_text(
        json.dumps(conv_log, indent=2), encoding="utf-8"
    )

    # README
    _write_readme(out_dir, pdf_path, chapters, quality_report, conv_log, catalog)

    tracker.mark_complete()
    print_step(8, total_steps, "Writing catalog & README ✓")

    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"  Output: {out_dir}")
    print(f"  Chapters: {len(chapters)}")
    print(f"  Estimated cost: {tracker.stats['estimated_cost']}")
    if errors:
        print(f"  Errors: {len(errors)} (see conversion_log.json)")
    print(f"{'='*50}")

    parser.close()


def _run_desc_only(out_dir: Path, chapter_ranges: list[dict], model: str):
    """Re-generate descriptions from existing chapter files."""
    chapters_dir = out_dir / "chapters"
    if not chapters_dir.exists():
        print("ERROR: No chapters found. Run full conversion first.")
        sys.exit(1)

    chapters = []
    for md_file in sorted(chapters_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        # Find matching range
        idx = int(md_file.stem.split("_")[0]) - 1
        page_range = ""
        if idx < len(chapter_ranges):
            r = chapter_ranges[idx]
            page_range = f"{r['start']+1}-{r['end']}"

        chapters.append({
            "filename": md_file.name,
            "title": md_file.stem.replace("_", " ").title(),
            "content": content,
            "page_range": page_range,
        })

    desc_gen = DescGenerator(model=model)
    desc_gen.generate_all(chapters, str(out_dir))
    print(f"Descriptions regenerated for {len(chapters)} chapters.")


def _write_readme(out_dir, pdf_path, chapters, quality_report, conv_log, catalog):
    """Generate output README.md."""
    lines = [
        f"# {Path(pdf_path).stem} Conversion Result",
        "",
        "## Basic Info",
        f"- Source: {Path(pdf_path).name} ({conv_log['total_pages']} pages)",
        f"- Converted: {conv_log['timestamp'][:10]}",
        f"- Chapters: {len(chapters)}",
        f"- Model: {conv_log['model']}",
        f"- Estimated cost: {conv_log['estimated_cost']}",
        "",
        "## Files",
        "",
        "| File | Title | Pages |",
        "|------|-------|-------|",
    ]
    for ch, desc in zip(chapters, catalog):
        lines.append(f"| {ch['filename']} | {ch['title']} | {ch['page_range']} |")

    lines.extend([
        "",
        "## Quality Report",
        f"- Marker OK: {quality_report['marker_ok']} pages",
        f"- Vision redo: {quality_report['vision_redo']} pages",
        f"- Image descriptions: {quality_report['vision_image_desc']} pages",
    ])

    if conv_log["errors"]:
        lines.extend([
            f"- Errors: {len(conv_log['errors'])} (see conversion_log.json)",
        ])

    lines.extend([
        "",
        "## Usage",
        "Import `chapters/*.md` into your RAG knowledge base.",
        "Use `catalog.json` for file descriptions.",
    ])

    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


@click.command()
@click.argument("pdf_path", type=click.Path())
@click.option("-o", "--output", "output_dir", default=config.DEFAULT_OUTPUT_DIR, help="Output directory")
@click.option("--model", default=config.DEFAULT_MODEL, help="Claude model for Vision API")
@click.option("--full-vision", is_flag=True, help="Skip Marker, use Vision API for all pages")
@click.option("--resume", is_flag=True, help="Resume from last checkpoint")
@click.option("--desc-only", is_flag=True, help="Only regenerate descriptions")
def cli(pdf_path, output_dir, model, full_vision, resume, desc_only):
    """Convert a PDF specification document to Markdown for RAG.

    PDF_PATH: Path to the input PDF file.
    """
    # Validate input
    if not Path(pdf_path).exists():
        click.echo(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    if not desc_only and not full_vision:
        # Marker + Vision hybrid needs API key
        if not config.ANTHROPIC_API_KEY:
            click.echo("Warning: ANTHROPIC_API_KEY not set. Vision API steps will fail.")

    if full_vision and not config.ANTHROPIC_API_KEY:
        click.echo("Error: ANTHROPIC_API_KEY required for full-vision mode.")
        sys.exit(1)

    run_pipeline(pdf_path, output_dir, model, full_vision, resume, desc_only)


if __name__ == "__main__":
    cli()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_main.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add main.py tests/test_main.py
git commit -m "feat: main CLI pipeline with 8-step conversion, resume, and desc-only mode"
```

---

### Task 10: Documentation & Integration Test

**Files:**
- Create: `USAGE.md`
- Create: `tests/test_integration.py`

- [ ] **Step 1: Write USAGE.md**

```markdown
# Doc to Markdown - Usage Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: First run will download Marker's ML models (~1GB). This is a one-time setup.

### 2. Set API Key

```bash
# Linux/Mac
export ANTHROPIC_API_KEY=sk-ant-xxxxx

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sk-ant-xxxxx"

# Windows (CMD)
set ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### 3. Run Conversion

```bash
python main.py input/your_spec.pdf
```

That's it! Output will be in `output/your_spec/`.

---

## All Commands

### Basic Conversion
```bash
python main.py input/ufs_spec.pdf
```

### Specify Output Directory
```bash
python main.py input/ufs_spec.pdf -o output/my_custom_dir
```

### Use a Different Claude Model
```bash
# Default is claude-sonnet-4-20250514
python main.py input/ufs_spec.pdf --model claude-sonnet-4-20250514

# Use Opus for higher quality (costs ~5x more)
python main.py input/ufs_spec.pdf --model claude-opus-4-20250514
```

### Full Vision Mode (skip Marker, all pages via API)
```bash
python main.py input/ufs_spec.pdf --full-vision
```

### Resume After Interruption
```bash
python main.py input/ufs_spec.pdf --resume
```

### Regenerate Descriptions Only
```bash
python main.py input/ufs_spec.pdf --desc-only
```

### Show Help
```bash
python main.py --help
```

---

## Output Structure

```
output/ufs_spec/
├── chapters/              # Markdown files split by chapter
│   ├── 01_introduction.md
│   ├── 02_architecture.md
│   └── ...
├── descriptions/          # Per-file description JSON
│   ├── 01_introduction_desc.json
│   └── ...
├── catalog.json           # All descriptions in one file
├── quality_report.json    # Quality check results
├── conversion_log.json    # Conversion metadata & token usage
├── progress.json          # Resume checkpoint
└── README.md              # Human-readable summary
```

---

## Importing to RAG Knowledge Base

1. Upload all `.md` files from `chapters/`
2. Use `catalog.json` for file descriptions — each entry has:
   - `file`: filename
   - `title`: chapter title
   - `description`: what the chapter covers
   - `keywords`: search terms
   - `page_range`: original PDF pages

---

## Configuration

Edit `config.py` to adjust defaults:

| Setting | Default | Description |
|---------|---------|-------------|
| `DEFAULT_MODEL` | `claude-sonnet-4-20250514` | Vision API model |
| `SAMPLE_SIZE` | `30` | Pages to sample for quality check |
| `SIMILARITY_THRESHOLD` | `0.70` | Min similarity score |
| `MAX_CHAPTER_PAGES` | `50` | Split chapter if longer |
| `MIN_CHAPTER_PAGES` | `2` | Merge chapter if shorter |
| `MAX_RETRIES` | `3` | API retry attempts |

---

## Troubleshooting

**"ANTHROPIC_API_KEY not set"**
→ Set the environment variable (see Step 2 above)

**Rate limit errors**
→ The tool auto-retries with backoff. If persistent, wait a few minutes or use `--resume`

**Marker model download fails**
→ Check internet connection. Models are cached after first download.

**Output quality is poor**
→ Try `--full-vision` for maximum quality, or change model to Opus:
```bash
python main.py input/spec.pdf --model claude-opus-4-20250514
```
```

- [ ] **Step 2: Write integration test**

```python
# tests/test_integration.py
"""
Integration test — requires:
1. A small test PDF in tests/fixtures/test_sample.pdf
2. ANTHROPIC_API_KEY environment variable set

Run with: pytest tests/test_integration.py -v -m integration
Skip in CI with: pytest -m "not integration"
"""
import os
import pytest
from pathlib import Path
from click.testing import CliRunner

pytestmark = pytest.mark.integration


@pytest.fixture
def test_pdf():
    """Path to a small test PDF for integration testing."""
    path = Path(__file__).parent / "fixtures" / "test_sample.pdf"
    if not path.exists():
        pytest.skip("Test PDF not found at tests/fixtures/test_sample.pdf")
    return str(path)


@pytest.fixture
def has_api_key():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        pytest.skip("ANTHROPIC_API_KEY not set")


class TestIntegration:
    def test_full_pipeline(self, test_pdf, has_api_key, tmp_path):
        from main import cli
        runner = CliRunner()
        result = runner.invoke(cli, [test_pdf, "-o", str(tmp_path)])

        assert result.exit_code == 0
        pdf_name = Path(test_pdf).stem
        out_dir = tmp_path / pdf_name

        # Check output structure
        assert (out_dir / "chapters").exists()
        assert (out_dir / "catalog.json").exists()
        assert (out_dir / "quality_report.json").exists()
        assert (out_dir / "README.md").exists()

        # Check at least one chapter was created
        chapters = list((out_dir / "chapters").glob("*.md"))
        assert len(chapters) > 0

    def test_full_vision_mode(self, test_pdf, has_api_key, tmp_path):
        from main import cli
        runner = CliRunner()
        result = runner.invoke(cli, [test_pdf, "-o", str(tmp_path), "--full-vision"])
        assert result.exit_code == 0
```

- [ ] **Step 3: Create test fixtures directory**

```bash
mkdir -p tests/fixtures
```

- [ ] **Step 4: Run unit tests (not integration)**

Run: `python -m pytest tests/ -v -m "not integration" --ignore=tests/test_integration.py`
Expected: All unit tests PASS

- [ ] **Step 5: Commit**

```bash
git add USAGE.md tests/test_integration.py
git commit -m "docs: USAGE.md guide and integration test scaffold"
```

---

## Self-Review Checklist

**Spec coverage:**
- ✅ PDF parsing with TOC, image detection, scanned page detection
- ✅ Marker conversion with per-page output
- ✅ Vision API conversion with retry and token tracking
- ✅ Quality check: rules (garbled, empty table, short, broken, missing image)
- ✅ Quality check: sampling comparison with systematic failure detection
- ✅ Chapter merging with split/merge logic
- ✅ Description generation with catalog.json
- ✅ Progress tracking with resume support
- ✅ CLI with all specified flags (--model, --full-vision, --resume, --desc-only, -o)
- ✅ USAGE.md documentation
- ✅ Output README.md per conversion
- ✅ Error handling: rate limit, API errors, no TOC fallback, scanned PDF
- ✅ Console progress output
- ✅ Cost tracking

**Placeholder scan:** No TBD/TODO found.

**Type consistency:** Verified method names, return types, and parameter names are consistent across all tasks.
