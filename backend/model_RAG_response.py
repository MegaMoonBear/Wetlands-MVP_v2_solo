"""Legacy script for running model_RAG_response demo.

This module is kept import-safe: it no longer executes IO at import time.
Use `ollama_vision.analyze_wetland_image()` for programmatic access.
"""

from typing import Optional


def run_demo(image_path: Optional[str] = None) -> None:
    """Small demo wrapper kept for manual runs. Importing this module does nothing.

    If run as a script, this will call `ollama_vision.analyze_wetland_image`.
    """
    try:
        # Guarded import: perform the import only when running the demo to avoid
        # import-time side effects and potential circular imports in tests.
        from ollama_vision import analyze_wetland_image
    except Exception:
        print("Demo requires `ollama_vision` to be available in the same folder.")
        return

    path = image_path or "images_preUpload/AnimalWaterBranches.png"
    try:
        resp = analyze_wetland_image(path)
        print(resp)
    except Exception as e:
        print(f"Error running demo: {e}")


if __name__ == "__main__":
    # When executed as a script, run the demo; importing this module elsewhere
    # will not trigger the demo because of the __main__ guard.
    run_demo()
