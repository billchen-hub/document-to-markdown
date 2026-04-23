"""Scan a PDF and classify each page by extraction strategy.

Classifies each page as one of:
  - "text_only"     : pure paragraph text, no drawings, no tables - direct extract
  - "has_table"     : pdfplumber detected a structured table - try table extract, maybe vision fallback
  - "has_figure"    : many vector drawings (likely a diagram) - vision needed
  - "mixed"         : drawings + tables + text - vision safer

Outputs JSON report so we know the real vision workload before committing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz  # PyMuPDF
import pdfplumber


def classify_page(fitz_page, plumber_page) -> dict:
    text = fitz_page.get_text()
    text_len = len(text.strip())
    drawings = fitz_page.get_drawings()
    n_drawings = len(drawings)
    images = fitz_page.get_images()
    n_images = len(images)

    try:
        tables = plumber_page.find_tables()
        n_tables = len(tables)
    except Exception:
        n_tables = 0

    # Heuristic classifier
    if n_images > 0:
        category = "has_raster_image"
    elif n_drawings >= 30 and n_tables == 0:
        category = "has_figure"
    elif n_tables >= 1 and n_drawings >= 10:
        category = "has_table"
    elif n_tables >= 1:
        category = "has_simple_table"
    elif n_drawings >= 10:
        category = "has_light_drawing"  # maybe header separator lines, maybe small figure
    elif text_len < 50:
        category = "near_empty"
    else:
        category = "text_only"

    return {
        "text_len": text_len,
        "n_drawings": n_drawings,
        "n_images": n_images,
        "n_tables": n_tables,
        "category": category,
    }


def scan(pdf_path: Path, out_path: Path) -> dict:
    results = []

    with fitz.open(str(pdf_path)) as doc, pdfplumber.open(str(pdf_path)) as plumber:
        total = doc.page_count
        for i in range(total):
            info = classify_page(doc[i], plumber.pages[i])
            info["page"] = i
            results.append(info)
            if i % 50 == 0:
                print(f"  scanned {i}/{total}")

    # Summarize
    counts: dict[str, int] = {}
    for r in results:
        counts[r["category"]] = counts.get(r["category"], 0) + 1

    report = {
        "pdf": str(pdf_path),
        "total_pages": len(results),
        "category_counts": counts,
        "pages": results,
    }
    out_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\n=== SUMMARY ===")
    print(f"Total pages: {len(results)}")
    for cat, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        pct = 100.0 * n / len(results)
        print(f"  {cat:<20} {n:>4} ({pct:5.1f}%)")

    vision_needed = sum(
        counts.get(c, 0)
        for c in ["has_figure", "has_table", "has_raster_image", "mixed"]
    )
    pct = 100.0 * vision_needed / len(results)
    print(f"\n=> Pages likely needing CLI vision: {vision_needed} ({pct:.1f}%)")
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=None)
    args = ap.parse_args()

    out = args.out or (
        args.pdf.parent.parent
        / "output"
        / args.pdf.stem
        / "layout_scan.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)

    scan(args.pdf, out)


if __name__ == "__main__":
    main()
