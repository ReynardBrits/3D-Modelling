"""
Colour each surface.

This file includes:
- Model display
- Model cycling
- Translation
- Coloured opaque surfaces
- White edges
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 3 - Surface Colours",
        allowed_modes=["normal", "colour"],
        starting_mode="normal",
        needs_texture=False,
    )