from AudioInput import *
from Cube_Visual import *
from Sphere_Visual import *
from Dots_Visual import *

# === Setup ===
WIDTH, HEIGHT = 800, 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Holographic Audio Visualizer")
clock = pygame.time.Clock()

# === Audio ===
audio = AudioInput()
audio.start()

# === State ===
angle = 0
visual_mode = 1  # Start with cube

# === Main Loop ===
running = True
while running:
    screen.fill((0, 0, 0))
    energy = audio.get_energy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                visual_mode = 1
            elif event.key == pygame.K_2:
                visual_mode = 2
            elif event.key == pygame.K_3:
                visual_mode = 3

    # === Draw Selected Visual ===
    if visual_mode == 1:
        angle = draw_cube_visual(screen, energy, angle)
    elif visual_mode == 2:
        angle = draw_sphere_visual(screen, energy, angle)
    elif visual_mode == 3:
        angle = draw_dots_visual(screen, energy, angle)

    pygame.display.flip()
    clock.tick(FPS)

# === Cleanup ===
audio.stop()
pygame.quit()
sys.exit()


