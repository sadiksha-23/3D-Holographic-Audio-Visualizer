import pygame
import numpy as np
import sounddevice as sd
import math
import colorsys
import sys 
import random

def draw_dots_visual(screen, energy, angle):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    boosted = min(energy * 10, 1.0)

    hue = ((angle * 5) % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (int(r * 255), int(g * 255), int(b * 255))

    offset = 200
    positions = [
        (center_x, center_y - offset),
        (center_x, center_y + offset),
        (center_x - offset, center_y),
        (center_x + offset, center_y)
    ]

    num_dots = int(30 + boosted * 100)

    for pos in positions:
        for _ in range(num_dots):
            x = pos[0] + random.randint(-100, 100)
            y = pos[1] + random.randint(-100, 100)
            radius = int(2 + boosted * 4)
            pygame.draw.circle(screen, color, (x, y), radius)

    return angle + 3