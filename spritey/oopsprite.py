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
info = py.display.Info()
screen_width = info.current_w
screen_height = info.current_h
size = (screen_width, screen_height)
screen = py.display.set_mode(size)

# Game Variables
done = False
clock = py.time.Clock()

def random_color():
    """Generate a random color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Circle(py.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.color = color
        self.radius: float = float(radius)
        self.image = py.Surface([self.radius * 2, self.radius * 2], py.SRCALPHA)
        py.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.uniform(float(0), float(size[0]) - float(self.radius * 2))
        self.rect.y = random.uniform(float(0), float(size[1]) - float(self.radius * 2))
        self.speed_x = random.choice([-1, 1]) * random.randint(3, 6)
        self.speed_y = random.choice([-1, 1]) * random.randint(3, 6)

    def update(self):
        """Updates stuff"""
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.right < 0 or self.rect.left > size[0] or self.rect.bottom < 0 or self.rect.top > size[1]:
            self.respawn()

    def reset_pos(self):
        """Resets the position"""
        self.rect.y = random.randint(0, size[1])
        self.rect.x = random.randint(0, size[0])
    
    def grow(self, amount):
        """Grows the circle by a set amount"""
        self.radius += amount
        self.image = py.Surface([self.radius * 2, self.radius * 2], py.SRCALPHA)
        py.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.rect.center)

    def respawn(self):
        """Respawns enemy circles"""
        self.kill()
        min_radius = max(10, player.radius * 0.8)
        max_radius = player.radius * 2  # Allow new circles to be up to twice the player's size
        new_radius = random.uniform(min_radius, max_radius)
        new_color = random_color()
        new_circle = Circle(new_color, new_radius)
        # Respawn offscreen
        if random.choice([True, False]):
            new_circle.rect.x = random.choice([-new_circle.radius * 2, size[0] + new_circle.radius * 2])
            new_circle.rect.y = random.uniform(0, size[1])
        else:
            new_circle.rect.y = random.choice([-new_circle.radius * 2, size[1] + new_circle.radius * 2])
            new_circle.rect.x = random.uniform(0, size[0])
        new_circle.speed_x = random.choice([-1, 1]) * random.randint(3, 6 + int(player.radius / 10))
        new_circle.speed_y = random.choice([-1, 1]) * random.randint(3, 6 + int(player.radius / 10))
        all_sprites.add(new_circle)
        circles.add(new_circle)

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
    base_color = random.choice([BLUE, GREEN, BLACK])
    color = random_color()
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
            player.grow(3)
            circle.respawn()
        else:
            done = True

    all_sprites.draw(screen)

    # Update Display
    py.display.flip()
    # Control Frame Rate (60 FPS)
    clock.tick(60)

py.quit()
