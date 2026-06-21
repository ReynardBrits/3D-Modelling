"""
Question 2 - Translate the 3D models.

This file includes the Question 1 display and model cycling.
It adds movement on the X, Y and Z axes in both positive and negative directions.

Controls:
M = cycle model
A = move left on X-axis
D = move right on X-axis
W = move up on Y-axis
S = move down on Y-axis
Z = move backwards on Z-axis
X = move forwards on Z-axis
Arrow keys = rotate model
ESC = quit
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 2 - Translation",
        allowed_modes=["wire"],
        starting_mode="wire",
        needs_texture=False,
    )