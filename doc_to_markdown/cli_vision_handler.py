"""CLI mode handler: prepare tasks for the current Claude Code session.

CLI mode skips all Vision/LLM API calls. Instead the pipeline:
1. Renders pages needing vision work to PNG under `pages_for_vision/`.
2. Writes `need_vision.json` describing what Claude should do.
3. Exits so the current Claude Code CLI session can pick up each task,
   Read the PNG with its multimodal vision, and Write markdown back
   to `marker_cache/page_XXXX.md` (or `descriptions/*.json`).
4. Re-running with `--resume` continues from the merge step, loading
   the Claude-written markdown from `marker_cache/`.

Used when `--mode cli` (the default) is active.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def prepare_vision_tasks(
    pdf_info: Any,
    needs_redo: list[dict],
    needs_vision_desc: list[dict],
    out_dir: Path,
    dpi: int = 200,
) -> dict:
    """Render PNGs and write a task manifest for Claude to process.

    Parameters
    ----------
    pdf_info:
        A ``PdfInfo`` instance providing ``render_page(page_num, dpi)``.
    needs_redo:
        List of ``{"page": int, "reason": str}`` - pages to fully reconvert.
    needs_vision_desc:
        List of ``{"page": int, "reason": str}`` - pages needing an
        image description appended (marker markdown already exists).
    out_dir:
        Output directory for this PDF (e.g. ``output/<pdf_name>/``).
    dpi:
        Rasterisation DPI (default 200 - good balance of detail vs size).

    Returns
    -------
    dict
        Summary: ``{"manifest_path": str, "pages_dir": str, "total_tasks": int}``.
    """
    pages_dir = out_dir / "pages_for_vision"
    pages_dir.mkdir(parents=True, exist_ok=True)

    marker_cache = out_dir / "marker_cache"
    marker_cache.mkdir(parents=True, exist_ok=True)

    redo_pages = sorted({r["page"] for r in needs_redo})
    desc_pages = sorted(
        {r["page"] for r in needs_vision_desc} - set(redo_pages)
    )

    tasks: list[dict[str, Any]] = []

    for p in redo_pages:
        png_path = pages_dir / f"page_{p:04d}.png"
        if not png_path.exists():
            img = pdf_info.render_page(p, dpi=dpi)
            img.save(str(png_path), format="PNG")
        reason = next(
            (r["reason"] for r in needs_redo if r["page"] == p),
            "",
        )
        tasks.append(
            {
                "page_0based": p,
                "page_1based": p + 1,
                "png": str(png_path.relative_to(out_dir)).replace("\\", "/"),
                "action": "convert_to_markdown",
                "output_md": f"marker_cache/page_{p:04d}.md",
                "reason": reason,
            }
        )

    for p in desc_pages:
        png_path = pages_dir / f"page_{p:04d}.png"
        if not png_path.exists():
            img = pdf_info.render_page(p, dpi=dpi)
            img.save(str(png_path), format="PNG")
        reason = next(
            (r["reason"] for r in needs_vision_desc if r["page"] == p),
            "",
        )
        tasks.append(
            {
                "page_0based": p,
                "page_1based": p + 1,
                "png": str(png_path.relative_to(out_dir)).replace("\\", "/"),
                "action": "append_image_description",
                "output_md": f"marker_cache/page_{p:04d}.md",
                "reason": reason,
            }
        )

    manifest = {
        "mode": "cli",
        "stage": "vision_redo",
        "total_tasks": len(tasks),
        "tasks": tasks,
        "instructions_for_claude": _vision_instructions(),
    }

    manifest_path = out_dir / "need_vision.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return {
        "manifest_path": str(manifest_path),
        "pages_dir": str(pages_dir),
        "total_tasks": len(tasks),
    }


def _vision_instructions() -> str:
    return (
        "For each task in `tasks`:\n"
        "  1. Read the PNG at `png` (relative to this output directory).\n"
        "  2. If action == 'convert_to_markdown': produce high-fidelity Markdown\n"
        "     preserving headings, text, ALL tables (use | syntax), and\n"
        "     describing figures in [Figure: ...] brackets. Write to `output_md`.\n"
        "  3. If action == 'append_image_description': read any existing\n"
        "     markdown at `output_md`, append '\\n\\n[Image Description: <detailed "
        "technical description of every diagram/figure on the page>]', write back.\n"
        "When every task has its `output_md` populated, run:\n"
        "  python -m doc_to_markdown.main <pdf> --resume --mode cli\n"
    )


def check_vision_tasks_complete(out_dir: Path) -> tuple[bool, list[int]]:
    """Verify every task in ``need_vision.json`` has a non-empty output file.

    Returns
    -------
    (complete, missing_pages)
        ``complete=True`` only when a manifest exists AND every task's
        ``output_md`` exists and is non-empty. If no manifest yet,
        returns ``(False, [])`` so the caller triggers preparation.
    """
    manifest_path = out_dir / "need_vision.json"
    if not manifest_path.exists():
        return False, []

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing: list[int] = []
    for task in manifest.get("tasks", []):
        out_md = out_dir / task["output_md"]
        if not out_md.exists() or out_md.stat().st_size == 0:
            missing.append(task["page_0based"])
    return len(missing) == 0, sorted(missing)


def prepare_desc_tasks(
    chapter_files: list[dict],
    out_dir: Path,
) -> dict:
    """Write ``need_desc.json`` describing per-chapter description tasks."""
    descriptions_dir = out_dir / "descriptions"
    descriptions_dir.mkdir(parents=True, exist_ok=True)

    tasks: list[dict[str, Any]] = []
    for ci in chapter_files:
        fname = ci["filename"]
        stem = Path(fname).stem
        tasks.append(
            {
                "chapter_file": f"chapters/{fname}",
                "title": ci["title"],
                "page_range": ci["page_range"],
                "output_json": f"descriptions/{stem}.json",
            }
        )

    manifest = {
        "mode": "cli",
        "stage": "descriptions",
        "total_tasks": len(tasks),
        "tasks": tasks,
        "instructions_for_claude": _desc_instructions(),
    }

    manifest_path = out_dir / "need_desc.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return {
        "manifest_path": str(manifest_path),
        "total_tasks": len(tasks),
    }


def _desc_instructions() -> str:
    return (
        "For each task in `tasks`:\n"
        "  1. Read `chapter_file` (Markdown, may be long - use offset/limit if needed).\n"
        "  2. Write `output_json` with exact schema:\n"
        '     {"file": "<filename.md>", "title": "<title>",\n'
        '      "description": "<2-3 Traditional Chinese sentences summarising '
        "what this chapter covers and what RAG questions it can answer>\",\n"
        '      "keywords": ["<eng keyword 1>", "<eng keyword 2>", ...],\n'
        '      "page_range": "<N-M>"}\n'
        "  3. Keep keywords 3-6 items, English, lowercased, domain-specific\n"
        "     (e.g. SCSI opcodes, protocol names, data structures).\n"
        "When all tasks done, run:\n"
        "  python -m doc_to_markdown.main <pdf> --resume --mode cli --desc-only\n"
    )


def check_desc_tasks_complete(
    out_dir: Path,
) -> tuple[bool, list[str]]:
    """Verify every task in ``need_desc.json`` has a corresponding JSON.

    Returns ``(False, [])`` when no manifest exists yet so the caller
    will trigger preparation on the first pass.
    """
    manifest_path = out_dir / "need_desc.json"
    if not manifest_path.exists():
        return False, []

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing: list[str] = []
    for task in manifest.get("tasks", []):
        out_json = out_dir / task["output_json"]
        if not out_json.exists() or out_json.stat().st_size == 0:
            missing.append(task["output_json"])
    return len(missing) == 0, sorted(missing)


def load_desc_results(
    descriptions_dir: Path,
    chapter_files: list[dict],
) -> list[dict]:
    """Load Claude-written description JSONs in the same order as chapters."""
    results: list[dict] = []
    for ci in chapter_files:
        stem = Path(ci["filename"]).stem
        json_path = descriptions_dir / f"{stem}.json"
        if json_path.exists():
            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
                data.setdefault("file", ci["filename"])
                data.setdefault("title", ci["title"])
                data.setdefault("page_range", ci["page_range"])
                data.setdefault("keywords", [])
                data.setdefault("description", "")
                results.append(data)
            except Exception:
                results.append(
                    {
                        "file": ci["filename"],
                        "title": ci["title"],
                        "page_range": ci["page_range"],
                        "description": "",
                        "keywords": [],
                    }
                )
        else:
            results.append(
                {
                    "file": ci["filename"],
                    "title": ci["title"],
                    "page_range": ci["page_range"],
                    "description": "",
                    "keywords": [],
                }
            )
    return results
