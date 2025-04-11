import pygame
import numpy as np
import sounddevice as sd
import math
import colorsys
import sys 

def draw_sphere_visual(screen, energy, angle):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    boosted = min(energy * 10, 1.0)
    radius = int(60 + boosted * 100)

    hue = ((angle * 2) % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (int(r * 255), int(g * 255), int(b * 255))

    offset = 200
    positions = [
        (center_x, center_y - offset),
        (center_x, center_y + offset),
        (center_x - offset, center_y),
        (center_x + offset, center_y)
    ]

    for pos in positions:
        pygame.draw.circle(screen, color, pos, radius)

    return angle + 1.5
