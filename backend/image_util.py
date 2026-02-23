"""Utility helpers for image handling.

Provide `convert_image_to_base64(image_path)` for other modules to call.
This module must not execute IO at import time.
"""
import base64
from pathlib import Path
from typing import Optional


def convert_image_to_base64(image_path: str) -> str:
    """Read an image file and return a base64-encoded UTF-8 string.

    Raises FileNotFoundError or OSError on IO errors.
    """
    path = Path(image_path)
    # Normalize and validate the path before attempting to open the file
    if not path.exists():
        # Explicitly raise FileNotFoundError so callers/tests can catch it
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Read binary image data and return a base64-encoded UTF-8 string
    with path.open("rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")