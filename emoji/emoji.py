import pygame as py
import random
import math

py.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window Settings
size = (700, 500)
screen = py.display.set_mode(size)

# Game Variables
done = False
clock = py.time.Clock()

# Emoji Variables
emoji_x = 150  # Center x-coordinate of the circle
emoji_y = 250  # Center y-coordinate of the circle
emoji_radius = 100  # Radius of the circle
emoji_dx = 2  # Horizontal speed
# Snow Variablekks
# Will create 50 random snowflakes
snowflakes = [
    {"x": random.randint(0, size[0]), "y": random.randint(-500, 0)} for _ in range(50)
]
snow_speed = 2


# Emoji Drawing Function
def emojidraw():
    """
    Draws an emoji with eyes and a simple smile
    """
    # Draw face
    py.draw.circle(screen, BLACK, (emoji_x, emoji_y), emoji_radius, 2)

    # Draw eyes
    eye_radius = 10
    left_eye_x = emoji_x - 30  # Left eye offset from center
    right_eye_x = emoji_x + 30  # Right eye offset from center
    eye_y = emoji_y - 20  # Eyes slightly above center
    py.draw.circle(screen, BLACK, (left_eye_x, eye_y), eye_radius)  # Left eye
    py.draw.circle(screen, BLACK, (right_eye_x, eye_y), eye_radius)  # Right eye

    # Draw smile
    smile_rect = py.Rect(emoji_x - 50, emoji_y + 20, 100, 50)  # Smile bounding box
    py.draw.arc(screen, BLACK, smile_rect, math.pi / 8, math.pi - math.pi / 8, 2)


# Snow Drawing Function
def drawsnow():
    """
    Draws falling snow on the screen.
    """
    for flake in snowflakes:
        py.draw.circle(
            screen, BLACK, (flake["x"], flake["y"]), 3
        )  # Small black snowflake


# Main Program Loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Update Emoji Position
    emoji_x += emoji_dx

    # Collision Checking for Horizontal Movement
    if emoji_x + emoji_radius > size[0]:  # Right edge collision
        emoji_x = size[0] - emoji_radius
        emoji_dx *= -1

    if emoji_x - emoji_radius < 0:  # Left edge collision
        emoji_x = emoji_radius
        emoji_dx *= -1

    # Update Snow Position
    for flake in snowflakes:
        flake["y"] += snow_speed

        # Reset snowflake when it goes off-screen
        if flake["y"] > size[1]:
            flake["y"] = random.randint(-50, -10)  # Reset above screen
            flake["x"] = random.randint(0, size[0])  # Random horizontal position

    # Clear Screen
    screen.fill(WHITE)

    # Draw Emoji and Snowflakes
    emojidraw()
    drawsnow()

    # Update Display
    py.display.flip()

    # Control Frame Rate (60 FPS)
    clock.tick(60)

py.quit()
