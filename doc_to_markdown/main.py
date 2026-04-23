"""CLI entry point and 8-step pipeline orchestrator for Doc to Markdown."""
from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

import click

from doc_to_markdown.config import (
    ANTHROPIC_API_KEY,
    CONVERSION_MODE,
    DEFAULT_VISION_MODEL,
    OUTPUT_DIR,
    STEPS,
)


def _print_step(step_num: int, total: int, msg: str, end: str = "\n"):
    """Print a formatted pipeline step message."""
    click.echo(f"[Step {step_num}/{total}] {msg}", nl=(end == "\n"))


def _load_progress(progress_path: Path) -> dict:
    """Load progress.json if it exists."""
    if progress_path.exists():
        return json.loads(progress_path.read_text(encoding="utf-8"))
    return {}


def _save_progress(progress_path: Path, progress: dict):
    """Save progress.json atomically."""
    tmp = progress_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(progress_path)


def _check_disk_space(path: Path, min_mb: int = 100) -> bool:
    """Check if there's enough disk space."""
    usage = shutil.disk_usage(str(path))
    free_mb = usage.free / (1024 * 1024)
    if free_mb < min_mb:
        click.echo(f"ERROR: Only {free_mb:.0f}MB free disk space, need at least {min_mb}MB.")
        return False
    return True


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
@click.option("-o", "--output", "output_dir", default=None, help="Output directory")
@click.option(
    "--mode",
    type=click.Choice(["cli", "api"]),
    default=None,
    help=(
        "Conversion mode. 'cli' (default): no API calls; this Claude Code "
        "session reads rendered PNGs. 'api': call a Vision/LLM API for "
        "redos and descriptions."
    ),
)
@click.option("--model", default=None, help=f"Vision API model (default: {DEFAULT_VISION_MODEL})")
@click.option("--full-vision", is_flag=True, help="Skip Marker, use Vision API for all pages (api mode only)")
@click.option(
    "--text-first",
    is_flag=True,
    help=(
        "Skip Marker and Vision. Extract the embedded text layer directly "
        "with PyMuPDF. Best for native-digital technical PDFs where text "
        "accuracy matters more than perfect table formatting."
    ),
)
@click.option("--resume", "do_resume", is_flag=True, help="Resume from last checkpoint")
@click.option("--desc-only", is_flag=True, help="Only regenerate descriptions")
def main(
    pdf_path: str,
    output_dir: str | None,
    mode: str | None,
    model: str | None,
    full_vision: bool,
    text_first: bool,
    do_resume: bool,
    desc_only: bool,
):
    """Convert a PDF specification to Markdown files for RAG.

    PDF_PATH is the path to the PDF file to convert.
    """
    # Resolve effective mode: CLI flag > env var > default "cli"
    effective_mode = mode or CONVERSION_MODE or "cli"
    if effective_mode not in ("cli", "api"):
        click.echo(f"ERROR: invalid --mode '{effective_mode}', use 'cli' or 'api'.")
        sys.exit(1)

    if full_vision and text_first:
        click.echo("ERROR: --full-vision and --text-first are mutually exclusive.")
        sys.exit(1)

    if full_vision and effective_mode == "cli":
        click.echo(
            "NOTE: --full-vision with --mode cli means every page will be "
            "handed to this Claude Code session."
        )

    if text_first:
        click.echo(
            "NOTE: --text-first mode: extracting embedded text directly with "
            "PyMuPDF. Marker and Vision are skipped."
        )
    pdf_path_obj = Path(pdf_path)
    pdf_name = pdf_path_obj.stem

    # Resolve output directory
    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = OUTPUT_DIR / pdf_name
    out_dir.mkdir(parents=True, exist_ok=True)

    chapters_dir = out_dir / "chapters"
    images_dir = out_dir / "images"
    descriptions_dir = out_dir / "descriptions"
    for d in [chapters_dir, images_dir, descriptions_dir]:
        d.mkdir(parents=True, exist_ok=True)

    progress_path = out_dir / "progress.json"
    log_path = out_dir / "conversion_log.json"
    quality_report_path = out_dir / "quality_report.json"

    # Check disk space
    if not _check_disk_space(out_dir):
        sys.exit(1)

    # Load or initialize progress
    progress = {}
    if do_resume:
        progress = _load_progress(progress_path)
        if progress:
            click.echo(f"Resuming from step: {progress.get('current_step', 'unknown')}")
        else:
            click.echo("No progress file found. Starting fresh.")
    elif progress_path.exists() and not desc_only:
        click.echo("Existing progress.json found. Use --resume to continue, or delete it to restart.")
        if not click.confirm("Start fresh?"):
            sys.exit(0)

    if not progress:
        progress = {
            "status": "in_progress",
            "current_step": STEPS[0],
            "pages": {},
            "stats": {
                "marker_completed": 0,
                "quality_checked": 0,
                "vision_total": 0,
                "vision_completed": 0,
                "vision_pending": 0,
            },
        }

    conversion_log = []
    total_steps = 8

    # ---------------------------------------------------------------
    # Step 1: PDF Parse
    # ---------------------------------------------------------------
    if not desc_only and _should_run_step(progress, "pdf_parse"):
        _print_step(1, total_steps, "PDF parsing...")

        from doc_to_markdown.pdf_parser import PdfInfo

        pdf_info = PdfInfo(str(pdf_path_obj))

        if pdf_info.is_encrypted():
            click.echo("ERROR: PDF is encrypted. Please provide an unencrypted file.")
            sys.exit(1)

        chapters = pdf_info.get_chapters()
        page_count = pdf_info.page_count

        # Categorize pages (has images, has tables, scan-only)
        page_categories = {}
        for p in range(page_count):
            has_images = len(pdf_info.get_page_image_regions(p)) > 0
            has_tables = pdf_info.page_has_tables(p)
            has_text = pdf_info.has_text_layer(p)
            page_categories[p] = {
                "has_images": has_images,
                "has_tables": has_tables,
                "has_text": has_text,
                "scan_only": not has_text,
            }

        progress["chapters"] = chapters
        progress["page_count"] = page_count
        progress["page_categories"] = page_categories
        progress["current_step"] = "marker_convert"
        _save_progress(progress_path, progress)

        scan_only = sum(1 for v in page_categories.values() if v["scan_only"])
        _print_step(
            1, total_steps,
            f"PDF parsing: {page_count} pages, {len(chapters)} chapters detected "
            f"({scan_only} scan-only pages) [OK]"
        )
    else:
        # Load from progress
        from doc_to_markdown.pdf_parser import PdfInfo
        pdf_info = PdfInfo(str(pdf_path_obj))
        chapters = progress.get("chapters", pdf_info.get_chapters())
        page_count = progress.get("page_count", pdf_info.page_count)
        page_categories = progress.get("page_categories", {})
        # Ensure keys are ints
        page_categories = {int(k): v for k, v in page_categories.items()}

    # ---------------------------------------------------------------
    # Step 2: Marker Conversion
    # ---------------------------------------------------------------
    marker_results: dict[int, str] = {}

    if not desc_only and _should_run_step(progress, "marker_convert"):
        if text_first:
            _print_step(2, total_steps, "Text-first extraction: starting...")

            from doc_to_markdown.text_extractor import (
                extract_all_pages,
                save_classifications_report,
            )

            texts, classifications = extract_all_pages(str(pdf_path_obj))

            marker_cache_dir = out_dir / "marker_cache"
            marker_cache_dir.mkdir(exist_ok=True)
            for p, md in texts.items():
                marker_results[p] = md
                (marker_cache_dir / f"page_{p:04d}.md").write_text(md, encoding="utf-8")

            save_classifications_report(
                classifications, out_dir / "text_extraction_report.json"
            )

            # Track which pages still need vision (hybrid/vision strategy)
            progress["text_first_classifications"] = [
                {"page": c.page, "strategy": c.strategy, "reason": c.reason}
                for c in classifications
            ]

            from collections import Counter
            counts = Counter(c.strategy for c in classifications)
            for p, md in texts.items():
                key = str(p)
                if key not in progress["pages"]:
                    progress["pages"][key] = {}
                progress["pages"][key]["text_first"] = "done"
            progress["stats"]["marker_completed"] = len(texts)
            progress["current_step"] = "quality_rules"
            _save_progress(progress_path, progress)

            _print_step(
                2, total_steps,
                f"Text-first extraction: {len(texts)}/{page_count} pages "
                f"(text={counts.get('text',0)}, hybrid={counts.get('hybrid',0)}, "
                f"vision={counts.get('vision',0)}) [OK]"
            )
        elif full_vision:
            _print_step(2, total_steps, "Marker conversion: SKIPPED (--full-vision mode) [OK]")
            progress["current_step"] = "quality_rules"
            _save_progress(progress_path, progress)
        else:
            _print_step(2, total_steps, "Marker conversion: starting...")

            from doc_to_markdown.marker_converter import MarkerConverter
            marker = MarkerConverter()

            def marker_progress(current, total):
                click.echo(f"\r[Step 2/{total_steps}] Marker conversion: {current}/{total} pages...", nl=False)

            marker_results = marker.convert_all(str(pdf_path_obj), progress_callback=marker_progress)

            # Save per-page results in progress
            for p, md in marker_results.items():
                key = str(p)
                if key not in progress["pages"]:
                    progress["pages"][key] = {}
                progress["pages"][key]["marker"] = "done"

            progress["stats"]["marker_completed"] = len(marker_results)
            progress["current_step"] = "quality_rules"
            _save_progress(progress_path, progress)

            # Save intermediate markdown files
            marker_cache_dir = out_dir / "marker_cache"
            marker_cache_dir.mkdir(exist_ok=True)
            for p, md in marker_results.items():
                (marker_cache_dir / f"page_{p:04d}.md").write_text(md, encoding="utf-8")

            click.echo(f"\r[Step 2/{total_steps}] Marker conversion: {len(marker_results)}/{page_count} pages [OK]")
    else:
        # Load cached marker results
        marker_cache_dir = out_dir / "marker_cache"
        if marker_cache_dir.exists():
            for f in sorted(marker_cache_dir.glob("page_*.md")):
                page_num = int(f.stem.split("_")[1])
                marker_results[page_num] = f.read_text(encoding="utf-8")

    # ---------------------------------------------------------------
    # Step 3: Quality Check - Rules
    # ---------------------------------------------------------------
    needs_redo: list[dict] = []
    needs_vision_desc: list[dict] = []

    if not desc_only and _should_run_step(progress, "quality_rules"):
        _print_step(3, total_steps, "Quality check (rules)...")

        from doc_to_markdown.quality_checker import QualityChecker
        checker = QualityChecker()

        quality_report = checker.check_all_pages(marker_results, pdf_info)
        needs_redo = quality_report["needs_redo"]
        needs_vision_desc = quality_report["needs_vision_describe"]

        # Mark scan-only pages for Vision redo
        for p, cat in page_categories.items():
            if cat.get("scan_only") and p not in [r["page"] for r in needs_redo]:
                needs_redo.append({"page": p, "reason": "scan_only"})

        # If full-vision, all pages need Vision
        if full_vision:
            needs_redo = [{"page": p, "reason": "full_vision"} for p in range(page_count)]
            needs_vision_desc = []

        progress["needs_redo"] = needs_redo
        progress["needs_vision_desc"] = needs_vision_desc
        progress["current_step"] = "quality_sampling"
        _save_progress(progress_path, progress)

        # Save quality report
        quality_report_path.write_text(
            json.dumps(quality_report, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        _print_step(
            3, total_steps,
            f"Quality check (rules): {page_count} pages scanned [OK]\n"
            f"           -> {len(needs_redo)} pages need redo, "
            f"{len(needs_vision_desc)} need image description"
        )
    else:
        needs_redo = progress.get("needs_redo", [])
        needs_vision_desc = progress.get("needs_vision_desc", [])

    # ---------------------------------------------------------------
    # Step 4: Quality Check - Sampling (API mode only)
    # ---------------------------------------------------------------
    if (
        not desc_only
        and not full_vision
        and effective_mode == "api"
        and _should_run_step(progress, "quality_sampling")
    ):
        _print_step(4, total_steps, "Quality check (sampling)...")

        from doc_to_markdown.quality_checker import QualityChecker
        from doc_to_markdown.vision_converter import VisionConverter

        if "checker" not in dir():
            checker = QualityChecker()

        vision = VisionConverter(model=model)

        sampling_result = checker.sample_and_compare(
            pdf_info, marker_results, vision
        )

        # Add newly flagged pages
        already_flagged = {r["page"] for r in needs_redo}
        new_flags = 0
        for p in sampling_result.get("flagged_pages", []):
            if p not in already_flagged:
                needs_redo.append({"page": p, "reason": "sampling_fail"})
                new_flags += 1

        # Handle category-level redo
        cat_redo = sampling_result.get("category_redo", {})
        if cat_redo.get("table"):
            for p, cat in page_categories.items():
                if cat.get("has_tables") and p not in already_flagged:
                    needs_redo.append({"page": p, "reason": "table_category_redo"})
                    new_flags += 1
        if cat_redo.get("image"):
            for p, cat in page_categories.items():
                if cat.get("has_images") and p not in already_flagged:
                    needs_vision_desc.append({"page": p, "reason": "image_category_redo"})

        progress["needs_redo"] = needs_redo
        progress["needs_vision_desc"] = needs_vision_desc
        progress["current_step"] = "vision_redo"
        _save_progress(progress_path, progress)

        sampled = len(sampling_result.get("sampled", []))
        _print_step(
            4, total_steps,
            f"Quality check (sampling): {sampled} pages compared [OK]\n"
            f"           -> {new_flags} additional pages flagged"
        )
    elif not desc_only and full_vision:
        _print_step(4, total_steps, "Quality check (sampling): SKIPPED (--full-vision mode) [OK]")
        progress["current_step"] = "vision_redo"
        _save_progress(progress_path, progress)
    elif not desc_only and effective_mode == "cli" and _should_run_step(progress, "quality_sampling"):
        _print_step(
            4, total_steps,
            "Quality check (sampling): SKIPPED (cli mode - no API calls) [OK]",
        )
        progress["current_step"] = "vision_redo"
        _save_progress(progress_path, progress)

    # ---------------------------------------------------------------
    # Step 5: Vision Redo + Image Descriptions
    # ---------------------------------------------------------------
    if not desc_only and _should_run_step(progress, "vision_redo") and effective_mode == "cli":
        # CLI mode: render PNGs + write task manifest, then either load
        # Claude-written markdown (if complete) or exit for Claude to work.
        from doc_to_markdown.cli_vision_handler import (
            check_vision_tasks_complete,
            prepare_vision_tasks,
        )

        total_vision = len(needs_redo) + len(needs_vision_desc)

        if total_vision == 0:
            _print_step(5, total_steps, "Vision (cli): no pages need processing [OK]")
            progress["current_step"] = "merge"
            _save_progress(progress_path, progress)
        else:
            complete, missing = check_vision_tasks_complete(out_dir)

            if not complete:
                _print_step(
                    5, total_steps,
                    f"Vision (cli): preparing {total_vision} page tasks...",
                )
                summary = prepare_vision_tasks(
                    pdf_info, needs_redo, needs_vision_desc, out_dir
                )
                manifest_path = summary["manifest_path"]
                progress["stats"]["vision_total"] = total_vision
                progress["stats"]["vision_pending"] = len(missing) if missing else total_vision
                _save_progress(progress_path, progress)

                click.echo("")
                click.echo(
                    "=" * 70 + "\n"
                    f"CLI MODE: Pipeline paused at Step 5.\n"
                    f"  Manifest: {manifest_path}\n"
                    f"  Pages rendered to: {summary['pages_dir']}\n"
                    f"  Total tasks: {summary['total_tasks']}\n\n"
                    "Claude Code: please process each task in the manifest by reading\n"
                    "the PNG and writing the resulting markdown to the path in\n"
                    "`output_md`. When every task has its output_md populated,\n"
                    "re-run this command with --resume to continue.\n"
                    + "=" * 70
                )
                sys.exit(0)

            # All tasks complete - load Claude-written md from marker_cache
            _print_step(
                5, total_steps,
                f"Vision (cli): loading {total_vision} Claude-written pages...",
            )
            marker_cache_dir = out_dir / "marker_cache"
            for task_file in sorted(marker_cache_dir.glob("page_*.md")):
                try:
                    page_num = int(task_file.stem.split("_")[1])
                    marker_results[page_num] = task_file.read_text(encoding="utf-8")
                except (ValueError, OSError):
                    continue
            progress["stats"]["vision_total"] = total_vision
            progress["stats"]["vision_completed"] = total_vision
            progress["stats"]["vision_pending"] = 0
            progress["current_step"] = "merge"
            _save_progress(progress_path, progress)
            _print_step(5, total_steps, f"Vision (cli): {total_vision} pages loaded [OK]")

    elif not desc_only and _should_run_step(progress, "vision_redo"):
        # API mode (original logic)
        from doc_to_markdown.vision_converter import VisionConverter, RateLimitExhausted

        if "vision" not in dir():
            vision = VisionConverter(model=model)

        # Validate API key before expensive operations
        if needs_redo or needs_vision_desc:
            _print_step(5, total_steps, "Vision API: validating API key...")
            if not vision.validate_api_key():
                click.echo("ERROR: Invalid API key. Set it and use --resume.")
                progress["status"] = "paused"
                _save_progress(progress_path, progress)
                sys.exit(1)

        # Deduplicate redo pages
        redo_pages = list({r["page"] for r in needs_redo})
        desc_pages = list({r["page"] for r in needs_vision_desc} - set(redo_pages))

        total_vision = len(redo_pages) + len(desc_pages)
        progress["stats"]["vision_total"] = total_vision
        progress["stats"]["vision_pending"] = total_vision

        if total_vision == 0:
            _print_step(5, total_steps, "Vision API: no pages need processing [OK]")
        else:
            _print_step(5, total_steps, f"Vision API: {total_vision} pages to process...")

            completed = 0
            try:
                # Redo pages
                for p in redo_pages:
                    page_key = str(p)
                    if progress["pages"].get(page_key, {}).get("vision") == "done":
                        completed += 1
                        continue

                    img = pdf_info.render_page(p)
                    md = vision.convert_page(img, p + 1)
                    marker_results[p] = md

                    # Save to cache
                    marker_cache_dir = out_dir / "marker_cache"
                    marker_cache_dir.mkdir(exist_ok=True)
                    (marker_cache_dir / f"page_{p:04d}.md").write_text(md, encoding="utf-8")

                    if page_key not in progress["pages"]:
                        progress["pages"][page_key] = {}
                    progress["pages"][page_key]["vision"] = "done"
                    completed += 1
                    progress["stats"]["vision_completed"] = completed
                    progress["stats"]["vision_pending"] = total_vision - completed
                    _save_progress(progress_path, progress)

                    click.echo(
                        f"\r[Step 5/{total_steps}] Vision API: {completed}/{total_vision} pages...",
                        nl=False,
                    )

                # Image description pages (not already redone)
                for p in desc_pages:
                    page_key = str(p)
                    if progress["pages"].get(page_key, {}).get("vision") == "done":
                        completed += 1
                        continue

                    img = pdf_info.render_page(p)
                    description = vision.describe_image(img)

                    # Append image description to existing markdown
                    existing = marker_results.get(p, "")
                    marker_results[p] = existing + f"\n\n[Image Description: {description}]"

                    # Save
                    marker_cache_dir = out_dir / "marker_cache"
                    (marker_cache_dir / f"page_{p:04d}.md").write_text(
                        marker_results[p], encoding="utf-8"
                    )

                    if page_key not in progress["pages"]:
                        progress["pages"][page_key] = {}
                    progress["pages"][page_key]["vision"] = "done"
                    completed += 1
                    progress["stats"]["vision_completed"] = completed
                    progress["stats"]["vision_pending"] = total_vision - completed
                    _save_progress(progress_path, progress)

                    click.echo(
                        f"\r[Step 5/{total_steps}] Vision API: {completed}/{total_vision} pages...",
                        nl=False,
                    )

            except RateLimitExhausted:
                click.echo(
                    f"\n[!] Rate limit exhausted after {completed}/{total_vision} pages. "
                    "Progress saved. Use --resume to continue."
                )
                progress["status"] = "paused"
                _save_progress(progress_path, progress)
                sys.exit(1)

            click.echo(f"\r[Step 5/{total_steps}] Vision API: {completed}/{total_vision} pages [OK]")

        progress["current_step"] = "merge"
        _save_progress(progress_path, progress)

    # ---------------------------------------------------------------
    # Step 6: Merge Chapters
    # ---------------------------------------------------------------
    chapter_files = []
    if not desc_only and _should_run_step(progress, "merge"):
        _print_step(6, total_steps, "Merging chapters...")

        from doc_to_markdown.merger import ChapterMerger
        merger = ChapterMerger()

        chapter_files = merger.merge(chapters, marker_results, out_dir)
        progress["chapter_files"] = chapter_files
        progress["current_step"] = "descriptions"
        _save_progress(progress_path, progress)

        _print_step(6, total_steps, f"Merging chapters: {len(chapter_files)}/{len(chapters)} [OK]")
    else:
        chapter_files = progress.get("chapter_files", [])
        # If desc-only, load chapter files from existing output
        if desc_only and not chapter_files:
            if chapters_dir.exists():
                for f in sorted(chapters_dir.glob("*.md")):
                    chapter_files.append({
                        "filename": f.name,
                        "title": f.stem.split("_", 1)[1].replace("_", " ").title() if "_" in f.stem else f.stem,
                        "page_range": "N/A",
                    })

    # ---------------------------------------------------------------
    # Step 7: Generate Descriptions
    # ---------------------------------------------------------------
    if (_should_run_step(progress, "descriptions") or desc_only) and effective_mode == "cli":
        from doc_to_markdown.cli_vision_handler import (
            check_desc_tasks_complete,
            load_desc_results,
            prepare_desc_tasks,
        )

        complete, missing = check_desc_tasks_complete(out_dir)

        if not complete or not (out_dir / "need_desc.json").exists():
            _print_step(
                7, total_steps,
                f"Descriptions (cli): preparing {len(chapter_files)} chapter tasks...",
            )
            summary = prepare_desc_tasks(chapter_files, out_dir)
            click.echo("")
            click.echo(
                "=" * 70 + "\n"
                f"CLI MODE: Pipeline paused at Step 7.\n"
                f"  Manifest: {summary['manifest_path']}\n"
                f"  Total tasks: {summary['total_tasks']}\n\n"
                "Claude Code: please read each chapter and write a description\n"
                "JSON to the path in `output_json` (see manifest for schema).\n"
                "Then re-run with --resume --mode cli to finish.\n"
                + "=" * 70
            )
            sys.exit(0)

        _print_step(
            7, total_steps,
            f"Descriptions (cli): loading {len(chapter_files)} Claude-written files...",
        )
        descriptions = load_desc_results(descriptions_dir, chapter_files)
        progress["descriptions"] = descriptions
        progress["current_step"] = "catalog"
        _save_progress(progress_path, progress)
        _print_step(
            7, total_steps,
            f"Descriptions (cli): {len(descriptions)}/{len(chapter_files)} loaded [OK]",
        )

    elif _should_run_step(progress, "descriptions") or desc_only:
        # API mode
        _print_step(7, total_steps, "Generating descriptions...")

        from doc_to_markdown.desc_generator import DescGenerator
        desc_gen = DescGenerator(model=model)

        def desc_progress(current, total):
            click.echo(
                f"\r[Step 7/{total_steps}] Generating descriptions: {current}/{total}...",
                nl=False,
            )

        descriptions = desc_gen.generate_all(chapter_files, chapters_dir, progress_callback=desc_progress)

        # Save individual description files
        for desc in descriptions:
            desc_file = descriptions_dir / f"{Path(desc['file']).stem}.json"
            desc_file.write_text(
                json.dumps(desc, ensure_ascii=False, indent=2), encoding="utf-8"
            )

        progress["descriptions"] = descriptions
        progress["current_step"] = "catalog"
        _save_progress(progress_path, progress)

        click.echo(f"\r[Step 7/{total_steps}] Generating descriptions: {len(descriptions)}/{len(chapter_files)} [OK]")
    else:
        descriptions = progress.get("descriptions", [])

    # ---------------------------------------------------------------
    # Step 8: Generate Catalog & README
    # ---------------------------------------------------------------
    if _should_run_step(progress, "catalog") or desc_only:
        _print_step(8, total_steps, "Writing catalog & README...")

        from doc_to_markdown.desc_generator import DescGenerator
        if "desc_gen" not in dir():
            desc_gen = DescGenerator(model=model)

        stats = {
            "pdf_name": pdf_name,
            "total_pages": page_count if "page_count" in dir() else 0,
            "marker_ok": progress.get("stats", {}).get("marker_completed", 0),
            "vision_redo": len(needs_redo) if "needs_redo" in dir() else 0,
            "vision_image_desc": len(needs_vision_desc) if "needs_vision_desc" in dir() else 0,
        }

        desc_gen.generate_catalog(descriptions, out_dir)
        desc_gen.generate_readme(descriptions, stats, out_dir)

        # Save conversion log
        conversion_log.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "pdf": str(pdf_path_obj),
            "output": str(out_dir),
            "stats": stats,
        })
        log_path.write_text(
            json.dumps(conversion_log, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        progress["status"] = "completed"
        progress["current_step"] = "done"
        _save_progress(progress_path, progress)

        _print_step(8, total_steps, "Writing catalog & README [OK]")

    # ---------------------------------------------------------------
    # Done
    # ---------------------------------------------------------------
    click.echo("")
    click.echo(f"Conversion complete! Output: {out_dir}")
    click.echo(f"  Chapters: {len(chapter_files)} files in {chapters_dir}")
    click.echo(f"  Catalog:  {out_dir / 'catalog.json'}")
    click.echo(f"  README:   {out_dir / 'README.md'}")


def _should_run_step(progress: dict, step_name: str) -> bool:
    """Check if a pipeline step should run based on progress."""
    if not progress or progress.get("status") == "completed":
        return True

    current = progress.get("current_step", "")
    if not current:
        return True

    # Get index of current step and requested step
    try:
        current_idx = STEPS.index(current)
        step_idx = STEPS.index(step_name)
    except ValueError:
        return True

    # Run if we haven't passed this step yet
    return step_idx >= current_idx


if __name__ == "__main__":
    main()
