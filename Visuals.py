import pygame
import numpy as np
import math
from functions import hex_to_rgb, apply_pulse_color

# Create a visually shaded cube surface
def create_cube_surface(size, color):
    cube = pygame.Surface((size, size), pygame.SRCALPHA)  # Transparent background
    for y in range(size):
        shade = int((y / size) * 80)  # Add vertical gradient shading
        shaded_color = (
            max(min(color[0] - shade, 255), 0),
            max(min(color[1] - shade, 255), 0),
            max(min(color[2] - shade, 255), 0)
        )
        pygame.draw.line(cube, shaded_color, (0, y), (size, y))  # Horizontal shaded lines
    return cube

# Render 3D rotating cube visual
def draw_cube_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    # Boost energy if above threshold
    boosted = 0 if energy < energy_threshold else min(energy * 10, 1.0)

    # Size and rotation speed based on detail level
    if detail_level == "Low":
        base_size = int(60 + boosted * 80)
        breath_scale = 1.0 + 0.05 * math.sin(math.radians(angle * 2))
        base_size = int(base_size * breath_scale)
        angle_step = 1.5
    elif detail_level == "High":
        base_size = int(100 + boosted * 140)
        breath_scale = 1.0 + 0.05 * math.sin(math.radians(angle * 2))
        base_size = int(base_size * breath_scale)
        angle_step = 2.5
    else:
        base_size = int(80 + boosted * 120)
        breath_scale = 1.0 + 0.05 * math.sin(math.radians(angle * 2))
        base_size = int(base_size * breath_scale)
        angle_step = 2.0

    # Apply pulsing color if enabled
    if color_mode == "Pulse":
        color = apply_pulse_color(color, energy)

    cube = create_cube_surface(base_size, color)
    rotated_cube = pygame.transform.rotate(cube, angle)

    # Render four cube copies in a cross layout
    offset = 250
    positions = [
        (center_x, center_y - offset),
        (center_x, center_y + offset),
        (center_x - offset, center_y),
        (center_x + offset, center_y)
    ]

    for pos in positions:
        screen.blit(rotated_cube, rotated_cube.get_rect(center=pos))

    return angle + angle_step * animation_speed  # Animate next angle


# Render animated sphere visuals
def draw_sphere_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    # Boost energy if above threshold
    boosted = 0 if energy < energy_threshold else min(energy * 10, 1.0)

    # Radius controlled by detail level
    if detail_level == "Low":
        radius = int(50 + boosted * 80)
    elif detail_level == "High":
        radius = int(70 + boosted * 120)
    else:
        radius = int(60 + boosted * 100 + 10 * math.sin(math.radians(angle * 2)))  # Wavy effect

    if color_mode == "Pulse":
        color = apply_pulse_color(color, energy)

    # Draw four colored spheres
    spacing = 250
    positions = [
        (center_x, center_y - spacing),
        (center_x, center_y + spacing),
        (center_x - spacing, center_y),
        (center_x + spacing, center_y)
    ]

    breath_scale = 1.0 + 0.05 * math.sin(math.radians(angle * 2))  # add breathing
    scaled_radius = int(radius * breath_scale)

    for pos in positions:
        pygame.draw.circle(screen, color, pos, scaled_radius)

    return angle + 1.5 * animation_speed


# Render dynamic particle-style dots
def draw_dots_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold):
    WIDTH, HEIGHT = screen.get_size()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    fade_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fade_surface.fill((0, 0, 0, 20))  # light black transparent fade
    screen.blit(fade_surface, (0, 0))

    boosted = 0 if energy < energy_threshold else min(energy * 10, 1.0)

    if color_mode == "Pulse":
        color = apply_pulse_color(color, energy)

    spacing = 250
    positions = [
        (center_x, center_y - spacing),
        (center_x, center_y + spacing),
        (center_x - spacing, center_y),
        (center_x + spacing, center_y)
    ]

    # Control number of dots by detail level
    if detail_level == "Low":
        num_dots = int(20 + boosted * 60)
    elif detail_level == "High":
        num_dots = int(40 + boosted * 140)
    else:
        num_dots = int(30 + boosted * 100)

    # Draw dots randomly within a square area around each center point
    for pos in positions:
        for _ in range(num_dots):
            x = pos[0] + np.random.randint(-100, 100)
            y = pos[1] + np.random.randint(-100, 100)
            radius = int(2 + boosted * 4)
            pygame.draw.circle(screen, color, (x, y), radius)

    return angle + 3 * animation_speed
