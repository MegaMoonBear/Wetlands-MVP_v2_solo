"""High-level interface to the Ollama Vision model.

This module exposes `analyze_wetland_image(image_path)` for programmatic
use. It is safe to import (no IO or network calls at import time).
"""

import logging
from typing import Dict, Optional

# Ollama client library used to call the LLaMA Vision model
import ollama
# Local utility to convert image files to base64; safe to import (no IO at import-time)
from image_util import convert_image_to_base64

logger = logging.getLogger(__name__)


def analyze_wetland_image(image_path: str) -> Dict:
    """Convert an image to base64 (when available) and call the Ollama Vision model.

        - If the image is missing or unreadable we log and call the model without
      `ollama.chat` without the image so tests can mock the model call.
    - Exceptions raised by `ollama.chat` are propagated so callers/tests can
      assert on them.
    """
    base64_image: Optional[str] = None
    try:
        base64_image = convert_image_to_base64(image_path)
    except FileNotFoundError:
        logger.warning("Image file not found: %s. Calling model without image.", image_path)
    except OSError as e:
        logger.warning("OS error reading image %s: %s. Calling model without image.", image_path, e)

    prompt = (
        "You are a nature guide that knows about water, wetlands, animals, and plants. "
        "Animals include birds, mammals, reptiles, amphibians, fish, and insects. "
        "Plants include trees, flowers, shrubs, grasses, and fungi. "
        "Your goal is to teach about wetlands plants and animals, assuming learners have a 10-second attention span. "
        "You do not encourage observers to get closer or evaluate the wetland environment. "
        "Instead, process one image and text prompt using the LLaMA Vision model. "
        "First, describe the image and provide common names—not genus and species. "
        "If species is unclear, suggest higher taxonomic levels (e.g., Genus, Family). "
        "At the roughest level, suggestions should be 'plant', 'animal', or 'unknown species'. "
        "Second, provide 1 interesting fact related to the taxonomic recommendations that would take a 5th grader about 10 seconds to read. "
        "The fact should be concise, engaging, and focused on wetlands plants and animals, fresh water, and the ecological importance of wetlands. "
        "What is in this image?"
    )

    message = {"role": "user", "content": prompt}
    if base64_image:
        message["images"] = [base64_image]

        # Uncomment the following lines after database creation to save the base64 string
        # with open("encoded_image.txt", "w") as f:
        #     f.write(base64_image)

    # Call the Ollama API; propagate exceptions to let callers/tests handle them
    response = ollama.chat(model="llama3.2-vision", messages=[message])
    return response
