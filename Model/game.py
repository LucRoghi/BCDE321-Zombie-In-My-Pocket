"""

"""
from Model.game_data import GameData
from Model.player import Player


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.player = Player()
        self.time = 9
        self.root = None  # Start in Foyer
        self.player.current_location = self.root
        self.state = ""
        self.current_dev_card = None

    def start_game(self):
        """
        Starts the gmae by removing 2 development cards from the pile and
        setting the player at the foyer
        :return:
        """
        self.root = self.game_data.map_tiles_indoor[-1]
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

    def draw_new_dev_card(self):
        try:
            self.current_dev_card = self.game_data.dev_card_pop()
        except IndexError as e:
            print(e)

    def draw_new_tile(self):
        raise NotImplementedError

    def rotate_new_tile(self):
        raise NotImplementedError

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
