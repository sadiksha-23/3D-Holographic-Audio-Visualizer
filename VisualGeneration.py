from AudioInput import *
from Cube_Visual import *
from Sphere_Visual import *
from Dots_Visual import *

# Screen and frame rate setup
WIDTH, HEIGHT = 1000, 800
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Launch in full screen
pygame.display.set_caption("3D Holographic Audio Visualizer")
clock = pygame.time.Clock()

# Start audio input
audio = AudioInput()
audio.start()

# Initial state
angle = 0                 # Used for rotating visuals
visual_mode = 1           # Default to cube visual

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))                # Clear screen with black background
    energy = audio.get_energy()          # Get audio energy level

    for event in pygame.event.get():
        # Close program when ESC key is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        # Handle window close button
        elif event.type == pygame.QUIT:
            running = False
        # Handle visual mode switching
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                visual_mode = 1
            elif event.key == pygame.K_2:
                visual_mode = 2
            elif event.key == pygame.K_3:
                visual_mode = 3

    # Render selected visual based on mode
    if visual_mode == 1:
        angle = draw_cube_visual(screen, energy, angle)
    elif visual_mode == 2:
        angle = draw_sphere_visual(screen, energy, angle)
    elif visual_mode == 3:
        angle = draw_dots_visual(screen, energy, angle)

    pygame.display.flip()   # Update the screen
    clock.tick(FPS)         # Maintain consistent frame rate

# Stop audio and quit Pygame
audio.stop()
pygame.quit()
sys.exit()



