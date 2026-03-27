"""Description generator - creates per-chapter descriptions and catalog for RAG."""
from __future__ import annotations

import json
import time
from pathlib import Path

import anthropic

from doc_to_markdown.config import (
    ANTHROPIC_API_KEY,
    DEFAULT_VISION_MODEL,
    MAX_RETRIES,
    RETRY_BASE_DELAY,
)

DESCRIPTION_PROMPT = """Read this Markdown chapter from a technical specification document.

Generate:
1. A "description" in Traditional Chinese (2-3 sentences) that summarizes what this chapter covers. The description should help a RAG system decide when to retrieve this document. Mention key topics, concepts, and what questions this chapter can answer.
2. A list of 3-6 English "keywords" that capture the main topics.

Chapter title: {title}
Page range: {page_range}

Respond ONLY in this exact JSON format (no markdown fencing):
{{"description": "...", "keywords": ["...", "..."]}}

Chapter content:
{content}"""


class DescGenerator:
    """Generates descriptions and keywords for chapter files using Claude API."""

    def __init__(self, model: str | None = None, api_key: str | None = None):
        self.model = model or DEFAULT_VISION_MODEL
        self.api_key = api_key or ANTHROPIC_API_KEY
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not set. Set it as environment variable or pass api_key."
            )
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(
        self, md_content: str, filename: str, title: str, page_range: str
    ) -> dict:
        """Generate description and keywords for a chapter.

        Returns:
            {file, title, description, keywords, page_range}
        """
        # Truncate content if too long (keep first ~15000 chars for API limits)
        content = md_content
        if len(content) > 15000:
            content = content[:15000] + "\n\n[... content truncated for description generation ...]"

        prompt = DESCRIPTION_PROMPT.format(
            title=title, page_range=page_range, content=content
        )

        response_text = self._call_api(prompt)

        # Parse JSON from response
        try:
            # Try to extract JSON from the response
            text = response_text.strip()
            # Remove markdown code fencing if present
            if text.startswith("```"):
                text = text.split("\n", 1)[1]
                if text.endswith("```"):
                    text = text[: text.rfind("```")]
                text = text.strip()
            if text.startswith("json"):
                text = text[4:].strip()

            data = json.loads(text)
        except json.JSONDecodeError:
            print(f"WARNING: Failed to parse description JSON for {filename}, using raw text")
            data = {
                "description": response_text[:500],
                "keywords": [],
            }

        return {
            "file": filename,
            "title": title,
            "description": data.get("description", ""),
            "keywords": data.get("keywords", []),
            "page_range": page_range,
        }

    def generate_all(
        self,
        chapter_files: list[dict],
        chapters_dir: Path,
        progress_callback=None,
    ) -> list[dict]:
        """Generate descriptions for all chapter files.

        Args:
            chapter_files: List of {filename, title, page_range} from merger
            chapters_dir: Directory containing the .md files
            progress_callback: Called with (current, total)

        Returns:
            List of description dicts
        """
        descriptions = []
        total = len(chapter_files)

        for i, info in enumerate(chapter_files):
            filepath = chapters_dir / info["filename"]
            if filepath.exists():
                content = filepath.read_text(encoding="utf-8")
            else:
                content = ""

            desc = self.generate(
                md_content=content,
                filename=info["filename"],
                title=info["title"],
                page_range=info["page_range"],
            )
            descriptions.append(desc)

            if progress_callback:
                progress_callback(i + 1, total)

        return descriptions

    def generate_catalog(self, descriptions: list[dict], output_dir: Path) -> None:
        """Write catalog.json with all descriptions."""
        catalog_path = output_dir / "catalog.json"
        catalog = {
            "total_files": len(descriptions),
            "files": descriptions,
        }
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def generate_readme(
        self, descriptions: list[dict], stats: dict, output_dir: Path
    ) -> None:
        """Write README.md summary of conversion results."""
        readme_path = output_dir / "README.md"

        lines = [
            f"# {stats.get('pdf_name', 'PDF')} Conversion Results",
            "",
            f"- Total pages: {stats.get('total_pages', 'N/A')}",
            f"- Total chapters: {len(descriptions)}",
            f"- Marker converted: {stats.get('marker_ok', 'N/A')} pages",
            f"- Vision API redo: {stats.get('vision_redo', 0)} pages",
            f"- Vision image descriptions: {stats.get('vision_image_desc', 0)} pages",
            "",
            "## Chapters",
            "",
        ]

        for desc in descriptions:
            lines.append(
                f"### {desc['title']} (pages {desc['page_range']})"
            )
            lines.append("")
            lines.append(f"**File:** `{desc['file']}`")
            lines.append("")
            lines.append(desc.get("description", ""))
            lines.append("")
            keywords = ", ".join(desc.get("keywords", []))
            if keywords:
                lines.append(f"**Keywords:** {keywords}")
                lines.append("")

        readme_path.write_text("\n".join(lines), encoding="utf-8")

    def _call_api(self, prompt: str) -> str:
        """Call Claude API with retry logic."""
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text
            except anthropic.RateLimitError:
                if attempt < MAX_RETRIES:
                    delay = RETRY_BASE_DELAY * (2 ** attempt)
                    print(f"  Rate limited, retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    raise
            except anthropic.AuthenticationError:
                raise ValueError(
                    "Invalid ANTHROPIC_API_KEY. Check your API key."
                )
