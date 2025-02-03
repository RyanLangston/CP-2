import pygame as py
import random

# Initialize Pygame
py.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Classes
class Block(py.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) Constructor
        super().__init__()
        # Set background color and set it to be transparent
        self.image = py.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw an ellipse
        py.draw.ellipse(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()


# Window Settings
# SIZE = (700, 500)
screen_width = 700
screen_height = 500
screen = py.display.set_mode([screen_width, screen_height])

# Game Variables
done = False
clock = py.time.Clock()

# Make a list of block sprites
block_list = py.sprite.Group()

# Make a list of all sprites
all_sprites_list = py.sprite.Group()

# Bad guy blocks
for i in range(50):
    block = Block(BLACK, 20, 15)

    # Set random location for block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of block
    block_list.add(block)
    all_sprites_list.add(block)

# Good guy blokc
player = Block(RED, 20, 15)
all_sprites_list.add(player)

score: int = 0

# Main Program Loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Clear Screen
    screen.fill(WHITE)
    # Get current mouse position
    pos = py.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything
    blocks_hit_list = py.sprite.spritecollide(player, block_list, True)

    # Check the list of collisions
    for block in blocks_hit_list:
        score += 1
        print(score)

    all_sprites_list.draw(screen)

    # Update Display
    py.display.flip()
    # Control Frame Rate (60 FPS)
    clock.tick(60)

py.quit()
