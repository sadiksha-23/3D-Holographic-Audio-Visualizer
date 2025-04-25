from AudioInput import *  # Custom audio input class to capture live audio energy
from Visuals import draw_cube_visual, draw_sphere_visual, draw_dots_visual  # Shape drawing functions
from functions import *  # Shared utilities and app_settings
import pygame
import os

# Set the working directory to the script's location (ensures consistency when run from terminal or IDE)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Force default shape and color on startup
# These ensure consistent visualizer state when starting the application
with open("shape.txt", "w") as f:
    f.write("Cube")
with open("color.txt", "w") as f:
    f.write("#FF0000")

# Screen dimensions and frame rate
WIDTH, HEIGHT = 1000, 800
FPS = 60

# Initialize Pygame environment
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Holographic Audio Visualizer")
clock = pygame.time.Clock()

# Start capturing audio energy from microphone or selected input
audio = AudioInput()
audio.start()

angle = 0  # Initial rotation angle for animations

# Function to load runtime settings saved in the GUI
def load_runtime_settings():
    try:
        with open("state_settings.txt", "r") as f:
            lines = f.read().strip().splitlines()
            settings = {
                "animation_speed": float(lines[0]),
                "energy_threshold": float(lines[1]),
                "color_mode": lines[2],
                "detail_level": lines[3]
            }
            return settings
    except Exception as e:
        return None  # If loading fails, fall back to default app_settings

# ========= MAIN GAME LOOP =========
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black background
    energy = audio.get_energy()  # Fetch current audio energy level

    # Get currently selected shape and color
    shape_name = get_saved_shape()
    visual_mode = shape_map.get(shape_name, shape_map["Cube"])  # Convert name to shape code
    color_hex = get_saved_color()
    color = hex_to_rgb(color_hex)  # Convert HEX to RGB tuple

    # Load runtime-adjusted settings (updated via GUI)
    settings = load_runtime_settings()
    if settings:
        animation_speed = settings["animation_speed"]
        energy_threshold = settings["energy_threshold"]
        color_mode = settings["color_mode"]
        detail_level = settings["detail_level"]
    else:
        # Use default or last-known values if file loading fails
        animation_speed = app_settings["animation_speed"]
        energy_threshold = app_settings["energy_threshold"]
        color_mode = app_settings["color_mode"]
        detail_level = app_settings["detail_level"]

    # Handle exit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # If audio energy passes threshold, render the corresponding shape
    if energy >= energy_threshold:
        if visual_mode == 1:
            angle = draw_cube_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold)
        elif visual_mode == 2:
            angle = draw_sphere_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold)
        elif visual_mode == 3:
            angle = draw_dots_visual(screen, energy, angle, color, animation_speed, color_mode, detail_level, energy_threshold)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)  # Maintain consistent frame rate

# Cleanup on exit
audio.stop()
pygame.quit()
