"""
Display and swap 3D models.
"""

from common_models import run_project


if __name__ == "__main__":
    run_project(
        window_title="Question 1 - Display Models",
        allowed_modes=["wire"],
        starting_mode="wire",
        needs_texture=False,
    )