"""
Translate the 3D models.

This file includes the Question 1 display and model cycling.
It adds movement on the X, Y and Z axes in both positive and negative directions.
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 2 - Translation",
        allowed_modes=["wire"],
        starting_mode="wire",
        needs_texture=False,
    )