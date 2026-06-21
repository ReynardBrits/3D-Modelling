"""
Creates texture.png for Question 4 and Question 5.
I am using pygame-ce and not pillow, because I had issues with pillow and I am more familiar with pygame.
"""

import pygame


def create_texture() -> None:
    pygame.init()

    size = 256
    block = 32

    surface = pygame.Surface((size, size))

    light = (230, 230, 230)
    dark = (80, 80, 80)
    blue = (30, 120, 255)
    red = (255, 80, 80)

    for y in range(0, size, block):
        for x in range(0, size, block):
            if (x // block + y // block) % 2 == 0:
                colour = light
            else:
                colour = dark

            pygame.draw.rect(surface, colour, (x, y, block, block))

    pygame.draw.line(surface, blue, (0, 0), (size, size), 8)
    pygame.draw.line(surface, red, (0, size), (size, 0), 8)

    pygame.image.save(surface, "texture.png")

    pygame.quit()
    print("texture.png created successfully.")


if __name__ == "__main__":
    create_texture()