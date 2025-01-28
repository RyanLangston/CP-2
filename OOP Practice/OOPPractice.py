import pygame as py
from random import randint, choice

# Initialize Engine
py.init()

# Variable Creation
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
SIZE = [1280, 800]


class Rectangle:
    def __init__(self):
        self.x = randint(0, SIZE[0])
        self.y = randint(0, SIZE[1])
        self.height = randint(20, 70)
        self.width = randint(20, 70)
        self.changeX = choice([-3, -2, -1, 1, 2, 3])
        self.changeY = choice([-3, -2, -1, 1, 2, 3])
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)

    def draw(self):
        py.draw.rect(
            screen, [self.r, self.g, self.g], [self.x, self.y, self.width, self.height]
        )

    def move(self):
        self.x += self.changeX
        self.y += self.changeY
        self.changeX += randint(-1, 1)
        self.changeY += randint(-1, 1)
        self.changeX *= choice([-1, 1])
        self.changeY *= choice([-1, 1])

        if self.x > SIZE[0] - self.width or self.x < 0:
            self.changeX *= -1
        if self.y > SIZE[1] - self.height or self.y < 0:
            self.changeY *= -1
        
        # This portionw is ai written, but it essentially reset its value to the center of the screen
        # Which is SIZE // 2
        if self.x > SIZE[0] - self.width or self.x < 0 or self.y > SIZE[1] - self.height or self.y < 0:
            self.x = SIZE[0] // 2
            self.y = SIZE[1] // 2


class Ellipse(Rectangle):
    def draw(self):
        py.draw.ellipse(
            screen, [self.r, self.g, self.b], [self.x, self.y, self.width, self.height]
        )


# The py.scaled and py.doublebuff makes vsync work, which should hopefully prevent some artifacting at higher speeds
screen = py.display.set_mode(SIZE, py.SCALED | py.DOUBLEBUF)

clock = py.time.Clock()

my_list = []

for i in range(50):
    my_object = Rectangle()
    my_other_object = Ellipse()
    my_list.append(my_object)
    my_list.append(my_other_object)


done = False
# Main Program Loop
while not done:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Drawing Section
    screen.fill(BLACK)  # Always clear screen first

    for object in my_list:
        object.draw()
        object.move()

    # All your Drawing goes here
    py.display.flip()

    clock.tick(60)  # FPS

# Be IDLE friendly
py.quit()
