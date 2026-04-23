"""Direct-text extractor for digitally-generated PDFs.

This is the cheap "Layer 1" used by `--text-first` mode. Instead of running
Marker (slow, VRAM-heavy) or full vision (expensive), it extracts the
embedded text layer with PyMuPDF and cleans it into usable Markdown.

When a page is text-only (no real figures, no broken tables), the result
is good enough for RAG use. Pages that genuinely need vision (diagrams,
raster images, complex multi-column tables) are flagged for the existing
vision reinforcement step.

For PDFs without an embedded text layer (scanned), this module still
returns empty content for those pages and the classifier flags them.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Optional

import fitz  # PyMuPDF


@dataclass
class PageClassification:
    page: int
    text_len: int
    n_drawings: int
    n_raster_images: int
    n_tables: int
    strategy: str  # "text" | "vision" | "hybrid"
    reason: str


def extract_all_pages(
    pdf_path: str,
    figure_drawing_threshold: int = 30,
    short_text_threshold: int = 50,
) -> tuple[dict[int, str], list[PageClassification]]:
    """Extract text + classify every page of a PDF.

    Returns
    -------
    (texts, classifications)
        ``texts[page_idx]`` is clean Markdown for pages classified as
        ``"text"``. Pages classified as ``"vision"`` get an empty string
        so the existing vision step can take over. ``"hybrid"`` pages
        get text PLUS a flag so vision can append figure descriptions.
    """
    doc = fitz.open(pdf_path)
    total = doc.page_count

    # First pass: collect top/bottom lines per page for boilerplate detection.
    # Scan top-3 and bottom-3 lines to catch multi-line running header/footer.
    header_candidates: list[str] = []
    footer_candidates: list[str] = []
    page_raw_lines: list[list[str]] = []

    for i in range(total):
        lines = _get_page_lines(doc[i])
        page_raw_lines.append(lines)
        non_empty = [ln.strip() for ln in lines if ln.strip()]
        header_candidates.extend(non_empty[:3])
        footer_candidates.extend(non_empty[-3:])

    boilerplate = _detect_boilerplate(header_candidates, footer_candidates, total)

    # Second pass: classify + clean
    texts: dict[int, str] = {}
    classifications: list[PageClassification] = []

    for i in range(total):
        page = doc[i]
        lines = page_raw_lines[i]
        drawings = page.get_drawings()
        images = page.get_images()

        raw_text = "\n".join(lines)
        clean = _clean_text(raw_text, boilerplate)

        text_len = len(clean.strip())
        n_draw = len(drawings)
        n_img = len(images)

        # pdfplumber-style quick table hint (optional) - skip for speed;
        # instead rely on drawings count as a proxy.
        n_tables = 0  # filled below if needed

        strategy, reason = _classify(
            text_len=text_len,
            n_drawings=n_draw,
            n_raster_images=n_img,
            figure_threshold=figure_drawing_threshold,
            short_threshold=short_text_threshold,
        )

        if strategy == "text" or strategy == "hybrid":
            texts[i] = clean
        else:
            texts[i] = ""  # vision will fill this in

        classifications.append(
            PageClassification(
                page=i,
                text_len=text_len,
                n_drawings=n_draw,
                n_raster_images=n_img,
                n_tables=n_tables,
                strategy=strategy,
                reason=reason,
            )
        )

    doc.close()
    return texts, classifications


def _get_page_lines(page: fitz.Page) -> list[str]:
    """Extract text as a list of lines in reading order."""
    raw = page.get_text("text")
    return [ln.rstrip() for ln in raw.splitlines()]


def _detect_boilerplate(
    headers: list[str],
    footers: list[str],
    total_pages: int,
    freq_threshold: float = 0.30,
) -> set[str]:
    """Identify lines repeated on 30%+ of pages (running headers/footers)."""
    if total_pages == 0:
        return set()

    head_counts = Counter(h for h in headers if h)
    foot_counts = Counter(f for f in footers if f)

    limit = max(1, int(total_pages * freq_threshold))
    boiler = set()
    for line, cnt in head_counts.items():
        if cnt >= limit:
            boiler.add(line)
    for line, cnt in foot_counts.items():
        if cnt >= limit:
            boiler.add(line)
    return boiler


_BOILER_SUBSTRS = (
    # Common page-level decoration substrings that appear inline
    "Working Draft",
)


def _clean_text(raw: str, boilerplate: set[str]) -> str:
    """Strip boilerplate lines, page numbers, and excessive blank lines."""
    out_lines: list[str] = []
    for ln in raw.splitlines():
        s = ln.strip()
        if not s:
            out_lines.append("")
            continue
        if s in boilerplate:
            continue
        # standalone page numbers like "29", "150"
        if re.fullmatch(r"\d{1,4}", s):
            continue
        # PDF timestamp watermark like "晨丹辰2022/ 10/ 06 10:02"
        if re.search(r"\d{4}/\s*\d{1,2}/\s*\d{1,2}", s) and len(s) < 40:
            continue
        out_lines.append(ln)

    # collapse >2 consecutive blank lines
    result: list[str] = []
    blank_run = 0
    for ln in out_lines:
        if not ln.strip():
            blank_run += 1
            if blank_run <= 1:
                result.append("")
        else:
            blank_run = 0
            result.append(ln)

    return "\n".join(result).strip() + "\n"


def _classify(
    text_len: int,
    n_drawings: int,
    n_raster_images: int,
    figure_threshold: int,
    short_threshold: int,
) -> tuple[str, str]:
    """Decide per-page extraction strategy."""
    if n_raster_images > 0:
        return "vision", f"has_raster_image({n_raster_images})"
    if text_len < short_threshold and n_drawings > 3:
        return "vision", f"short_text({text_len})+drawings({n_drawings})"
    if n_drawings >= figure_threshold:
        return "hybrid", f"many_drawings({n_drawings})"
    return "text", f"text_only(chars={text_len},drawings={n_drawings})"


def save_classifications_report(
    classifications: list[PageClassification],
    out_path,
) -> dict:
    """Write a JSON report with per-page strategy and summary counts."""
    import json
    from pathlib import Path

    out_path = Path(out_path)
    pages = [
        {
            "page": c.page,
            "text_len": c.text_len,
            "n_drawings": c.n_drawings,
            "n_raster_images": c.n_raster_images,
            "strategy": c.strategy,
            "reason": c.reason,
        }
        for c in classifications
    ]
    counts: dict[str, int] = {}
    for c in classifications:
        counts[c.strategy] = counts.get(c.strategy, 0) + 1

    report = {
        "total_pages": len(classifications),
        "strategy_counts": counts,
        "pages": pages,
    }
    out_path.write_text(
        __import__("json").dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return report
