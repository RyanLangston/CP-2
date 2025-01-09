import pygame as py

# Initialize Engine
py.init

# Variable Creation
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
SIZE = [400, 400]

screen = py.display.set_mode(SIZE)
py.display.set_caption("PRISON MIKE BOUNCEHOUSE")

clock = py.time.Clock()

# Main Program Loop
while True:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Game Logic -- Math

    # Drawing Section
    screen.fill(BLACK)  # Always clear screen first

    # All your Drawing goes here
    py.draw.rect(screen, RED, (100, 100, 200, 200))
    py.display.flip()

    clock.tick(60)  # FPS

# Be IDLE friendly
py.quit()
