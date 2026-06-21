"""
Question 3 - Colour each surface.

This file includes:
- Model display
- Model cycling
- Translation
- Coloured opaque surfaces
- White edges

Controls:
M = cycle model
V = switch between normal and colour view
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
        window_title="Question 3 - Surface Colours",
        allowed_modes=["normal", "colour"],
        starting_mode="normal",
        needs_texture=False,
    )