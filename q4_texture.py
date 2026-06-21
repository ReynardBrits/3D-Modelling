"""
Texture the models.

This file includes:
- Model display
- Model cycling
- Translation
- Coloured surfaces
- Textured surfaces using texture.png
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 4 - Textures",
        allowed_modes=["normal", "colour", "texture"],
        starting_mode="normal",
        needs_texture=True,
    )