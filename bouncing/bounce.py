import pygame as py

# Initialize Engine
py.init()

# Variable Creation
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Image Load
prisonMike = py.image.load("mikey.jpg")
prisonMike.set_colorkey(BLACK)
resized_mike = py.transform.scale(prisonMike, [50, 50])

# Load Background Image
background = py.image.load("bagel.jpg")
background = py.transform.scale(background, [900, 600])

# Audio loading
bounceSound = py.mixer.Sound("homer.mp3")
py.mixer.music.load("never-1.mp3")

# Set up the screen
SIZE = [900, 600]
rect_x = 100
rect_y = 100
speed_x = 2
speed_y = 2
rotation = 0

screen = py.display.set_mode(SIZE)
py.display.set_caption("PRISON MIKE BOUNCEHOUSE")

clock = py.time.Clock()
py.mixer.music.play(-1)

done = False
# Main Program Loop
while not done:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Game Logic -- Math
    rect_x += speed_x
    rect_y += speed_y
    rotation += 1

    if rect_y > 450 or rect_y < 0:
        speed_y *= -1
        bounceSound.play()
    if rect_x > 560 or rect_x < 0:
        speed_x *= -1
        bounceSound.play()

    # Drawing Section
    screen.fill(BLACK)  # Always clear screen first
    screen.blit(background, (0, 0))  # Draw the background image

    # All your Drawing goes here
    rotatedMike = py.transform.rotate(resized_mike, rotation)
    mike_rect = rotatedMike.get_rect(center=(rect_x + 25, rect_y + 25))
    screen.blit(rotatedMike, mike_rect.topleft)
    py.display.flip()

    clock.tick(60)  # FPS

# Be IDLE friendly
py.quit()
