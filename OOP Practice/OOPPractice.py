# THIS IS SOOOOO COOOOOL

import pygame as py
import random

# Initialize Engine
py.init()

# Variable Creation
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Rectangle:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)

    def draw(self):
        py.draw.rect(screen, GREEN, [self.x, self.y, 10, 10])


# Set up the screen
SIZE = [900, 600]

screen = py.display.set_mode(SIZE)

clock = py.time.Clock()

my_object = Rectangle()

done = False
# Main Program Loop
while not done:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Drawing Section
    screen.fill(BLACK)  # Always clear screen first

    # All your Drawing goes here
    py.display.flip()

    clock.tick(60)  # FPS

# Be IDLE friendly
py.quit()
