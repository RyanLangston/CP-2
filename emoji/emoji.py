import pygame as py

py.init()
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Window Settings
size = (700, 500)
screen = py.display.set_mode(size)

# Stuff
done = False

# CLock
clock = py.time.Clock()


# Emoji Function
def emojidraw():
    py.draw.ellipse(screen, BLACK, [20,20,250,100],2)


# Program Loop
while not done:
    # Main Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

        # Game Logic

        # Screen Clearing code
        screen.fill(WHITE)

        # Actual drawing
        emojidraw()

        py.display.flip()

        clock.tick(60)


py.quit()
