"""Chapter merger - assembles per-page markdown into per-chapter .md files."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from doc_to_markdown.config import MAX_CHAPTER_COUNT, MAX_FILE_SIZE_KB


class ChapterMerger:
    """Merges per-page markdown results into chapter-level .md files."""

    def merge(
        self,
        chapters: list[dict],
        page_markdowns: dict[int, str],
        output_dir: Path,
    ) -> list[dict]:
        """Merge page markdowns into chapter files.

        Args:
            chapters: List of {title, start_page, end_page} from PdfInfo.get_chapters()
            page_markdowns: {page_num: markdown_text} from conversion
            output_dir: Root output directory (chapters/ subdir will be created)

        Returns:
            List of {filename, title, page_range, size_kb} for each chapter file
        """
        chapters_dir = output_dir / "chapters"
        chapters_dir.mkdir(parents=True, exist_ok=True)

        results = []

        if len(chapters) > MAX_CHAPTER_COUNT:
            print(
                f"WARNING: {len(chapters)} chapters detected, exceeds limit of "
                f"{MAX_CHAPTER_COUNT}. Consider adjusting split granularity."
            )

        for i, chapter in enumerate(chapters):
            title = chapter["title"]
            start = chapter["start_page"]
            end = chapter["end_page"]

            # Collect all page markdowns for this chapter
            content_parts = []
            for page_num in range(start, end + 1):
                md = page_markdowns.get(page_num, "")
                if md.strip():
                    content_parts.append(md)

            content = "\n\n".join(content_parts)

            # Add chapter title as H1 if not already present
            if content and not content.lstrip().startswith("# "):
                content = f"# {title}\n\n{content}"

            filename = self._format_filename(i + 1, title)
            filepath = chapters_dir / filename

            filepath.write_text(content, encoding="utf-8")

            size_kb = len(content.encode("utf-8")) / 1024

            if size_kb > MAX_FILE_SIZE_KB:
                print(
                    f"WARNING: {filename} is {size_kb:.0f}KB, "
                    f"exceeds {MAX_FILE_SIZE_KB}KB limit. Consider splitting."
                )

            results.append({
                "filename": filename,
                "title": title,
                "page_range": f"{start + 1}-{end + 1}",
                "size_kb": round(size_kb, 1),
            })

        return results

    def _format_filename(self, index: int, title: str) -> str:
        """Generate a clean filename like '01_introduction.md'."""
        # Normalize unicode
        clean = unicodedata.normalize("NFKD", title)
        # Keep only alphanumeric, spaces, hyphens
        clean = re.sub(r"[^\w\s-]", "", clean)
        # Replace whitespace with underscores
        clean = re.sub(r"\s+", "_", clean.strip())
        # Lowercase
        clean = clean.lower()
        # Truncate to reasonable length
        if len(clean) > 60:
            clean = clean[:60].rstrip("_")
        # Handle empty title
        if not clean:
            clean = "untitled"

        return f"{index:02d}_{clean}.md"
