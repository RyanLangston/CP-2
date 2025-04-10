import pygame as py
import random


def create_seed():
    """Creates a pseudo-random seed"""
    seed = random.randint(0, 2**32 - 1)
    random.seed(seed)  # Initialize the random number generator with the seed
    return seed


class LinearCongruentialGenerator:
    def __init__(self, seed=None):
        self.seed = seed or random.randint(0, 2**32)

        # LCG parameters
        self.multiplier = 1664525
        self.increment = 1013904223
        self.modulus = 2**32

    def next(self):
        # Generate next pseudo-random number
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        return self.seed / self.modulus

    def range(self, min_val, max_val):
        # Generate random number in specific range
        return min_val + self.next() * (max_val - min_val)


class ProceduralDungeonGenerator:
    def __init__(self, width=50, height=50, seed=None):
        self.width = width
        self.height = height
        self.lcg = LinearCongruentialGenerator(seed)
        self.dungeon_map = [[" " for _ in range(width)] for _ in range(height)]
        self.enemy_positions = []

    def generate_dungeon(self):
        """Generates basic dungeon structures"""
        for y in range(self.height):
            for x in range(self.width):
                noise = self.lcg.next()

                if noise < 0.3:
                    self.dungeon_map[y][x] = "#"
                else:
                    self.dungeon_map[y][x] = "."
                # elif noise < 0.7:
                #     self.dungeon_map[y][x] = '.'
                # else:
                #     self.dungeon_map[y][x]

        # Run a check to ensure borders are walls
        for x in range(self.width):
            self.dungeon_map[0][x] = "#"
            self.dungeon_map[self.height - 1][x] = "#"

        for y in range(self.height):
            self.dungeon_map[y][0] = "#"
            self.dungeon_map[y][self.width - 1] = "#"

    def place_enemies(self, enemy_count=20):
        """Places enemeies"""
        # Clear previous enemy positions
        self.enemy_positions.clear()

        # Place enemies procedurally
        for _ in range(enemy_count):
            attempts = 0
            while attempts < 100:
                x = int(self.lcg.range(1, self.width - 1))
                y = int(self.lcg.range(1, self.height - 1))

                # Only place on floor tiles and also avoid dupes
                if self.dungeon_map[y][x] == "." and (x, y) not in self.enemy_positions:
                    self.enemy_positions.append((x, y))
                    break

    def get_player_spawn_point(self):
        """Calculates and sets a valid spawn point for the player"""
        while True:
            x = int(self.lcg.range(1, self.width - 1))
            y = int(self.lcg.range(1, self.height - 1))

            if self.dungeon_map[y][x] == ".":
                return x, y


class Character(py.sprite.Sprite):
    """Character can be either an enemy or the player"""

    def __init__(self, x, y, char, color: tuple):
        super().__init__()
        self.image = py.Surface((20, 20))
        self.image.fill(color)
        py.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 2)

        # Text Rendering
        font = py.font.SysFont("courier", 15)
        text = font.render(char, True, (0, 0, 0))
        text_rect = text.get_rect(center=(10, 10))
        self.image.blit(text, text_rect)

        # Positioning
        self.rect = self.image.get_rect()
        self.rect.x = x * 20  # Make sure it matches with tile size
        self.rect.y = y * 20
        self.x = x
        self.y = y

        # Base stats
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.speed = 20

        # Combat timing
        self.last_attack_time = 0
        self.attack_cooldown = 1000  # 1 second between attacks

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage

    def can_attack(self):
        """Check if character can attack based on cooldown"""
        current_time = py.time.get_ticks()
        return current_time - self.last_attack_time > self.attack_cooldown

    def is_alive(self):
        """Checks if the character is alive"""
        # Returns a true or false
        return self.health > 0

    def perform_attack(self, target):
        """Perform attack on target"""
        if self.can_attack():
            damage = self.attack
            variance = random.randint(-2, 2)  # Add variance between -2 and 2
            calculated_damage = damage + variance
            dealt_damage = target.take_damage(calculated_damage)
            self.last_attack_time = py.time.get_ticks()
            return dealt_damage
        return 0


class Player(Character):
    """The player class"""

    def __init__(self, x, y):
        super().__init__(x, y, "@", (255, 255, 255))

        # Add player specific customizations
        self.max_health = 150
        self.health = self.max_health
        self.attack = 15
        self.defense = 10
        self.experience = 0
        self.level = 1
        self.inventory = []

    def gain_experience(self, amount):
        """Gain experience and check for level up"""
        self.experience += amount
        if self.experience >= 100 * self.level:
            self.level_up()

    def level_up(self):
        """Increase player stats when leveling up"""
        self.level += 1
        self.max_health += 20
        self.attack += 5
        self.defense += 3
        self.health = self.max_health
        print(f"Level up baby!!!! Now level {self.level}")

    def pickup_item(self, item):
        """Picks up a given item"""
        self.inventory.append(item)


class Enemy(Character):
    """
    The enemy class, currently only goblins
    """

    def __init__(self, x, y):
        super().__init__(x, y, "G", (255, 0, 0))
        # Use LCG for slight stat variation
        lcg = LinearCongruentialGenerator()

        # Enemy specific Customizations
        self.max_health = int(50 + lcg.next() * 20)  # 50 - 70 health
        self.health = self.max_health
        self.attack = random.randint(10, 25)
        self.defense = 8
        self.experience_value = 10

        # Initialize last attack time
        self.last_attack_time = 0


class Game:
    """Game class"""

    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((800, 600))
        py.display.set_caption("Awesome Roguelike")

        # Dungeon Generation
        self.dungeon_generator = ProceduralDungeonGenerator(
            width=50, height=50, seed=create_seed()
        )

        # Generate dungeon layout
        self.dungeon_generator.generate_dungeon()

        # Place enemies
        self.dungeon_generator.place_enemies()

        # Sprite Groups
        self.all_sprites = py.sprite.Group()
        self.enemy_sprites = py.sprite.Group()
        self.wall_sprites = py.sprite.Group()

        # Create Player
        spawn_x, spawn_y = self.dungeon_generator.get_player_spawn_point()
        self.player = Player(spawn_x, spawn_y)
        self.all_sprites.add(self.player)
        self.prev_x, self.prev_y = (
            self.player.rect.x,
            self.player.rect.y,
        )  # Initialize previous position

        # Create enemies
        for ex, ey in self.dungeon_generator.enemy_positions:
            enemy = Enemy(ex, ey)
            self.all_sprites.add(enemy)
            self.enemy_sprites.add(enemy)

        self.clock = py.time.Clock()

        # Combat text
        self.font = py.font.SysFont("courier", 20)
        self.combat_messages = []
        self.in_combat = False

    def draw_dungeon(self):
        """Draws the dungeon to the screen"""
        tile_size = 20
        self.wall_sprites.empty()  # Clear previous wall sprites
        font = py.font.SysFont("courier", 15)
        for y, row in enumerate(self.dungeon_generator.dungeon_map):
            for x, tile in enumerate(row):
                color = (255, 255, 255)  # White color for all tiles
                py.draw.rect(
                    self.screen,
                    color,
                    (x * tile_size, y * tile_size, tile_size, tile_size),
                )
                if tile == "#":
                    wall = py.sprite.Sprite()
                    wall.image = py.Surface((tile_size, tile_size))
                    wall.image.fill(color)
                    wall.rect = wall.image.get_rect()
                    wall.rect.topleft = (x * tile_size, y * tile_size)
                    self.wall_sprites.add(wall)
                    text = font.render("#", True, (0, 0, 0))  # Black ASCII character
                elif tile == ".":
                    text = font.render(".", True, (0, 0, 0))  # Black ASCII character
                elif tile == "+":
                    text = font.render("+", True, (0, 0, 0))  # Black ASCII character
                else:
                    continue
                text_rect = text.get_rect(
                    center=(x * tile_size + 10, y * tile_size + 10)
                )
                self.screen.blit(text, text_rect)

    def handle_wall_collision(self):
        """Prevent player from moving through walls"""
        wall_collisions = py.sprite.spritecollide(self.player, self.wall_sprites, False)
        if wall_collisions:
            # Revert to previous position
            self.player.rect.x = self.prev_x
            self.player.rect.y = self.prev_y

    def handle_combat(self):
        """Handle combat"""
        # This portion was written with ai
        # Check for enemy collisions
        collided_enemies = py.sprite.spritecollide(
            self.player, self.enemy_sprites, False
        )

        if collided_enemies:
            self.in_combat = True  # Set in_combat to True when combat starts
            for enemy in collided_enemies:
                # Player attacks enemy
                player_damage = self.player.perform_attack(enemy)
                if player_damage > 0:
                    message = f"Player deals {player_damage} damage to Goblin!"
                    self.add_combat_message(message)

                # Check if enemy is defeated
                if not enemy.is_alive():
                    message = "Goblin defeated!"
                    self.add_combat_message(message)
                    self.player.gain_experience(enemy.experience_value)
                    self.enemy_sprites.remove(enemy)
                    self.all_sprites.remove(enemy)
                elif enemy.is_alive():
                    # Enemy attacks player
                    enemy_damage = enemy.perform_attack(self.player)
                    if enemy_damage > 0:
                        message = f"Goblin deals {enemy_damage} damage to player"
                        self.add_combat_message(message)

                # Check if player is defeated
                if not self.player.is_alive():
                    message = "Game Over! Player Defeated"
                    self.add_combat_message(message)
                    py.time.wait(2000)
                    py.quit()
                    return

            # End combat turn
            self.in_combat = (
                False  # Reset in_combat to False after combat turn is processed
            )

    def add_combat_message(self, message):
        """Add combat message"""
        print(message)
        self.combat_messages.append(
            {
                "text": message,
                "time": py.time.get_ticks(),
                "duration": 2000,  # Message appears for 2 secs
            }
        )

    def draw_combat_messages(self):
        """Draw combat messages on screen"""
        current_time = py.time.get_ticks()
        y_offset = 10

        # Remove old messages
        self.combat_messages = [
            msg
            for msg in self.combat_messages
            if current_time - msg["time"] < msg["duration"]
        ]

        # Draw remaining messages
        for msg in self.combat_messages:
            text_surface = self.font.render(
                msg["text"], True, (255, 255, 255)
            )  # White text
            self.screen.blit(text_surface, (10, y_offset))
            y_offset += 30

    def run(self):
        running = True
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

            # Movement and combat
            keys = py.key.get_pressed()
            move_speed = 1

            # Handle Combat
            self.handle_combat()

            if not self.in_combat:
                # Store previous position
                self.prev_x, self.prev_y = self.player.rect.x, self.player.rect.y
                if keys[py.K_UP]:
                    self.player.rect.y -= move_speed
                if keys[py.K_DOWN]:
                    self.player.rect.y += move_speed
                if keys[py.K_LEFT]:
                    self.player.rect.x -= move_speed
                if keys[py.K_RIGHT]:
                    self.player.rect.x += move_speed

                # Handle wall collisions
                self.handle_wall_collision()

            # Clear screen
            self.screen.fill((0, 0, 0))  # Black background

            # Draw dungeon
            self.draw_dungeon()

            # Draw sprites
            self.all_sprites.draw(self.screen)

            # Draw Combat messages
            self.draw_combat_messages()

            # Update display
            py.display.flip()
            self.clock.tick(60)  # Control game speed

        py.quit()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
