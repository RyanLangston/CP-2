import pygame as py

# Initialize Pygame
py.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Window Settings
size = (700, 500)
screen = py.display.set_mode(size)

# Game Variables
done = False
clock = py.time.Clock()


# Main Program Loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Clear Screen
    screen.fill(WHITE)

    # Update Display
    py.display.flip()
    # Control Frame Rate (60 FPS)
    clock.tick(60)

py.quit()
