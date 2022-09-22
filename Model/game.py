"""

"""
import random

from Model.game_data import GameData
from Model.player import Player


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.active_tile_list = self.game_data.map_tiles_indoor
        self.player = Player()
        self.time = 9
        self.last_action = None
        self.current_dev_card = None
        self.current_tile = None
        self.start_game()

    def start_game(self):
        """
        Starts the game by removing 2 development cards from the pile and
        setting the player at the foyer
        :return:
        """
        self.player.current_location = self.active_tile_list.pop(-1)

    def move_player(self, direction):
        move_player_functions = {"up": self.player.move_player_up,
                                 "right": self.player.move_player_right,
                                 "down": self.player.move_player_down,
                                 "left": self.player.move_player_left}
        try:
            move_player_functions[direction]()
            print(f"Current location is {self.player.current_location.room_name}")
        except (ValueError, KeyError) as e:
            print(e)

    def player_attack(self):
        zombie_number = self.player.current_location.zombie_number
        self.player.health = self.player.health - (zombie_number - self.player.attack)
        self.player.current_location.zombie_number -= self.player.attack
        if self.player.current_location.zombie_number < 0:
            self.player.current_location.zombie_number = 0
        if self.player.health <= 0:
            print("YOU HAVE DIED")

    def player_flee(self, direction):
        self.move_player(direction)
        self.player.health -= 1

    def player_cower(self):
        self.game_data.dev_card_pop()
        self.player.health += 3

    def draw_new_dev_card(self):
        try:
            self.current_dev_card = self.game_data.dev_card_pop()
            return self.current_dev_card
        except IndexError as e:
            print(e)

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
            attach_new_tile_functions[direction]
            print(f"Attached tile {self.player.current_location.room_name} to "
                  f"{self.current_tile.room_name} going {direction}")
            self.current_tile = None
        except (ValueError, KeyError) as e:
            print(e)

    def rotate_tile(self, direction):
        if direction == "left":
            self.current_tile.rotate_tile_left()
        elif direction == "right":
            self.current_tile.rotate_tile_right()


if __name__ == "__main__":
    new_game = Game()
    new_game.draw_new_tile()
    print(new_game.player.current_location.room_name)
    new_game.attach_new_tile("up")
    new_game.move_player("up")
    print(new_game.player.current_location.room_name)
