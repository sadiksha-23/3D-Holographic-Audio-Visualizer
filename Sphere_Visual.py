import pygame
import numpy as np
import sounddevice as sd
import math
import colorsys
import sys

# Draws four pulsating spheres that change color based on audio energy and angle
def draw_sphere_visual(screen, energy, angle):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2  # Center of the screen

    # Boost audio energy for visual effect and limit it to 1.0
    boosted = min(energy * 10, 1.0)

    # Calculate radius of each sphere based on energy
    radius = int(60 + boosted * 100)

    # Smoothly cycle through colors using HSV and rotation angle
    hue = ((angle * 2) % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (int(r * 255), int(g * 255), int(b * 255))  # Convert to RGB 0–255

    # Positions for the spheres around the center (top, bottom, left, right)
    spacing = 250
    positions = [
        (center_x, center_y - spacing),  # Top
        (center_x, center_y + spacing),  # Bottom
        (center_x - spacing, center_y),  # Left
        (center_x + spacing, center_y)   # Right
    ]

    # Draw each sphere at its position with current color and size
    for pos in positions:
        pygame.draw.circle(screen, color, pos, radius)

    return angle + 1.5  # Slightly rotate color for next frame
