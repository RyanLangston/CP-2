import pygame  # Import's the pygame library
pygame.init()  # initializes the pygame library
# VARIABLE CREATION STATION
blink_y = 40
speed_y = 1
# COLOR CREATION
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (121, 191, 88)
DARKGREEN = (18, 102, 13)
BLUE = (0, 0, 255)
LIGHTBLUE = (135, 206, 250)
BROWN = (184, 139, 55)
YELLOW = (242, 231, 109)
PI = 3.14

# FUNCTION DEFININATIONS


# OPENING THE WINDOW
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Emoji Animation")

# SET UP
done = False # Controls the loop until the user clicks the red x to close the window

clock = pygame.time.Clock() # Used to manage the FRAMERATE, how fast the screen updates

# MAIN PROGRAM LOOP
while not done:
    # MAIN EVENT LOOP
    for event in pygame.event.get(): # Checks the log for actions
        if event.type == pygame.QUIT: # If the user clicks the window closed
            done = True # Flag that we are done, exits the loop

    # GAME LOGIC - Math/Updates
    if blink_y > 205 or blink_y < 195:
        speed_y *= -1

    

    # DRAWING THE SCREEN
    screen.fill(LIGHTBLUE) # Clears the screen EVERY frame

    # DRAW EVERYTHING

   # FACE SHAPE

    pygame.draw.ellipse(screen, YELLOW, [250, 150, 200, blink_y + 160] )


    # MOUTH
    pygame.draw.arc(screen, BLACK, [310, 225, 80, blink_y + 40], (7*PI)/6,(11*PI)/6, 3)


    # EYES
    
    pygame.draw.ellipse(screen, BROWN, [370,205,40, blink_y])
    pygame.draw.ellipse(screen, BROWN, [290,205,40, blink_y]) # Parameters: Surface, color {upperLeftX, upperleftY, width, height}, thickness

    blink_y = blink_y + 0.1








    pygame.display.flip() # Stamps the drawings the the screen

    clock.tick(60) # Frames per second, FPS