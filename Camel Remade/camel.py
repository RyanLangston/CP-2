from random import randint


class Player:
    """The player"""

    def __init__(self):
        self.thirst = 0
        self.canteen = 4
        self.distance_traveled = 0

    def drink(self):
        """Player drinks from canteen"""
        if self.thirst > 0:
            if self.canteen != 0:
                # Resets players thirst
                self.thirst = 0
            else:
                print("Your canteen is empty")
        else:
            print("You aren't thirsty")

    def increase_thirst(self):
        self.thirst += 1

    def movement(self, speed: int):
        """Handles player movement"""
        if speed == 1:
            # Move at a moderate speed
            self.distance_traveled += randint(5, 12)
        if speed == 2:
            # Move at full speed
            self.distancce_traveled += randint(10, 20)


class Camel:
    """Camels stats"""

    def __init__(self):
        # exhaustion = self.exhuastion
        self.exhaustion = 0

    def reset_exhaustion(self):
        self.exhaustion = 0
        print("Your camel has rested")

    def increase_exhaustion(self, increase: int):
        """Increases camels exhaustion level"""
        self.exhaustion += increase


class Natives:
    def __init__(self):
        self.distance_traveled = -13

    def move(self):
        """The natives always move the same distance regardless"""
        self.distance_traveled += randint(7, 14)


class Game:
    """The main games logic and state"""

    def __init__(self):
        print("Welcome to the super sweet camel game")
        self.game_over = False
        self.win = False
        self.camel = Camel()
        self.player = Player()
        self.natives = Natives()

    def check_game_status(self):
        """Checks game condition and see if player has failed"""
        if self.camel.exhaustion > 5:
            self.game_over = True
            print("Your camel is too tired and you die of exhaustion")
        elif self.player.thirst > 4:
            self.game_over = True
            print("You die of thirst")
        elif self.player.distance_traveled >= 200:
            self.game_over = True
            self.win = True
            print("YOU WON!!! LESSS GOOOO")

    def print_options(self):
        print("\nChoose an action:")
        print("1. Drink from your canteen")
        print("2. Ahead Moderate Speed")
        print("3. Ahead Full speed")
        print("4. Stop for the night")
        print("5. Status check")
        print("6. Quit\n")

    def every_round(self):
        """Stuff that runs every single game loop regardless"""
        self.natives.move()

    def handle_player_choice(self, choice):
        """Handles the players choice."""
        if choice == 1:
            self.player.drink()
        # Need to use an if statement again so that we can make rounds work correctly
        elif choice == 2:
            self.player.movement(1)
            self.every_round()
        elif choice == 3:
            self.player.movement(2)
            self.every_round()

    def check_status(self):
        """Allows the player to see stats"""
        print("\nThirst: " + self.player.thirst)
        print("\nDistance traveled: " + self.player.distance_traveled)
        print("\nNatives Distance Traveled" + self.natives.distance_traveled)

    def play(self):
        while not self.game_over:
            self.print_options()
            try:
                choice = int(input("Your choice? "))
                if choice < 1 or choice > 6:
                    # Uses proper python syntax for error handling
                    # ValueError is just a basic method of error handling
                    raise ValueError("Invalid choice")
                self.handle_player_choice(choice)
            except ValueError:
                print("Invalid input, please enter a number between 1 and 6")
            self.handle_player_choice(choice)
            self.check_game_status()


game = Game()
game.play()
