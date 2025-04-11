import pygame
import numpy as np
import sounddevice as sd
import math
import colorsys
import sys 

def create_cube_surface(size, color):
    cube = pygame.Surface((size, size), pygame.SRCALPHA)
    for y in range(size):
        shade = int((y / size) * 80)
        shaded_color = (
            max(min(color[0] - shade, 255), 0),
            max(min(color[1] - shade, 255), 0),
            max(min(color[2] - shade, 255), 0)
        )
        pygame.draw.line(cube, shaded_color, (0, y), (size, y))
    return cube

def draw_cube_visual(screen, energy, angle):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    boosted = min(energy * 10, 1.0)
    base_size = int(80 + boosted * 120)

    hue = (angle % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (int(r * 255), int(g * 255), int(b * 255))

    cube = create_cube_surface(base_size, color)
    rotated_cube = pygame.transform.rotate(cube, angle)

    offset = 200
    positions = [
        (center_x, center_y - offset),
        (center_x, center_y + offset),
        (center_x - offset, center_y),
        (center_x + offset, center_y)
    ]

    for pos in positions:
        screen.blit(rotated_cube, rotated_cube.get_rect(center=pos))

    return angle + 2
