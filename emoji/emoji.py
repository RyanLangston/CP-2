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

# Emoji Variables
# Position in space
emoji_x = 20 # Initial X Coordinate
emoji_y = 300 # Initial Y Coordinate
emoji_dx = 2 # Horizontal Speed
emoji_dy = 1 # Vertical Speed

# Emoji Function
def emojidraw(x: int,y: int):
    """
    Draw emoji at position (x, y)
    """
    py.draw.ellipse(screen, BLACK, [x,y,250,100],2)


# Program Loop
while not done:
    # Main Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

        # Emoji Position Updating
        emoji_x += emoji_dx
        emoji_y += emoji_dy

        # Check for screen boundaries collision
        if emoji_x + 250 > size[0] or emoji_x < 0:
            emoji_dx *= -1
        # Game Logic

        # Screen Clearing code
        screen.fill(WHITE)

        # Actual drawing
        emojidraw()

        py.display.flip()

        clock.tick(60)


py.quit()
