"""
Question 5 - Tint the textured models.

This file includes:
- Model display
- Model cycling
- Translation
- Coloured surfaces
- Textured surfaces
- Tinted textured surfaces

Controls:
M = cycle model
V = switch between normal, colour, texture and tinted view
T = toggle texture view
C = toggle colour view
A/D = move on X-axis
W/S = move on Y-axis
Z/X = move on Z-axis
Arrow keys = rotate model
ESC = quit
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 5 - Texture Tinting",
        allowed_modes=["normal", "colour", "texture", "tinted"],
        starting_mode="normal",
        needs_texture=True,
    )