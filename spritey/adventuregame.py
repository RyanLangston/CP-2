import pygame as py
import random

class Character(py.sprite.Sprite):
    """Character can be either an enemy or the player"""
    def __init__(self, x, y, char, color: tuple):
        super().__init__()
        self.image = py.Surface((20, 20))
        self.image.fill(color)
        py.draw.rect(self.image, (0,0,0), self.image.get_rect(), 2)

        # Text Rendering
        font = py.font.SysFont('courier', 15)
        text = font.render(char, True, (0,0,0))
        text_rect = text.get_rect(center=(10,10))
        self.image.blit(text, text_rect)
        
        
        # Positioning
        self.x = x
        self.y = y

        # Base stats
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.speed = 20
    
    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage

    def is_alive(self):
        """Checks if the character is alive"""
        # Returns a true or false
        return self.health > 0

    def attack_target(self, target):
        damage = self.attack
        return target.take_damage(damage)
    

class Player(Character):
    """The player class"""        
    def __init__(self, x, y):
        super().__init__(x, y, '@', (255,255,255))

        # Add player specific customizations
        self.max_health = 150
        self.health = self.max_health
        self.attack = 15
        self.defense = 10
        self.inventory = []

    
    def pickup_item(self, item):
        """Picks up a given item"""
        self.inventory.append(item)
    

class Enemy(Character):
    """
    The enemy class, currently only goblins
    """
    def __init__(self, x, y):
        super().__init__(x, y, 'G', (255, 0, 0))
        
        # Enemy specific Customizations
        self.max_health = 50
        self.health = self.max_health
        self.attack = 5
        self.defense = 2
        self.experience_value = 10


class Game:
    """Game class"""
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((800, 600))
        py.display.set_caption("Awesome Roguelike")

        # Sprite Groups
        self.all_sprites = py.sprite.Group()
        self.enemy_sprites = py.sprite.Group()

        # Create Player
        self.player = Player(5, 5)
        self.all_sprites.add(self.player)

        # Create enemies
        # TODO: Add to dungeon procedural generation logic

    def handle_combat(self):
        """Handles combat by checking collisions"""
        collided_enemies = py.sprite.spritecollide(self.player, self.enemy_sprites, True)

        for enemy in collided_enemies:
            damage_dealt = self.player.attack_target(enemy)
            print(f"Player dealt {damage_dealt} damage!")

            if not enemy.is_alive():
                print("Enemy defeated!")
            
    def run(self):
        running = True
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

            # Movement and combat
            keys = py.key.get_pressed()
            if keys[py.K_UP]:
                self.player.rect.y -= self.player.speed
            if keys[py.K_DOWN]:
                self.player.rect.y += self.player.speed
            if keys[py.K_LEFT]:
                self.player.rect.x -= self.player.speed
            if keys[py.K_RIGHT]:
                self.player.rect.x += self.player.speed

            self.handle_combat()

            # Drawing
            self.screen.fill((200,200,200))
            self.all_sprites.draw(self.screen)
            py.display.flip()

            self.clock.tick(10)  # Control game speed

        py.quit()