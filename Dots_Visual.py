import pygame
import numpy as np
import sounddevice as sd
import math
import colorsys
import sys 
import random

# Draws animated dot bursts around four positions based on audio energy
def draw_dots_visual(screen, energy, angle):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2  # Get center of the screen

    # Boost and clamp the energy for more visual impact
    boosted = min(energy * 10, 1.0)

    # Calculate hue based on angle for smooth rainbow-like color shifting
    hue = ((angle * 5) % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (int(r * 255), int(g * 255), int(b * 255))  # Convert to 0–255 RGB

    # Distance from center to position each cluster of dots
    spacing = 250
    positions = [
        (center_x, center_y - spacing),  # Top
        (center_x, center_y + spacing),  # Bottom
        (center_x - spacing, center_y),  # Left
        (center_x + spacing, center_y)   # Right
    ]

    # Number of dots increases with sound energy
    num_dots = int(30 + boosted * 100)

    # Draw random dots around each position
    for pos in positions:
        for _ in range(num_dots):
            # Randomly scatter each dot within a ±100 pixel range
            x = pos[0] + random.randint(-100, 100)
            y = pos[1] + random.randint(-100, 100)
            radius = int(2 + boosted * 4)  # Dot size also grows with energy
            pygame.draw.circle(screen, color, (x, y), radius)

    return angle + 3  # Increase angle to continuously change color
