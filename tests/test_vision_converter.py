"""Tests for doc_to_markdown.vision_converter module.

All API calls are mocked -- no real Anthropic requests are made.
"""

import base64
import json

import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from PIL import Image
import anthropic

from doc_to_markdown.vision_converter import (
    RateLimitExhausted,
    VisionConverter,
    _pil_to_base64,
    _split_image_halves,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def small_image():
    """A tiny RGB image for testing."""
    return Image.new("RGB", (100, 100), color="white")


@pytest.fixture
def tall_image():
    """A taller image to verify split dimensions."""
    return Image.new("RGB", (200, 300), color="blue")


@pytest.fixture
def converter():
    """A VisionConverter with a dummy API key and mocked client."""
    with patch("doc_to_markdown.vision_converter.anthropic.Anthropic"):
        vc = VisionConverter(api_key="test-key-12345")
    return vc


def _make_api_response(text: str) -> MagicMock:
    """Build a mock Messages API response containing a single text block."""
    block = MagicMock()
    block.text = text
    response = MagicMock()
    response.content = [block]
    return response


# ---------------------------------------------------------------------------
# RateLimitExhausted
# ---------------------------------------------------------------------------


class TestRateLimitExhausted:
    def test_is_exception_subclass(self):
        assert issubclass(RateLimitExhausted, Exception)

    def test_can_be_raised_and_caught(self):
        with pytest.raises(RateLimitExhausted, match="all retries"):
            raise RateLimitExhausted("all retries exhausted")


# ---------------------------------------------------------------------------
# __init__
# ---------------------------------------------------------------------------


class TestInit:
    def test_raises_value_error_when_no_api_key(self):
        """With no env var and no explicit key, ValueError is raised."""
        with patch("doc_to_markdown.vision_converter.config") as mock_cfg:
            mock_cfg.ANTHROPIC_API_KEY = ""
            mock_cfg.DEFAULT_VISION_MODEL = "test-model"
            with pytest.raises(ValueError, match="No Anthropic API key"):
                VisionConverter(api_key="")

    def test_raises_value_error_when_api_key_is_none_and_env_empty(self):
        with patch("doc_to_markdown.vision_converter.config") as mock_cfg:
            mock_cfg.ANTHROPIC_API_KEY = ""
            mock_cfg.DEFAULT_VISION_MODEL = "test-model"
            with pytest.raises(ValueError, match="No Anthropic API key"):
                VisionConverter(api_key=None)

    def test_succeeds_with_explicit_key(self):
        with patch("doc_to_markdown.vision_converter.anthropic.Anthropic"):
            vc = VisionConverter(api_key="sk-valid-key")
        assert vc.model is not None


# ---------------------------------------------------------------------------
# _pil_to_base64
# ---------------------------------------------------------------------------


class TestPilToBase64:
    def test_returns_valid_base64_string(self, small_image):
        result = _pil_to_base64(small_image)
        # Must be a non-empty string
        assert isinstance(result, str)
        assert len(result) > 0

    def test_base64_decodes_successfully(self, small_image):
        result = _pil_to_base64(small_image)
        # Should decode without errors
        raw = base64.standard_b64decode(result)
        assert len(raw) > 0

    def test_decoded_bytes_are_valid_png(self, small_image):
        result = _pil_to_base64(small_image)
        raw = base64.standard_b64decode(result)
        # PNG magic bytes
        assert raw[:4] == b"\x89PNG"


# ---------------------------------------------------------------------------
# _split_image_halves
# ---------------------------------------------------------------------------


class TestSplitImageHalves:
    def test_top_half_dimensions(self, small_image):
        top, _ = _split_image_halves(small_image)
        assert top.size == (100, 50)

    def test_bottom_half_dimensions(self, small_image):
        _, bottom = _split_image_halves(small_image)
        assert bottom.size == (100, 50)

    def test_odd_height_image(self):
        """With odd height, top is floor(h/2), bottom is ceil(h/2)."""
        img = Image.new("RGB", (80, 101), color="red")
        top, bottom = _split_image_halves(img)
        assert top.size == (80, 50)
        assert bottom.size == (80, 51)

    def test_tall_image_split(self, tall_image):
        top, bottom = _split_image_halves(tall_image)
        assert top.size == (200, 150)
        assert bottom.size == (200, 150)

    def test_both_halves_cover_full_height(self, small_image):
        top, bottom = _split_image_halves(small_image)
        assert top.size[1] + bottom.size[1] == small_image.size[1]


# ---------------------------------------------------------------------------
# compare_outputs
# ---------------------------------------------------------------------------


class TestCompareOutputs:
    def test_parses_valid_json_response(self, converter, small_image):
        """When the API returns well-formed JSON, it should be parsed correctly."""
        payload = json.dumps({"similarity": 0.85, "issues": ["minor heading mismatch"]})
        converter._call_api = MagicMock(return_value=payload)

        result = converter.compare_outputs(small_image, "# Some markdown")

        assert result["similarity"] == 0.85
        assert result["issues"] == ["minor heading mismatch"]

    def test_handles_malformed_json_gracefully(self, converter, small_image):
        """When the API returns garbage, similarity should default to 0.0."""
        converter._call_api = MagicMock(return_value="NOT VALID JSON {{{")

        result = converter.compare_outputs(small_image, "# Markdown")

        assert result["similarity"] == 0.0
        assert len(result["issues"]) > 0

    def test_strips_markdown_code_fence(self, converter, small_image):
        """JSON wrapped in ```json ... ``` fences should still be parsed."""
        inner = json.dumps({"similarity": 0.92, "issues": []})
        fenced = f"```json\n{inner}\n```"
        converter._call_api = MagicMock(return_value=fenced)

        result = converter.compare_outputs(small_image, "# Markdown")

        assert result["similarity"] == 0.92
        assert result["issues"] == []

    def test_strips_plain_code_fence(self, converter, small_image):
        """JSON wrapped in plain ``` ... ``` fences should still be parsed."""
        inner = json.dumps({"similarity": 0.78, "issues": ["missing table"]})
        fenced = f"```\n{inner}\n```"
        converter._call_api = MagicMock(return_value=fenced)

        result = converter.compare_outputs(small_image, "# Markdown")

        assert result["similarity"] == 0.78

    def test_missing_similarity_defaults_to_zero(self, converter, small_image):
        """If the JSON has no 'similarity' key, it should default to 0.0."""
        payload = json.dumps({"issues": ["everything"]})
        converter._call_api = MagicMock(return_value=payload)

        result = converter.compare_outputs(small_image, "# Markdown")

        assert result["similarity"] == 0.0

    def test_issues_non_list_converted_to_list(self, converter, small_image):
        """If 'issues' is not a list, it should be wrapped in one."""
        payload = json.dumps({"similarity": 0.5, "issues": "single issue"})
        converter._call_api = MagicMock(return_value=payload)

        result = converter.compare_outputs(small_image, "# Markdown")

        assert isinstance(result["issues"], list)
        assert result["issues"] == ["single issue"]


# ---------------------------------------------------------------------------
# convert_page
# ---------------------------------------------------------------------------


class TestConvertPage:
    def test_returns_markdown_text(self, converter, small_image):
        converter._call_api_with_overflow_fallback = MagicMock(
            return_value="# Hello World"
        )

        result = converter.convert_page(small_image, page_num=1)

        assert result == "# Hello World"
        converter._call_api_with_overflow_fallback.assert_called_once()

    def test_returns_empty_on_unexpected_exception(self, converter, small_image):
        converter._call_api_with_overflow_fallback = MagicMock(
            side_effect=RuntimeError("unexpected")
        )

        result = converter.convert_page(small_image, page_num=1)

        assert result == ""

    def test_propagates_rate_limit_exhausted(self, converter, small_image):
        converter._call_api_with_overflow_fallback = MagicMock(
            side_effect=RateLimitExhausted("exhausted")
        )

        with pytest.raises(RateLimitExhausted):
            converter.convert_page(small_image, page_num=1)

    def test_propagates_authentication_error(self, converter, small_image):
        converter._call_api_with_overflow_fallback = MagicMock(
            side_effect=anthropic.AuthenticationError(
                message="invalid key",
                response=MagicMock(status_code=401),
                body=None,
            )
        )

        with pytest.raises(anthropic.AuthenticationError):
            converter.convert_page(small_image, page_num=1)


# ---------------------------------------------------------------------------
# _call_api  --  rate-limit retry & auth error propagation
# ---------------------------------------------------------------------------


class TestCallApiRetryLogic:
    @patch("doc_to_markdown.vision_converter.time.sleep", return_value=None)
    def test_retries_on_rate_limit_then_succeeds(self, mock_sleep, converter):
        """After one RateLimitError the second attempt succeeds."""
        rate_err = anthropic.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429),
            body=None,
        )
        success_resp = _make_api_response("# Success")

        converter.client.messages.create = MagicMock(
            side_effect=[rate_err, success_resp]
        )

        result = converter._call_api(messages=[{"role": "user", "content": "hi"}])

        assert result == "# Success"
        assert converter.client.messages.create.call_count == 2
        mock_sleep.assert_called_once()  # slept once between attempts

    @patch("doc_to_markdown.vision_converter.time.sleep", return_value=None)
    def test_raises_rate_limit_exhausted_after_all_retries(
        self, mock_sleep, converter
    ):
        """If every attempt hits rate limit, RateLimitExhausted is raised."""
        rate_err = anthropic.RateLimitError(
            message="rate limited",
            response=MagicMock(status_code=429),
            body=None,
        )

        converter.client.messages.create = MagicMock(side_effect=rate_err)

        with pytest.raises(RateLimitExhausted, match="retries"):
            converter._call_api(messages=[{"role": "user", "content": "hi"}])

    def test_authentication_error_propagates_immediately(self, converter):
        """AuthenticationError should be re-raised on the first attempt."""
        auth_err = anthropic.AuthenticationError(
            message="invalid api key",
            response=MagicMock(status_code=401),
            body=None,
        )

        converter.client.messages.create = MagicMock(side_effect=auth_err)

        with pytest.raises(anthropic.AuthenticationError):
            converter._call_api(messages=[{"role": "user", "content": "hi"}])

        # Only called once -- no retries.
        assert converter.client.messages.create.call_count == 1


# ---------------------------------------------------------------------------
# validate_api_key
# ---------------------------------------------------------------------------


class TestValidateApiKey:
    def test_returns_true_on_success(self, converter):
        converter.client.messages.create = MagicMock(
            return_value=_make_api_response("hi")
        )

        assert converter.validate_api_key() is True

    def test_returns_false_on_authentication_error(self, converter):
        auth_err = anthropic.AuthenticationError(
            message="bad key",
            response=MagicMock(status_code=401),
            body=None,
        )
        converter.client.messages.create = MagicMock(side_effect=auth_err)

        assert converter.validate_api_key() is False

    def test_returns_false_on_other_exception(self, converter):
        converter.client.messages.create = MagicMock(
            side_effect=ConnectionError("network down")
        )

        assert converter.validate_api_key() is False
