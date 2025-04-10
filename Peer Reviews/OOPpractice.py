import pygame as py
import random as r

# Initialize engine
py.init()

# Variables
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# classes
class Basta_fazoolin:
    def __init__(self):
        self.x = r.randint(0, 700)
        self.y = r.randint(0, 500)
        self.height = r.randint(1, 50)
        self.width = r.randint(1, 50)
        self.changeX = r.randint(-1, 1)
        self.changeY = r.randint(-1, 1)
        self.r = r.randint(0, 205)
        self.g = r.randint(0, 205)
        self.b = r.randint(0, 205)

    def draw(self):
        py.draw.rect(
            screen, [self.r, self.g, self.b], [self.x, self.y, self.width, self.height]
        )
        py.draw.rect(
            screen,
            [self.r + 50, self.g + 50, self.b + 50],
            [
                self.x + (self.width / 10),
                self.y + (self.height / 10),
                self.width - (self.width * 0.2),
                self.height - (self.height * 0.2),
            ],
        )

    def move(self):
        self.x += self.changeX
        self.y += self.changeY

        if self.x >= 700 - self.width or self.x <= 0:
            self.changeX *= -1
        if self.y >= 500 - self.height or self.y <= 0:
            self.changeY *= -1


class Ellipse(Basta_fazoolin):
    def draw(self):
        py.draw.ellipse(
            screen, [self.r, self.g, self.b], [self.x, self.y, self.width, self.height]
        )
        py.draw.ellipse(
            screen,
            [self.r + 50, self.g + 50, self.b + 50],
            [
                self.x + (self.width / 10),
                self.y + (self.height / 10),
                self.width - (self.width * 0.2),
                self.height - (self.height * 0.2),
            ],
        )


obj_list = []

for i in range(r.randint(100, 300)):
    rectangle = Basta_fazoolin()
    ellipse = Ellipse()
    obj_list.append(rectangle)
    obj_list.append(ellipse)
# set up screen
SIZE = [700, 500]
screen = py.display.set_mode(SIZE)
py.display.set_caption("Shape Factory")
done = False

clock = py.time.Clock()

# _______Main Program Loop_______
while not done:
    # Event Loop_____________
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Game Logic -- Math

    # Drawing section -- What goes on screen
    screen.fill(BLACK)  # Always clear the screen
    for object in obj_list:
        object.draw()
        object.move()

    # The rest of the screen drawing

    py.display.flip()

    clock.tick(60)

py.quit()
