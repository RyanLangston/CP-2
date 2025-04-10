import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)


class Rectangle:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.changeX = 2
        self.changeY = 2
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def draw(self):
        pygame.draw.rect(
            screen, (self.r, self.g, self.b), [self.x, self.y, self.width, self.height]
        )

    def move(self):
        self.x += self.changeX
        self.y += self.changeY
        if self.x > 700 - self.width or self.x < 0:
            self.changeX *= -1
        if self.y > 500 - self.height or self.y < 0:
            self.changeY *= -1


class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(
            screen, (self.r, self.g, self.b), [self.x, self.y, self.width, self.height]
        )


pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


done = False


clock = pygame.time.Clock()


myList = []


for i in range(10):
    my_object = Rectangle()
    myOtherObject = Ellipse()
    myList.append(my_object)
    myList.append(myOtherObject)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    for object in myList:
        object.draw()
        object.move()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

"""
abstraction: hide complexity

inheritance: classes can inherit atrributes and methods from other classes



"""
