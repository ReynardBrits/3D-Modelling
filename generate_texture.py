"""
Creates a custom texture image for Question 4 and Question 5.
"""

import pygame


def create_texture() -> None:
    pygame.init()

    size = 256
    surface = pygame.Surface((size, size))

    # Base background
    background = (35, 35, 45)
    surface.fill(background)

    # Grid colours
    grid_light = (85, 85, 105)
    grid_dark = (55, 55, 70)

    # Draw grid pattern
    grid_size = 32

    for x in range(0, size, grid_size):
        pygame.draw.line(surface, grid_dark, (x, 0), (x, size), 2)

    for y in range(0, size, grid_size):
        pygame.draw.line(surface, grid_dark, (0, y), (size, y), 2)

    # Draw smaller inner grid
    for x in range(0, size, 16):
        pygame.draw.line(surface, grid_light, (x, 0), (x, size), 1)

    for y in range(0, size, 16):
        pygame.draw.line(surface, grid_light, (0, y), (size, y), 1)

    # Add diagonal design lines
    blue = (40, 130, 255)
    orange = (255, 130, 45)

    pygame.draw.line(surface, blue, (0, 0), (size, size), 6)
    pygame.draw.line(surface, orange, (0, size), (size, 0), 6)

    # Add corner circles for visual difference
    pygame.draw.circle(surface, (255, 255, 255), (32, 32), 12)
    pygame.draw.circle(surface, (255, 255, 255), (224, 32), 12)
    pygame.draw.circle(surface, (255, 255, 255), (32, 224), 12)
    pygame.draw.circle(surface, (255, 255, 255), (224, 224), 12)

    pygame.draw.circle(surface, blue, (32, 32), 7)
    pygame.draw.circle(surface, orange, (224, 32), 7)
    pygame.draw.circle(surface, orange, (32, 224), 7)
    pygame.draw.circle(surface, blue, (224, 224), 7)

    # Add simple text to make the texture clearly custom
    font = pygame.font.SysFont("Arial", 28, bold=True)
    text = font.render("ITGDA4", True, (240, 240, 240))
    text_rect = text.get_rect(center=(size // 2, size // 2))
    surface.blit(text, text_rect)

    pygame.image.save(surface, "texture.png")

    pygame.quit()
    print("Custom texture.png created successfully.")


if __name__ == "__main__":
    create_texture()