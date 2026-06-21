"""
Tint the texture.

This file includes:
- Model display
- Model cycling
- Translation
- Coloured surfaces
- Textured surfaces
- Tinted textured surfaces
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 5 - Texture Tinting",
        allowed_modes=["normal", "colour", "texture", "tinted"],
        starting_mode="normal",
        needs_texture=True,
    )