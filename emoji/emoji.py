import pygame as py
import random
import math
# Note for teacher, primary notes on ai usage is just in the readme, I believe vscode should allow for the proper display of it, if not
# use this link https://github.com/Dragonlord1005/CP-2/tree/main/emoji

# Initialize Pygame
py.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window Settings
size = (700, 500)
screen = py.display.set_mode(size)
py.display.set_caption("Emoji with Simplified Snow Animation")

# Game Variables
done = False
clock = py.time.Clock()

# Emoji Variables
emoji_x = 150  # Center x-coordinate of the circle
emoji_y = 250  # Center y-coordinate of the circle
emoji_radius = 100  # Radius of the circle
emoji_dx = 2  # Horizontal speed

# Snow Variables
snow_list = []  # List to store snowflakes

# Initialize snowflakes at random positions
for i in range(50):
    x = random.randrange(0, size[0])  # Random x-coordinate within screen width
    y = random.randrange(
        -500, size[1]
    )  # Random y-coordinate above or within screen height
    snow_list.append([x, y])  # Append as [x, y] pair


# Emoji Drawing Function
def emojidraw():
    """
    Draws an emoji with eyes and a simple smile.
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
    # Smile was done with help from ai, as pi is stupid
    smile_rect = py.Rect(emoji_x - 50, emoji_y + 20, 100, 50)  # Smile bounding box
    py.draw.arc(
        screen,
        BLACK,
        smile_rect,
        math.pi / 8,
        math.pi - math.pi / 8,
        2,
    )


# Main Program Loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Update Emoji Position
    emoji_x += emoji_dx

    # Collision Checking for Horizontal Movement
    # Initial collision checking had overshot issues, ai led me to this solution, which I understand
    if (
        emoji_x + emoji_radius > size[0]
    ):  # Right edge collision by checking against radius
        emoji_x = size[0] - emoji_radius
        emoji_dx *= -1  # Reverse direction

    if emoji_x - emoji_radius < 0:  # Left edge collision
        emoji_x = emoji_radius  # Set to radius
        emoji_dx *= -1  # Reverse Direction

    # Snowflake Positions
    for i in range(len(snow_list)):
        snow_list[i][1] += 2  # Move each snowflake down by speed of 2 pixels

        # Reset snowflake when it goes off-screen
        if snow_list[i][1] > size[1]:
            snow_list[i][1] = random.randrange(-50, -10)  # Reset above screen
            snow_list[i][0] = random.randrange(0, size[0])  # Random horizontal position

    # Clear Screen
    screen.fill(WHITE)

    # Draw Emoji and Snowflakes
    emojidraw()

    for i in range(len(snow_list)):
        py.draw.circle(
            screen, BLACK, snow_list[i], 3
        )  # Draw each snowflake as a small black circle

    # Update Display
    py.display.flip()

    # Control Frame Rate (60 FPS)
    clock.tick(60)

py.quit()
