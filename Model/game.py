"""

"""
import random

from Model.game_data import GameData
from Model.map_tile import MapTile
from Model.player import Player


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.active_tile_list = self.game_data.map_tiles_indoor
        self.player = Player()
        self.time = 9
        self.root = None  # Start in Foyer
        self.last_action = None
        self.player.current_location = None
        self.current_dev_card = None
        self.current_tile = None

    def start_game(self):
        """
        Starts the game by removing 2 development cards from the pile and
        setting the player at the foyer
        :return:
        """
        self.root = self.active_tile_list[-1]
        print(self.root.room_name)
        self.player.current_location = self.root

    def move_player(self, direction):
        direction = direction.lower()
        move_player_functions = {"up": self.player.move_player_up(),
                                 "right": self.player.move_player_right(),
                                 "down": self.player.move_player_down(),
                                 "left": self.player.move_player_left()}
        try:
            move_player_functions[direction]
        except (ValueError, KeyError) as e:
            print(e)

    def player_attack(self):
        zombie_number = self.player.current_location.zombie_number
        self.player.health = self.player.health - (zombie_number - self.player.attack)
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
            return self.active_tile_list.pop(random_index)
        except IndexError as e:
            print(e)

    def attach_new_tile(self, tile, direction):
        direction = direction.lower()
        attach_new_tile_functions = {"up": self.player.current_location.add_new_room_up(tile),
                                     "right": self.player.current_location.add_new_room_right(tile),
                                     "down": self.player.current_location.add_new_room_down(tile),
                                     "left": self.player.current_location.add_new_room_left(tile)}
        try:
            attach_new_tile_functions[direction]
        except (ValueError, KeyError) as e:
            print(e)
            print("You need to rotate the tile in order to place it correctly")



