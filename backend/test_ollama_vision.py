# Unit tests for analyze_wetland_image() or __________ - These tests mock external ollama.chat() API to ensure...
# fast, reliable, # and isolated testing without making real model calls. The suite verifies:
    # 1) Expected behavior under normal conditions (happy path),
    # 2) Proper handling of edge outputs like "unknown species",
    # 3) Robust error handling when the API raises exceptions.
# The goal is to test behavior and response structure—not the external model itself.

import pytest
from unittest.mock import patch
from ollama_vision import analyze_wetland_image

# ------------------------
# HAPPY PATH TEST
# ------------------------
@patch("ollama.chat")
def test_analyze_wetland_image_success(mock_chat):
    mock_chat.return_value = {
        "message": {
            "content": "animal - This bird can see ultraviolet light."
        }
    }

    result = analyze_wetland_image("fake/path/image.jpg")

    assert result["message"]["content"].startswith("animal")
    mock_chat.assert_called_once()


# ------------------------
# EDGE CASE TEST
# ------------------------
@patch("ollama.chat")
def test_analyze_wetland_image_unknown_species(mock_chat):
    mock_chat.return_value = {
        "message": {
            "content": "unknown species - Some organisms are hard to identify."
        }
    }

    result = analyze_wetland_image("fake/path/image.jpg")

    assert "unknown species" in result["message"]["content"]


# ------------------------
# ERROR HANDLING TEST
# ------------------------
@patch("ollama.chat")
def test_analyze_wetland_image_api_failure(mock_chat):
    mock_chat.side_effect = Exception("API failure")

    with pytest.raises(Exception) as exc_info:
        analyze_wetland_image("fake/path/image.jpg")

    assert "API failure" in str(exc_info.value)


# ------------------------
# FILE / IO ERROR TESTS
# ------------------------
def test_analyze_wetland_image_file_not_found_calls_model():
    # When the image file is missing, we expect the function to log and still
    # call `ollama.chat` without the image; the model response should be returned.
    from unittest.mock import patch
    with patch("ollama_vision.convert_image_to_base64") as mock_convert, patch("ollama.chat") as mock_chat:
        mock_convert.side_effect = FileNotFoundError()
        mock_chat.return_value = {"message": {"content": "animal - fallback response"}}

        result = analyze_wetland_image("nonexistent.jpg")

        assert result["message"]["content"].startswith("animal")
        mock_chat.assert_called_once()
        mock_convert.assert_called_once_with("nonexistent.jpg")


def test_analyze_wetland_image_os_error_calls_model():
    # For IO/OSError (e.g., permissions), the function should still call the model
    from unittest.mock import patch
    with patch("ollama_vision.convert_image_to_base64") as mock_convert, patch("ollama.chat") as mock_chat:
        mock_convert.side_effect = OSError("Permission denied")
        mock_chat.return_value = {"message": {"content": "plant - fallback response"}}

        result = analyze_wetland_image("unreadable.jpg")

        assert result["message"]["content"].startswith("plant")
        mock_chat.assert_called_once()
        mock_convert.assert_called_once_with("unreadable.jpg")


def test_analyze_wetland_image_invalid_format_propagates():
    # If image decoding raises a format error (ValueError), that is not caught
    # by the function and should propagate to the caller.
    from unittest.mock import patch
    with patch("ollama_vision.convert_image_to_base64") as mock_convert, patch("ollama.chat") as mock_chat:
        mock_convert.side_effect = ValueError("Invalid image format")

        with pytest.raises(ValueError):
            analyze_wetland_image("bad_format.jpg")

        # Ensure the model was not called when decoding raises an unexpected error
        mock_chat.assert_not_called()
