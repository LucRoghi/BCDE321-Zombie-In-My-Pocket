# This is the controller
from GameData import GameData
from MapTile import MapTile
from Player import Player

# TODO - Luc fix :)
class GameController:
    def __init__(self):
        self.game_data = GameData()
        self.map_tile = MapTile()
        self.player = Player()
        self.time = 9

    def dev_card_popper(self):
        pass

    def time_update(self):
        if not self.game_data.dev_card and self.game_state is "PLAY":
            self.time += 1
            print(f'It is now {self.time}pm')

    def player_status(self):
        return print(f'It is {self.time}pm \n'
                     f'The player currently has {self.player.health} health \n'
                     f'The player currently has {self.player.attack} attack \n'
                     f'The players items are {self.player.inventory} \n'
                     f'The players current location is {self.player.current_location}')

    def player_action_change(self):
        player_actions = ["can_cower", "can_flee", "can_attack"]
        if self.map_tile.zombie_number > 0:
            for attr in player_actions:
                setattr(self.player, attr, True)
        else:
            for attr in player_actions:
                setattr(self.player, attr, False)

