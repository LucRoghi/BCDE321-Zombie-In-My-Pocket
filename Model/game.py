"""

"""

import random
from pathlib import Path
from PIL import Image
from Model.game_data import GameData
from Model.player import Player


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.active_tile_list = self.game_data.map_tiles_indoor
        self.player = Player()
        self.time_list = ["time_nine", "time_ten", "time_eleven"]
        self.current_time = 0
        self.last_action = None
        self.current_dev_card = None
        self.current_tile = None
        self.previous_direction = None
        self.start_game()

    def start_game(self):
        """
        Starts the game by removing 2 development cards from the pile and
        setting the player at the foyer
        :return:
        """
        self.player.current_location = self.active_tile_list.pop(-1)

    @staticmethod
    def end_game():
        print("YOU HAVE LOST THE GAME. Returning to main menu")

    def new_dev_card_deck(self):
        self.game_data.dev_cards = self.game_data.get_dev_cards()
        self.game_data.dev_card_pop()
        self.game_data.dev_card_pop()

    def move_player(self, direction):
        move_player_functions = {"up": self.player.move_player_up,
                                 "right": self.player.move_player_right,
                                 "down": self.player.move_player_down,
                                 "left": self.player.move_player_left}
        try:
            move_player_functions[direction]()
            self.print_player_info()
            self.draw_new_dev_card()
            self.execute_current_dev_card()
        except (ValueError, KeyError) as e:
            print(e)
            print("Place a new tile to an available door to be able to navigate")

    def update_last_direction(self, direction):
        opposite_direction_dict = {"up": "down",
                                   "left": "right",
                                   "down": "up",
                                   "right": "left"}
        self.previous_direction = opposite_direction_dict[direction]

    def update_time(self):
        self.current_time += 1
        self.new_dev_card_deck()

    def break_open_wall(self, direction):
        try:
            break_wall_direction = {"up": self.player.current_location.door_up,
                                    "left": self.player.current_location.door_left,
                                    "right": self.player.current_location.door_right,
                                    "down": self.player.current_location.door_down}
            if not break_wall_direction[direction]:
                break_wall_direction[direction] = True
                self.player.current_location.zombie_number += 3
                print("You break open a wall but attract 3 zombies to you")
            else:
                raise ValueError("Cannot break open a wall where a door is")
        except ValueError as e:
            print(e)

    def player_attack(self):
        zombie_number = self.player.current_location.zombie_number
        self.player.health = self.player.health - (zombie_number - self.player.attack)
        self.player.current_location.zombie_number -= self.player.attack
        if self.player.current_location.zombie_number < 0:
            self.player.current_location.zombie_number = 0
        if self.player.health <= 0:
            self.end_game()

    def player_flee(self):
        print(f"You flee from {self.player.current_location.room_name} but get hit on the way. Lose 1 health")
        self.move_player(self.previous_direction)
        self.player.health -= 1

    def player_cower(self):
        print(f"You cower in fear. You gain 3 health but lose some time")
        self.game_data.dev_card_pop()
        self.player.health += 3

    def print_player_info(self):
        print(f"PLAYER INFO: \n"
              f"Current Location: {self.player.current_location.room_name} \n"
              f"{self.player.current_location.print_doors()} \n"
              f"Player Health: {self.player.health} \n"
              f"Player Attack: {self.player.attack} \n"
              f"Current Time: {self.current_time + 9}")

    def draw_new_dev_card(self):
        try:
            if len(self.game_data.dev_cards) > 0:
                self.current_dev_card = self.game_data.dev_card_pop()
            else:
                self.update_time()
        except IndexError as e:
            print(e)

    def execute_current_dev_card(self):
        message, effect = getattr(self.current_dev_card, self.time_list[self.current_time])
        action_functions = {"get_new_item": self.get_new_item,
                            "lose_1_health": self.lose_1_health,
                            "add_1_health": self.add_1_health}
        if effect == "None":
            print(message)
        elif effect.isnumeric():
            self.player.current_location.zombie_number += int(effect)
            print(f"{effect} Zombies have entered the room. What do you do? (Attack or Flee)")
            self.print_player_info()
        else:
            if message != "None":
                print(message)
            action_functions[effect]()

    def get_new_item(self):
        self.draw_new_dev_card()
        for item in self.game_data.items:
            if item.name == self.current_dev_card.item:
                self.player.inventory.append(item)
                print(f"You find a {item.name} in the room")
                break

    def drop_item(self, item_name):
        try:
            for item in self.player.inventory:
                if item.name == item_name:
                    self.player.inventory.pop(item)
                    break
                else:
                    raise ValueError(f"Item {item_name} is not in the players inventory")
        except ValueError as e:
            print(e)

    def lose_1_health(self):
        print("You lose 1 health")
        self.player.health -= 1

    def add_1_health(self):
        print("You gain 1 health")
        self.player.health += 1

    def draw_new_tile(self):
        try:
            random_index = random.randint(0, len(self.active_tile_list) - 1)
            self.current_tile = self.active_tile_list.pop(random_index)
        except IndexError as e:
            print(e)

    def attach_new_tile(self, direction):
        try:
            tile = self.current_tile
            direction = direction.lower()
            attach_new_tile_functions = {"up": self.player.current_location.add_new_room_up(tile),
                                         "right": self.player.current_location.add_new_room_right(tile),
                                         "down": self.player.current_location.add_new_room_down(tile),
                                         "left": self.player.current_location.add_new_room_left(tile)}
            if not attach_new_tile_functions[direction]:
                raise ValueError("Tile cannot be placed. Either a room already exists or no door can be connected")
            print(f"Attached tile {self.player.current_location.room_name} to "
                  f"{self.current_tile.room_name} going {direction}")
            self.current_tile = None
            self.print_player_info()
        except (ValueError, KeyError) as e:
            print(e)

    def rotate_tile(self, direction):
        if direction == "left":
            self.current_tile.rotate_tile_left()
        elif direction == "right":
            self.current_tile.rotate_tile_right()

    def print_tile(self, direction):
        try:
            image_ref_dict = {"here": self.player.current_location,
                              "drawn": self.current_tile,
                              "up": self.player.current_location.room_up,
                              "left": self.player.current_location.room_left,
                              "down": self.player.current_location.room_down,
                              "right": self.player.current_location.room_right}
            root_dir = Path(__file__).parent.parent
            img = Image.open(f"{root_dir}/Data/TileImages/{image_ref_dict[direction].room_name}.png")
            img.show()
        except (FileNotFoundError, AttributeError):
            print("There is no room to look into")


if __name__ == "__main__":
    new_game = Game()
    new_game.draw_new_tile()
    print(new_game.player.current_location.room_name)
    new_game.attach_new_tile("up")
    new_game.move_player("up")
    print(new_game.player.current_location.room_name)
