# This is the controller
import random

from Model.game_data import GameData
from Model.map_tile import MapTile
from Model.player import Player
from View.view_commands import Commands


# TODO - Luc fix :)
class GameController:
    def __init__(self):
        self.game_data = GameData()
        self.map_tile = MapTile()
        self.player = Player(self.game_data)
        self.commands = Commands()
        self.dev_cards = self.game_data.dev_cards
        self.time = 9
        self.game_state = ""
        self.room_state = ""
        self.root = self.game_data.map_tiles_indoor[-1]
        self.user_prompt = Commands().prompt

    def game_start(self):
        self.game_state = "START"
        self.room_state = "INDOORS"
        self.player.current_location = self.root
        self.game_data.dev_card_pop()
        self.game_data.dev_card_pop()
        self.user_prompt = f'{Commands.intro_block()}'

    def room_state_changes(self):
        if self.player.current_location.room_name == "Patio":
            self.room_state = "Outdoors"
            self.game_data.map_tiles_outdoor()
        if self.player.current_location.room_name == "Dining Room":
            self.room_state = "Indoors"
            self.game_data.map_tiles_indoor()

    def time_update(self):
        if not self.game_data.dev_cards and self.game_state is "PLAY":
            self.time += 1
            self.game_data.dev_card_pop()
            self.game_data.dev_card_pop()
            print(f'It is now {self.time}pm')

    def player_status(self):
        return print(f'It is {self.time}pm \n'
                     f'The player currently has {self.player.health} health \n'
                     f'The player currently has {self.player.attack} attack \n'
                     f'The players items are {self.player.inventory} \n'
                     f'The players current location is {self.player.current_location.room_name}')

    def player_action_change(self):
        player_actions = ["can_cower", "can_flee", "can_attack"]
        if self.map_tile.zombie_number > 0:
            for attr in player_actions:
                setattr(self.player, attr, True)
        else:
            for attr in player_actions:
                setattr(self.player, attr, False)

    def player_item_cap(self):
        if len(self.player.inventory) > 2:
            print("You can not pick up an items. Please drop one to replace!")

    def win_con(self):
        if self.player.current_location.room_name == "Graveyard" and self.map_tile.bury_totem():
            print("The horde starts to crumble into dust, you collapse on the ground exhausted.\nYou have won!")
            self.game_state = "WIN"

    def time_game_over(self):
        print("The time has reached 12am. The horde has grown stronger and there is no stopping them")
        self.game_state = "END"

    def dead_game_over(self):
        print("You have died")
        self.game_state = "DEAD"

    def loss_con(self):
        command = ""
        if self.time == 12:
            command = "Time"
        elif self.player.health <= 0:
            command = "Dead"
        command_dict = {"Time": self.time_game_over(), "Dead": self.dead_game_over}
        command_dict[command]

    def player_select_tile_type(self):
        # Checking which tile the player wishes to use
        if self.player.current_location.room_name == "Dining Room" \
                and "Patio" not in self.player.current_location.get_doors():
            valid_inputs = ["Indoors", "Outdoors"]
            self.user_prompt = f"Do you wish to stay Indoors or go Outdoors? ({valid_inputs}): "
            command = self.user_prompt
            command_dict = {"Indoor": self.commands.do_place_tile("Indoor"),
                            "Outdoor": self.commands.do_place_tile("Outdoor")}
            command_dict[command]
            self.commands.not_valid_input()

