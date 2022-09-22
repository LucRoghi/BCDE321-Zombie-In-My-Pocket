from Model.map_tile import MapTile
from Model.player import Player
from Model.game_data import GameData
from Model.file_handler import Filehandler
from Model.dev_cards import DevCard
from time import sleep
from random import random


class ZIMPController:
    def __init__(self):
        self.map = MapTile("", None, False, False, False, False)
        self.file_handler = Filehandler()
        self.game_data = GameData()
        self.player = Player(self.game_data)
        self.valid_input = []
        self.active_tile = []
        self.game_state: str = ""
        self.room_state: str = ""
        self.root = self.game_data.map_tiles_indoor[-1]
        self.prompt: str = ">>> "
        self.dev_cards = DevCard
        self.time: int = 9
        self.is_at_temple = False
        self.new_game()

    def new_game(self):
        pass

    def start_game(self):
        self.game_state = "START"
        self.room_state = "INDOORS"
        self.player.current_location = self.root
        self.game_data.dev_card_pop()
        self.game_data.dev_card_pop()

    def room_state_changes(self):
        if self.player.current_location.room_name == "Patio":
            self.room_state = "Outdoors"
            self.active_tile = self.game_data.map_tiles_outdoor
        if self.player.current_location.room_name == "Dining Room":
            self.room_state = "Indoors"
            self.active_tile = self.game_data.map_tiles_indoor

    def time_update(self):
        if not self.dev_cards and self.game_state == "PLAY":
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
        if self.map.zombie_number > 0:
            for attr in player_actions:
                setattr(self.player, attr, True)
        else:
            for attr in player_actions:
                setattr(self.player, attr, False)

    def player_item_cap(self):
        # and DevCard = Item
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

    # TODO I don't think I finished this?
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

    def fix_db(self):
        self.game_data.reset_database()

    def not_valid_input(self):
        if self.prompt not in self.valid_input:
            print("That is not a Valid Input\nPlease try again or look at the help page")

    def move_player(self):
        if self.game_state == "MOVING":
            self.valid_input = ["N", "E", "S", "W"]
            self.prompt = f'Which way do you wish to move? {self.valid_input}'
            command = self.prompt.upper()
            command_dict = {
                "N": self.player.move_player_up(),
                "E": self.player.move_player_right(),
                "S": self.player.move_player_down(),
                "W": self.player.move_player_left()
            }
            command_dict[command]
            self.not_valid_input()
        else:
            print("Player can not move at this time")

    def rotate_tile(self, tile: MapTile = None):
        if self.game_state == "ROTATE":
            self.prompt = "Do you wish to Rotate? (Y/N) "
            answer = self.prompt.upper()
            if answer == "Y":
                self.prompt = "How many times do you wish to rotate? (90º Steps) "
                r = int(self.prompt)
                try:
                    for i in range(r):
                        tile.rotate_tile_left()
                except:
                    raise TypeError
                return tile
        else:
            print("Unable to Rotate Tile")

    def place_tile(self):
        if type == "Indoor":
            map_tile_list = self.game_data.map_tiles_indoor
        elif type == "Outdoor":
            map_tile_list = self.game_data.map_tiles_outdoor
        random_max_index = random.randint(0, len(map_tile_list) - 1)
        new_tile = map_tile_list.pop(random_max_index)
        self.player.current_location.print_door()
        self.prompt = "Which direction do you wish to place a new tile? (up/left/down/right)"
        r = self.prompt.lower()
        new_tile = self.rotate_tile(new_tile)
        direction = {"up": self.player.current_location.add_new_room_up(new_tile),
                     "left": self.player.current_location.add_new_room_left(new_tile),
                     "down": self.player.current_location.add_new_room_down(new_tile),
                     "right": self.player.current_location.add_new_room_right(new_tile)}
        direction[r]

    def player_actions(self):
        if self.player.current_location.zombie_number > 0:
            self.game_state = "ZOMBIES"
            self.player.can_cower = True
            self.player.can_attack = True
            self.player.can_flee = True

            self.valid_input = ["Attack", "atk", "Cower", "Flee"]
            self.prompt = f'What would you like to do? {self.valid_input}'
            command = self.prompt.upper()
            # Look at Effects in DevCard
            # Change to dictionary
            command_dict = {
                "Attack": self.player.player_attack(),
                "atk": self.player.player_attack(),
                "Cower": self.player.cower(),
                "Flee": self.player.flee()
            }
            command_dict[command]

            if command == "cower":
                self.game_data.dev_card_pop()
            self.not_valid_input()

    def bury_totem(self):
        for item in self.player.inventory:
            if item.name == "Totem" and self.player.current_location.room_name == "Graveyard":
                self.prompt = "Do you wish to bury the totem? (Y/N) "
                answer = self.prompt.upper()
                if answer == "Y":
                    pass
            else:
                if self.player.current_location.room_name != "Graveyard":
                    print("You cannot bury the totem here")
                else:
                    print("You do not have the item in your inventory")

    def drop_item(self):
        if self.player_item_cap():
            self.prompt = "Would you like to drop an item? (Y/N)"
            command = self.prompt.upper()
            match command:
                case "Y":
                    pass
                case "N":
                    pass

    def file_handler_save(self):
        self.file_handler.save_object_to_pickle()

    def file_handler_load(self):
        self.file_handler.load_object_from_pickle()

    def restart_game(self):
        del self.game_data

    def use_item(self):
        if "Can of Soda" in self.player.inventory:
            self.player.health += 2
            index = self.player.inventory.index("Can of Soda")
            self.player.inventory.pop(index)
            print("You drunk a can of Soda. +2 HP")

        if "Gasoline" and "Chainsaw" in self.player.inventory:
            self.prompt = "Do you wish to combine these items? (Gasoline + Chainsaw)"
            command = self.prompt.upper()
            if command == "Y":
                pass
            else:
                pass

        if "Gasoline" and "Candle" in self.player.inventory and self.player.current_location.zombie_number > 0:
            self.prompt = "Do you wish to combine these items? (Gasoline + Candle)"
            command = self.prompt.upper()
            if command == "Y":
                pass
            else:
                pass

        if "Oil" and "Candle" in self.player.inventory and self.player.current_location.zombie_number > 0:
            self.prompt = "Do you wish to combine these items? (Oil + Candle)"
            command = self.prompt.upper()
            if command == "Y":
                pass
            else:
                pass

    def get_totem(self):
        if self.player.current_location == "Evil Temple":
            self.is_at_temple = True

        time_dict = {
            self.dev_cards.nine_oclock: {self.time: 9},
            self.dev_cards.ten_oclock: {self.time: 10},
            self.dev_cards.eleven_oclock: {self.time: 11}
        }
        if time_dict == "get_new_item" and self.is_at_temple == True:
            self.player_item_cap()
            self.player.inventory.append("Totem")
            print("You picked up a Totem... where to take it now?")

    def exit_game(self):
        return exit()
