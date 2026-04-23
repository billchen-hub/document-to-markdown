"""Vision-based PDF page conversion via LLM API.

Converts PDF page images to Markdown and generates image descriptions
for RAG pipelines. Two providers are supported:

- ``anthropic`` - uses the public Anthropic Claude API.
- ``openai-compatible`` - any OpenAI-compatible endpoint (including
  corporate on-prem AI gateways such as internal Qwen/LLaMA deployments).

Includes rate-limit handling with exponential backoff and automatic
image splitting for oversized requests.
"""
from __future__ import annotations

import base64
import json
import logging
import time
from io import BytesIO
from typing import Any

import anthropic
import PIL.Image

from doc_to_markdown import config

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Prompts (English for best API quality)
# ---------------------------------------------------------------------------

PROMPT_PAGE_CONVERSION = (
    "Convert this PDF page to well-structured Markdown. "
    "Preserve ALL text content, tables (use Markdown table syntax), "
    "headings, and lists exactly as shown. For any figures or diagrams, "
    "provide a detailed text description in brackets."
)

PROMPT_IMAGE_DESCRIPTION = (
    "Describe this technical diagram or figure from a UFS storage "
    "specification document. Provide a detailed description suitable for "
    "text-based search and retrieval. Include all labels, values, "
    "relationships, and technical details visible in the image."
)

PROMPT_COMPARISON = (
    "Compare the following Markdown text against this PDF page image. "
    "Rate the structural similarity from 0.0 to 1.0 considering: "
    "heading accuracy, table completeness, content coverage. "
    'Respond in JSON format: {"similarity": float, "issues": ["issue1", ...]}'
)

# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------


class RateLimitExhausted(Exception):
    """Raised when all retry attempts are exhausted due to rate limiting."""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _pil_to_base64(image: PIL.Image.Image) -> str:
    """Encode a PIL Image as a base64 PNG string."""
    buf = BytesIO()
    image.save(buf, format="PNG")
    return base64.standard_b64encode(buf.getvalue()).decode()


def _split_image_halves(
    image: PIL.Image.Image,
) -> tuple[PIL.Image.Image, PIL.Image.Image]:
    """Split a PIL Image into top and bottom halves."""
    width, height = image.size
    mid = height // 2
    top = image.crop((0, 0, width, mid))
    bottom = image.crop((0, mid, width, height))
    return top, bottom


# ---------------------------------------------------------------------------
# VisionConverter
# ---------------------------------------------------------------------------


class VisionConverter:
    """Converts PDF page images to Markdown via a Vision/LLM API.

    Supports two providers via ``config.VISION_PROVIDER``:

    - ``anthropic`` (default)
    - ``openai-compatible`` - for OpenAI-compatible endpoints such as an
      on-prem Qwen/LLaMA gateway. Requires ``base_url``.
    """

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        provider: str | None = None,
        base_url: str | None = None,
    ) -> None:
        self.model = model or config.DEFAULT_VISION_MODEL
        resolved_key = api_key or config.VISION_API_KEY
        resolved_provider = (provider or config.VISION_PROVIDER or "anthropic").lower()
        resolved_base_url = base_url or config.VISION_BASE_URL

        if not resolved_key:
            raise ValueError(
                "No API key provided. Set VISION_API_KEY (or ANTHROPIC_API_KEY) "
                "environment variable, or pass api_key explicitly."
            )

        self.provider = resolved_provider
        self.base_url = resolved_base_url

        if resolved_provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=resolved_key)
        elif resolved_provider == "openai-compatible":
            try:
                import openai  # type: ignore
            except ImportError as exc:
                raise ImportError(
                    "openai package required for provider 'openai-compatible'. "
                    "Install via: pip install openai"
                ) from exc
            if not resolved_base_url:
                raise ValueError(
                    "VISION_BASE_URL is required for provider 'openai-compatible'."
                )
            self.client = openai.OpenAI(
                api_key=resolved_key,
                base_url=resolved_base_url,
            )
        else:
            raise ValueError(
                f"Unknown VISION_PROVIDER: {resolved_provider!r}. "
                "Expected 'anthropic' or 'openai-compatible'."
            )

    # -- internal helpers ---------------------------------------------------

    def _build_image_message(
        self,
        b64: str,
        prompt: str,
    ) -> list[dict[str, Any]]:
        """Build the ``messages`` list for a single-image request.

        Format depends on provider - Anthropic and OpenAI-compatible
        endpoints use different image content schemas.
        """
        if self.provider == "anthropic":
            return [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": b64,
                            },
                        },
                        {"type": "text", "text": prompt},
                    ],
                }
            ]
        # openai-compatible
        return [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{b64}",
                        },
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ]

    def _invoke(
        self,
        messages: list[dict[str, Any]],
        max_tokens: int,
    ) -> str:
        """Provider-agnostic single API call returning response text."""
        if self.provider == "anthropic":
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=messages,
            )
            text_parts = [
                block.text for block in response.content if hasattr(block, "text")
            ]
            return "\n".join(text_parts)

        # openai-compatible
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=messages,
        )
        try:
            return response.choices[0].message.content or ""
        except (AttributeError, IndexError):
            return ""

    def _call_api(
        self,
        messages: list[dict[str, Any]],
        max_tokens: int = 4096,
    ) -> str:
        """Send a request with retry logic across both providers.

        Handles rate-limit errors with exponential back-off. Authentication
        errors surface immediately.
        """
        last_exc: Exception | None = None

        # Collect exception classes from each installed SDK.
        rate_limit_excs: list[type[BaseException]] = [anthropic.RateLimitError]
        auth_excs: list[type[BaseException]] = [anthropic.AuthenticationError]
        try:
            import openai  # type: ignore
            rate_limit_excs.append(openai.RateLimitError)
            auth_excs.append(openai.AuthenticationError)
        except ImportError:
            pass

        rate_limit_tuple = tuple(rate_limit_excs)
        auth_tuple = tuple(auth_excs)

        for attempt in range(config.MAX_RETRIES):
            try:
                return self._invoke(messages, max_tokens)
            except rate_limit_tuple as exc:  # type: ignore[misc]
                last_exc = exc
                delay = config.RETRY_BASE_DELAY * (2 ** attempt)
                logger.warning(
                    "Rate limited (attempt %d/%d). Retrying in %ds ...",
                    attempt + 1,
                    config.MAX_RETRIES,
                    delay,
                )
                time.sleep(delay)
            except auth_tuple:  # type: ignore[misc]
                raise  # surface immediately

        raise RateLimitExhausted(
            f"Rate limit not resolved after {config.MAX_RETRIES} retries "
            f"(last error: {last_exc})"
        )

    def _call_api_with_overflow_fallback(
        self,
        image: PIL.Image.Image,
        prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Call the API; on token-overflow errors, split the image and retry."""
        b64 = _pil_to_base64(image)
        messages = self._build_image_message(b64, prompt)

        bad_request_excs: list[type[BaseException]] = [anthropic.BadRequestError]
        try:
            import openai  # type: ignore
            bad_request_excs.append(openai.BadRequestError)
        except ImportError:
            pass
        bad_request_tuple = tuple(bad_request_excs)

        try:
            return self._call_api(messages, max_tokens=max_tokens)
        except bad_request_tuple as exc:  # type: ignore[misc]
            error_body = str(exc).lower()
            if "too large" in error_body or "token" in error_body:
                logger.warning(
                    "Request too large; splitting image into halves."
                )
                return self._convert_split(image, prompt, max_tokens)
            raise

    def _convert_split(
        self,
        image: PIL.Image.Image,
        prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Split the image in half and convert each part separately."""
        top, bottom = _split_image_halves(image)

        top_b64 = _pil_to_base64(top)
        top_messages = self._build_image_message(top_b64, prompt)
        top_md = self._call_api(top_messages, max_tokens=max_tokens)

        bottom_b64 = _pil_to_base64(bottom)
        bottom_messages = self._build_image_message(bottom_b64, prompt)
        bottom_md = self._call_api(bottom_messages, max_tokens=max_tokens)

        return f"{top_md}\n\n{bottom_md}"

    # -- public API ---------------------------------------------------------

    def convert_page(self, image: PIL.Image.Image, page_num: int) -> str:
        """Convert a single PDF page image to Markdown.

        Parameters
        ----------
        image:
            A PIL Image of the rendered PDF page.
        page_num:
            1-based page number (used only for logging).

        Returns
        -------
        str
            The Markdown representation of the page.
        """
        logger.info("Converting page %d via Vision API ...", page_num)
        auth_excs: list[type[BaseException]] = [anthropic.AuthenticationError]
        try:
            import openai  # type: ignore
            auth_excs.append(openai.AuthenticationError)
        except ImportError:
            pass
        auth_tuple = tuple(auth_excs)
        try:
            md = self._call_api_with_overflow_fallback(
                image, PROMPT_PAGE_CONVERSION
            )
        except RateLimitExhausted:
            raise
        except auth_tuple:  # type: ignore[misc]
            raise
        except Exception as exc:
            logger.warning(
                "Unexpected error converting page %d: %s. "
                "Returning empty string.",
                page_num,
                exc,
            )
            return ""
        return md

    def describe_image(
        self, image: PIL.Image.Image, context: str = ""
    ) -> str:
        """Generate a textual description of a figure or diagram for RAG.

        Parameters
        ----------
        image:
            The cropped figure / diagram image.
        context:
            Optional surrounding text to give the model more context.

        Returns
        -------
        str
            A detailed natural-language description of the image.
        """
        prompt = PROMPT_IMAGE_DESCRIPTION
        if context:
            prompt += f"\n\nAdditional context from the surrounding text:\n{context}"

        b64 = _pil_to_base64(image)
        messages = self._build_image_message(b64, prompt)
        return self._call_api(messages, max_tokens=4096)

    def compare_outputs(
        self, image: PIL.Image.Image, marker_md: str
    ) -> dict[str, Any]:
        """Ask the Vision model to evaluate Marker output against the page.

        Parameters
        ----------
        image:
            The original PDF page image.
        marker_md:
            The Markdown text produced by Marker for this page.

        Returns
        -------
        dict
            ``{"similarity": float, "issues": [str, ...]}``
        """
        prompt = (
            f"{PROMPT_COMPARISON}\n\n"
            f"--- Markdown output to evaluate ---\n{marker_md}"
        )
        b64 = _pil_to_base64(image)
        messages = self._build_image_message(b64, prompt)
        raw = self._call_api(messages, max_tokens=2048)

        # Attempt to parse the JSON response.
        try:
            # The model may wrap the JSON in a code fence; strip it.
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                # Remove opening fence (possibly ```json)
                first_newline = cleaned.index("\n")
                cleaned = cleaned[first_newline + 1 :]
            if cleaned.endswith("```"):
                cleaned = cleaned[: -3]
            cleaned = cleaned.strip()

            result = json.loads(cleaned)

            # Normalise the expected keys.
            similarity = float(result.get("similarity", 0.0))
            issues = result.get("issues", [])
            if not isinstance(issues, list):
                issues = [str(issues)]

            return {"similarity": similarity, "issues": issues}

        except (json.JSONDecodeError, ValueError, TypeError) as exc:
            logger.warning(
                "Could not parse comparison JSON (%s). Raw response: %s",
                exc,
                raw[:500],
            )
            return {"similarity": 0.0, "issues": [f"Unparseable response: {raw[:200]}"]}

    def validate_api_key(self) -> bool:
        """Quick check whether the configured API key is valid.

        Sends a minimal, inexpensive request.  Returns ``True`` if the key
        is accepted, ``False`` otherwise.
        """
        auth_excs: list[type[BaseException]] = [anthropic.AuthenticationError]
        try:
            import openai  # type: ignore
            auth_excs.append(openai.AuthenticationError)
        except ImportError:
            pass
        auth_tuple = tuple(auth_excs)

        try:
            if self.provider == "anthropic":
                self.client.messages.create(
                    model=self.model,
                    max_tokens=1,
                    messages=[{"role": "user", "content": "Hi"}],
                )
            else:
                self.client.chat.completions.create(
                    model=self.model,
                    max_tokens=1,
                    messages=[{"role": "user", "content": "Hi"}],
                )
            return True
        except auth_tuple:  # type: ignore[misc]
            return False
        except Exception as exc:
            logger.warning("API key validation encountered an error: %s", exc)
            return False
