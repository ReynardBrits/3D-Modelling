# ITGDA4-14 Initial Project 1

## Project Description

This project uses Python, PyOpenGL and pygame-ce to render and manipulate 3D models. The models used in the project are:

* Cube
* Pyramid
* Prism

The project includes model swapping, translation, colouring, texturing and tinted texturing.

---

## Required Packages

Install the required packages using:

```bash
pip install -r requirements.txt
```

The required packages are:

PyOpenGL
pygame-ce

---

## Generate the Texture

Before running Question 4 or Question 5, generate the texture image by running:

```bash
python generate_texture.py
```

This creates the `texture.png` file used for the textured and tinted views.

---

## How to Run the Project

Run each question separately from the terminal:

```bash
python q1_display.py
python q2_translate.py
python q3_colour.py
python q4_texture.py
python q5_tint.py
```

---

## Controls

| Key           | Action                                   |
| ------------- | ---------------------------------------- |
| `M`           | Cycle between cube, pyramid and prism    |
| `A`           | Move model left on the X-axis            |
| `D`           | Move model right on the X-axis           |
| `W`           | Move model up on the Y-axis              |
| `S`           | Move model down on the Y-axis            |
| `Z`           | Move model further away on the Z-axis    |
| `X`           | Move model closer on the Z-axis          |
| `V`           | Cycle between the available view modes   |
| `C`           | Toggle coloured view where available     |
| `T`           | Toggle textured view where available     |
| `Left Arrow`  | Rotate model left                        |
| `Right Arrow` | Rotate model right                       |
| `Up Arrow`    | Rotate model upward                      |
| `Down Arrow`  | Rotate model downward                    |
| `Q`           | Rotate model anticlockwise on the Z-axis |
| `E`           | Rotate model clockwise on the Z-axis     |
| `ESC`         | Close the program                        |

---

## Question 1: Display

Run:

```bash
python q1_display.py
```

This displays one model at a time. Press `M` to cycle through:

Cube -> Pyramid -> Prism -> Cube


---

## Question 2: Translation

Run:

```bash
python q2_translate.py
```

This allows the model to move on all three axes:

A / D = X-axis movement
W / S = Y-axis movement
Z / X = Z-axis movement


When the model is changed using `M`, the new model stays in the same position.

---

## Question 3: Colouring

Run:

```bash
python q3_colour.py
```

This adds coloured surfaces to the models. The model edges remain white.

Use:

V = switch between normal and coloured view
C = toggle coloured view


---

## Question 4: Texturing

Run:

```bash
python q4_texture.py
```

This adds textured surfaces using `texture.png`.

Use:

V = switch between normal, coloured and textured view
T = toggle textured view


---

## Question 5: Tinting

Run:

```bash
python q5_tint.py
```

This adds tinted textures by combining the texture with the surface colours.

Use:

V = switch between normal, coloured, textured and tinted view


---

## Files Included


q1_display.py
q2_translate.py
q3_colour.py
q4_texture.py
q5_tint.py
common_models.py
generate_texture.py
texture.png
requirements.txt
README.md
.gitignore


---

## Notes

The shared model data and drawing functions are stored in `common_models.py`. Each question file runs the required version of the project for that question.
