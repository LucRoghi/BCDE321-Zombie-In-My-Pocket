"""

"""
from Model.game_data import GameData
from Model.player import Player


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.player = Player(self.game_data)
        self.time = 9
        self.root = None # Start in Foyer
        self.player.current_location = self.root
        self.state = ""

    def start_game(self):
        """
        Starts the gmae by removing 2 development cards from the pile and
        setting the player at the foyer
        :return:
        """
        self.root = self.game_data.map_tiles_indoor[-1]
        self.player.current_location = self.root

    def move_player(self, direction):
        move_player_functions = {"up": self.player.move_player_up(),
                                 "right": self.player.move_player_right(),
                                 "down": self.player.move_player_down(),
                                 "left": self.player}

