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

# Window Settings
size = (1280, 800)
screen = py.display.set_mode(size)

# Game Variables
done = False
clock = py.time.Clock()


class Circle(py.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.color = color
        self.radius = radius
        # We use SRCALPHA to allow for semi transparent objects, allowing for smoother edges
        self.image = py.Surface([self.radius * 2, self.radius * 2], py.SRCALPHA)
        py.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, size[0] - self.radius * 2)
        self.rect.y = random.randint(0, size[1] - self.radius * 2)
        self.speed_x = random.choice([-1, 1] * random.randint(1, 3))
        self.speed_y = random.choice([-1, 1] * random.randint(1, 3))

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.right < 0 or self.rect.left > size[0] or self.rect.bottom < 0 or self.rect.top > size[1]:
            self.kill()
            new_circle = Circle(random.choice([BLUE, GREEN, BLACK]), random.randint(10, 30))
            all_sprites.add(new_circle)
            circles.add(new_circle)

    def reset_pos(self):
        self.rect.y = random.randint(0, size[1])
        self.rect.x = random.randint(0, size[0])
    
    def grow(self, amount):
        """Grows the circle by a set amount"""
        self.radius += amount
        self.image = py.Surface([self.radius * 2, self.radius * 2], py.SRCALPHA)
        py.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.rect.center)

    def respawn(self):
        self.kill()
        new_radius = max(10, min(player.radius * random.uniform(0.5, 1.5), 30))
        new_circle = Circle(random.choice([BLUE, GREEN, BLACK]), new_radius)
        all_sprites.add(new_circle)
        circles.add(new_circle)
        # py.draw.circle(self.image, self.color, (self.radius))

# Create Sprite Groups
all_sprites = py.sprite.Group()
circles = py.sprite.Group()

# Create player circle
player = Circle(RED, 20)
player.rect.center = (size[0] // 2, size[1] // 2)
all_sprites.add(player)

# Create enemy circles
for _ in range(20):
    radius = random.randint(10, 30)
    color = random.choice([BLUE, GREEN, BLACK])
    circle = Circle(color, radius)
    circle.rect.x = random.randint(0, size[0] - radius * 2)
    circle.rect.y = random.randint(0, size[1] - radius * 2)
    all_sprites.add(circle)
    circles.add(circle)

# Main Program Loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

    # Clear Screen
    screen.fill(WHITE)

    # Update player pos
    pos = py.mouse.get_pos()
    player.rect.center = pos

    all_sprites.update()

    # Check for collisions
    collided_circles = py.sprite.spritecollide(player, circles, False, py.sprite.collide_circle)
    for circle in collided_circles:
        if player.radius > circle.radius:
            player.grow(circle.radius // 2)
            circle.respawn()
        else:
            done = True

    all_sprites.draw(screen)

    # Update Display
    py.display.flip()
    # Control Frame Rate (60 FPS)
    clock.tick(40)

py.quit()
