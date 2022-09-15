"""
Author: Jared Ireland jai0095
"""
from random import random

from Model.file_handler import Filehandler
from Model.game_data import GameData
from Model.map_tile import MapTile
from Model.player import Player
from time import sleep


class GameController:
    def __init__(self):
        self.game_data = GameData()
        self.player = Player(self.game_data)
        self.active_tile = []
        self.dev_cards = self.game_data.dev_cards
        self.time: int = 9
        self.game_state: str = ""
        self.room_state: str = ""
        self.root = self.game_data.map_tiles_indoor[-1]
        self.prompt: str = ">>> "

    def intro_block(self):
        welcome = "Welcome to Zombies In My Pocket. A free to play card based print and play game made in Python"
        hint_one = "Type 'help' or '?' to get a list of usable commands - This is recommended for first time players!"
        hint_two = "Type 'rules' to get the rules and how to play - This is recommended for first time players!"
        hint_three = "When closing the game please use the 'exit' command. This will automatically save the game for " \
                     "you! "
        user_input = "You are currently in the 'Main Menu' of the game - you have 3 options: 'Load' 'Start' " \
                     "'Help'/'?' "
        self.prompt = user_input
        intro = welcome, sleep(0.5), hint_one, sleep(0.5), hint_two, sleep(0.5), hint_three, sleep(0.5), user_input
        return intro

    def game_start(self):
        self.game_state = "START"
        self.room_state = "INDOORS"
        self.player.current_location = self.root
        self.game_data.dev_card_pop()
        self.game_data.dev_card_pop()
        self.prompt = f'{self.intro_block()}'

    def get_game(self):
        text = ''
        if self.game_state == "Moving":
            text = "In this state, the player can choose a cardinal direction to move in"
        if self.game_state == "Rotating":
            text = "In this state, the player can choose how many rotations happen to the tile piece"
        if self.game_state == "DrawDevCard":
            text = "Use the draw command to draw a development card"

        # Fixme: Change self.temp to the correct commands - New Tile + Its doors
        return print(f'The chosen tile is {self.temp}, the valible doors are: {self.temp}. '
                     f'Current game state: {self.game_state}')

    def room_state_changes(self):
        if self.player.current_location.room_name == "Patio":
            self.room_state = "Outdoors"
            self.active_tile = self.game_data.map_tiles_outdoor
        if self.player.current_location.room_name == "Dining Room":
            self.room_state = "Indoors"
            self.active_tile = self.game_data.map_tiles_indoor

    def time_update(self):
        if not self.game_data.dev_cards and self.game_state == "PLAY":
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
            self.graph.player_health_graph()

    def time_game_over(self):
        print("The time has reached 12am. The horde has grown stronger and there is no stopping them")
        self.game_state = "END"
        self.graph.player_health_graph()

    def dead_game_over(self):
        print("You have died")
        self.game_state = "DEAD"
        self.graph.player_health_graph()

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
            self.prompt = f"Do you wish to stay Indoors or go Outdoors? ({valid_inputs}): "
            command = self.prompt
            command_dict = {"Indoor": self.commands.do_place_tile("Indoor"),
                            "Outdoor": self.commands.do_place_tile("Outdoor")}
            command_dict[command]
            self.commands.not_valid_input()

    def draw_new_map_tile(self, type_: str) -> MapTile:
        """
        Draws a new map tile from the respective list in game data. It is done by popping a random tile within the
        list and returning it as a Maptile object
        :param type_: str
        :return: Maptile object
        """
        if type_ == "Indoors":
            random_index = random.randint(0, len(self.game_data.map_tiles_indoor) - 1)
            return self.game_data.map_tiles_indoor.pop(random_index)
        elif type_ == "Outdoors":
            random_index = random.randint(0, len(self.game_data.map_tiles_outdoor) - 1)
            return self.game_data.map_tiles_outdoor.pop(random_index)


    def move_player(self, direction):
        """
        Moves the player in the corresponding direction based on the accepted argument
        :param direction:
        :return:
        """
        directions = {"up": self.player.move_player_up(), "right": self.player.move_player_right(),
                      "down": self.player.move_player_down(), "left": self.player.move_player_left()}
        if direction not in directions.keys():
            return False
        else:
            directions[direction.lower()]

    def add_new_tile(self, location):
        """
        Adds a new tile to the player tree based on the chose direction
        :param location:
        :return:
        """
        new_tile = self.draw_new_map_tile(self.room_state)
        add_tile_to_direction = {"up": self.player.current_location.add_new_room_up(new_tile),
                                 "right": self.player.current_location.add_new_room_right(new_tile),
                                 "down": self.player.current_location.add_new_room_down(new_tile),
                                 "left": self.player.current_location.add_new_room_down(new_tile)}
        status = add_tile_to_direction[location]
        if not status:
            print("Cannot add new room as a room is already placed or no door connects the room")
        return True

    def save_game(self):
        file_handler = Filehandler()
        file_handler.save_object_to_pickle("/Saves/", self)

    def load_save(self, save_name):
        file_handler = Filehandler()
        new_save_game = file_handler.load_object_from_pickle("/Saves/", save_name)
        return new_save_game


