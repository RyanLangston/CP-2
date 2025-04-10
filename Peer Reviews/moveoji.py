import pygame  # import the pygame Library with all of its bells and whistles

pygame.init()  # initialized the game engine

# FUNCTION DEFINITIONS

# VARIABLE CREATION STATION
eyebrowX = 190
eyebrowSpeed = 1
hairCounter = 0
hairMath = hairCounter % 2
circleY = 230
eyeSPeed = 1
mouthLength = 100
mouthSpeed = 1
mouthX = 300
mouthSP = -1
# COLOR CREATION
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKIN_COLOR = (232, 190, 172)
hair_color = BLACK
SAYIN = (244, 252, 3)
PI = 3.1415926535
# Set up
# Opening the Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE EMOJI! IT MOVES!")


done = False  # Controls the Loop until the user clicks the red x to close the window

clock = (
    pygame.time.Clock()
)  # Used to manage the FRAME RATE, how fast the screen updates

# SET UP COMPLETE

# MAIN PROGRAM LOOP
while not done:
    # 1- Main Event loop
    for event in pygame.event.get():  # Checks the Log for actions
        if event.type == pygame.QUIT:  # If the user clicks the window closed
            done = True  # Flag that we are done, exit the loop

    # 2- GAME LOGIC- Math/Updates
    if eyebrowX == 210 or eyebrowX == 189:
        hairCounter += 1
        if hairMath > 1:
            hair_color == BLACK
        else:
            hair_color == SAYIN
        eyebrowSpeed *= -1
    if circleY == 220 or circleY == 250:
        hairCounter += 1
        if hairMath > 1:
            hair_color == BLACK
        else:
            hair_color == SAYIN
        eyeSPeed *= -1
    if mouthLength == 70 or mouthLength == 130:
        hairCounter += 1
        if hairMath > 1:
            hair_color == BLACK
        else:
            hair_color == SAYIN
        mouthSpeed *= -1

    eyebrowX += eyebrowSpeed
    circleY += eyeSPeed
    mouthLength += mouthSpeed

    # 3- DRAWING THE SCREEN
    screen.fill(WHITE)  # Clears the screen ALWAYS FIRST

    # DRAW EVERYTHING!!!!!

    pygame.draw.circle(screen, SKIN_COLOR, [350, 250], 90)
    pygame.draw.circle(screen, BLACK, [315, circleY], 10)
    pygame.draw.circle(screen, BLACK, [385, circleY], 10)
    pygame.draw.arc(screen, BLACK, [mouthX, 260, mouthLength, 50], 3.3, 0, 5)
    pygame.draw.line(
        screen, BLACK, [300, 200], [330, eyebrowX], 10
    )  # parameters: surface. color, startXY, endXY, width
    pygame.draw.line(
        screen, BLACK, [370, eyebrowX], [400, 200], 10
    )  # parameters: surface. color, startXY, endXY, width
    pygame.draw.polygon(screen, hair_color, [[190, 210], [260, 265], [300, 185]])
    pygame.draw.polygon(screen, hair_color, [[220, 275], [260, 255], [270, 285]])
    pygame.draw.polygon(screen, hair_color, [[290, 190], [315, 165], [200, 190]])
    pygame.draw.polygon(screen, hair_color, [[322, 175], [315, 165], [330, 160]])
    pygame.draw.polygon(screen, hair_color, [[345, 185], [360, 160], [330, 160]])
    pygame.draw.polygon(screen, hair_color, [[367, 175], [360, 160], [375, 165]])

    pygame.display.flip()  # Stamps the drawings to the screen, ALWAYS LAST!

    clock.tick(60)  # Frames per second, 60fps
