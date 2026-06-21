"""
OpenGL code for the ITGDA4-14 Initial Project 1.

This file contains:
- Cube, pyramid and prism model data
- Model swapping
- Translation on X, Y and Z axes
- Surface colouring
- Texture loading
- Texture tinting
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT, KEYDOWN, K_ESCAPE
from OpenGL.GL import *
from OpenGL.GLU import *


Vec3 = Tuple[float, float, float]
Edge = Tuple[int, int]
Face = Tuple[int, ...]
Colour = Tuple[float, float, float]


MODELS: Dict[str, Dict[str, object]] = {
    "Cube": {
        "vertices": (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1),
        ),
        "edges": (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),
        ),
        "faces": (
            (0, 1, 2, 3),
            (4, 6, 7, 5),
            (0, 4, 5, 1),
            (3, 2, 7, 6),
            (1, 5, 7, 2),
            (0, 3, 6, 4),
        ),
    },
    "Pyramid": {
        "vertices": (
            (1, -1, 1),
            (-1, -1, 1),
            (0, -1, -1),
            (1, 1, 0.5),
        ),
        "edges": (
            (0, 1),
            (0, 2),
            (0, 3),
            (2, 1),
            (2, 3),
            (3, 1),
        ),
        "faces": (
            (0, 1, 2),
            (0, 3, 1),
            (0, 2, 3),
            (1, 3, 2),
        ),
    },
    "Prism": {
        "vertices": (
            (-1, -1, 1),
            (1, -1, 1),
            (0, 1, 1),
            (-1, -1, -1),
            (1, -1, -1),
            (0, 1, -1),
        ),
        "edges": (
            (0, 1),
            (0, 2),
            (1, 2),
            (3, 4),
            (3, 5),
            (4, 5),
            (0, 3),
            (1, 4),
            (2, 5),
        ),
        "faces": (
            (0, 1, 2),
            (3, 5, 4),
            (0, 3, 4, 1),
            (1, 4, 5, 2),
            (2, 5, 3, 0),
        ),
    },
}


MODEL_ORDER = ["Cube", "Pyramid", "Prism"]


FACE_COLOURS: List[Colour] = [
    (0.95, 0.35, 0.25),  # warm red-orange
    (0.25, 0.65, 0.95),  # soft blue
    (0.30, 0.85, 0.55),  # green
    (0.95, 0.75, 0.25),  # gold
    (0.70, 0.45, 0.95),  # purple
    (0.25, 0.90, 0.90),  # cyan
]


@dataclass
class AppState:
    model_index: int = 0
    position_x: float = 0.0
    position_y: float = 0.0
    position_z: float = 0.0
    rotation_x: float = 20.0
    rotation_y: float = -30.0
    rotation_z: float = 0.0
    view_mode: str = "normal"


# Loads texture.png using pygame and converts it into an OpenGL texture.
def load_texture(texture_path: str) -> int:
    surface = pygame.image.load(texture_path).convert_alpha()
    surface = pygame.transform.flip(surface, False, True)

    image_data = pygame.image.tostring(surface, "RGBA", True)
    width = surface.get_width()
    height = surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        width,
        height,
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        image_data,
    )

    glBindTexture(GL_TEXTURE_2D, 0)
    return texture_id


# Gives texture coordinates for triangle and rectangle faces.
def texture_coordinates_for_face(face: Face) -> List[Tuple[float, float]]:
    if len(face) == 3:
        return [
            (0.5, 1.0),
            (0.0, 0.0),
            (1.0, 0.0),
        ]

    return [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0),
    ]



# Draws white model edges.
def draw_edges(vertices: Tuple[Vec3, ...], edges: Tuple[Edge, ...]) -> None:
    glDisable(GL_TEXTURE_2D)
    glLineWidth(2)
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)
    for start, end in edges:
        glVertex3fv(vertices[start])
        glVertex3fv(vertices[end])

    glEnd()


# Question 1: draws the model using white edges only.
def draw_wireframe_model(model_name: str) -> None:
    model = MODELS[model_name]

    vertices: Tuple[Vec3, ...] = model["vertices"] #type: ignore
    edges: Tuple[Edge, ...] = model["edges"]  #type: ignore

    draw_edges(vertices, edges)



# Draws the model surfaces.
def draw_surface_model(
    model_name: str,
    mode: str,
    texture_id: int | None = None,
) -> None:
    model = MODELS[model_name]

    vertices: Tuple[Vec3, ...] = model["vertices"]  #type: ignore
    edges: Tuple[Edge, ...] = model["edges"]  #type: ignore
    faces: Tuple[Face, ...] = model["faces"]  #type: ignore

    glDisable(GL_BLEND)
    glEnable(GL_DEPTH_TEST)

    if mode in ("texture", "tinted") and texture_id is not None:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)
    else:
        glDisable(GL_TEXTURE_2D)

    for face_index, face in enumerate(faces):
        face_colour = FACE_COLOURS[face_index % len(FACE_COLOURS)]

        if mode == "normal":
            glColor3f(0.55, 0.55, 0.55)

        elif mode == "colour":
            glColor3f(*face_colour)

        elif mode == "texture":
            glColor3f(1.0, 1.0, 1.0)

        elif mode == "tinted":
            glColor3f(*face_colour)

        glBegin(GL_POLYGON)

        tex_coords = texture_coordinates_for_face(face)

        for vertex_index, tex_coord in zip(face, tex_coords):
            if mode in ("texture", "tinted") and texture_id is not None:
                glTexCoord2f(tex_coord[0], tex_coord[1])

            glVertex3fv(vertices[vertex_index])

        glEnd()

    if mode in ("texture", "tinted") and texture_id is not None:
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

    draw_edges(vertices, edges)



# Moves the camera back and applies translation and rotation.
# The camera is moved backwards so that it is not inside the model.
def apply_camera_and_model_transform(state: AppState) -> None:
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -7.0)

    # Question 2 translation values.
    glTranslatef(state.position_x, state.position_y, state.position_z)

    glRotatef(state.rotation_x, 1.0, 0.0, 0.0)
    glRotatef(state.rotation_y, 0.0, 1.0, 0.0)
    glRotatef(state.rotation_z, 0.0, 0.0, 1.0)



# Clears and redraws the scene.
def draw_scene(
    state: AppState,
    texture_id: int | None = None,
) -> None:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    apply_camera_and_model_transform(state)

    model_name = MODEL_ORDER[state.model_index]

    if state.view_mode == "wire":
        draw_wireframe_model(model_name)
    else:
        draw_surface_model(model_name, state.view_mode, texture_id)



# Handles keyboard input.
# Returns False when the program should close.
def handle_keys(
    event: pygame.event.Event,
    state: AppState,
    allowed_modes: List[str],
) -> bool:
    key = event.key

    movement_step = 0.25
    rotation_step = 7.5

    if key == K_ESCAPE:
        return False

    elif key == pygame.K_m:
        state.model_index = (state.model_index + 1) % len(MODEL_ORDER)
        print(f"Current model: {MODEL_ORDER[state.model_index]}")

    elif key == pygame.K_a:
        state.position_x -= movement_step

    elif key == pygame.K_d:
        state.position_x += movement_step

    elif key == pygame.K_w:
        state.position_y += movement_step

    elif key == pygame.K_s:
        state.position_y -= movement_step

    elif key == pygame.K_z:
        state.position_z -= movement_step

    elif key == pygame.K_x:
        state.position_z += movement_step

    elif key == pygame.K_LEFT:
        state.rotation_y -= rotation_step

    elif key == pygame.K_RIGHT:
        state.rotation_y += rotation_step

    elif key == pygame.K_UP:
        state.rotation_x -= rotation_step

    elif key == pygame.K_DOWN:
        state.rotation_x += rotation_step

    elif key == pygame.K_q:
        state.rotation_z -= rotation_step

    elif key == pygame.K_e:
        state.rotation_z += rotation_step

    elif key == pygame.K_v:
        current_index = allowed_modes.index(state.view_mode)
        next_index = (current_index + 1) % len(allowed_modes)
        state.view_mode = allowed_modes[next_index]
        print(f"View mode: {state.view_mode}")

    elif key == pygame.K_c and "colour" in allowed_modes:
        if state.view_mode == "colour":
            state.view_mode = allowed_modes[0]
        else:
            state.view_mode = "colour"

        print(f"View mode: {state.view_mode}")

    elif key == pygame.K_t and "texture" in allowed_modes:
        if state.view_mode == "texture":
            state.view_mode = allowed_modes[0]
        else:
            state.view_mode = "texture"

        print(f"View mode: {state.view_mode}")

    return True



# Starts the pygame and OpenGL window.

def run_project(
    window_title: str,
    allowed_modes: List[str],
    starting_mode: str,
    needs_texture: bool = False,
) -> None:
    pygame.init()

    display_width = 1000
    display_height = 750

    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(window_title)

    glViewport(0, 0, display_width, display_height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display_width / display_height, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.08, 0.08, 0.10, 1.0)

    texture_id = None

    if needs_texture:
        texture_path = os.path.join(os.path.dirname(__file__), "texture.png")

        if not os.path.exists(texture_path):
            raise FileNotFoundError(
                "texture.png was not found. Run python generate_texture.py first."
            )

        texture_id = load_texture(texture_path)

    state = AppState(view_mode=starting_mode)

    print(window_title)
    print("Controls:")
    print("M = cycle model")
    print("V = cycle view mode")
    print("C = colour view where available")
    print("T = texture view where available")
    print("W/S = move up/down")
    print("A/D = move left/right")
    print("Z/X = move backwards/forwards")
    print("Arrow keys and Q/E = rotate")
    print("ESC = quit")
    print(f"Allowed view modes: {', '.join(allowed_modes)}")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                running = handle_keys(event, state, allowed_modes)

        draw_scene(state, texture_id)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()