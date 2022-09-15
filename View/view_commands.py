"""
Author: Jared Ireland - jai0095
For: BCDE311 Assignment2
"""
import cmd
from random import random

from Model.map_tile import MapTile
from Model.player import Player
from Model.game_data import GameData
from Model.game import GameController


# FIXME SuperSet Commands
#   This is for Global Commands - Mainly to Exit, Load, Save and Quit to main menu
#   Quit might have Quit -app and Quit -menu as Arguments


class Commands(cmd.Cmd):
    intro = "Donk Memes"

    def __init__(self):
        cmd.Cmd.__init__(self)
        super().__init__()
        self.game_state = ""
        self.player = Player()
        self.game = GameController()
        self.game_data = GameData()
        self.valid_input = []
        self.prompt = ">>> "

    # TODO - Doubt this works lmao
    def not_valid_input(self):
        if self.game.prompt not in self.valid_input:
            print("That is not a Valid Input\nPlease try again or look at the help page")

    def do_fix_db(self):
        """
        In case the database storing the rows is broken, running this function will recreate the database
        from the datafiles in the /Data file
        :return:
        """
        self.game_data.reset_database()

    # TODO - Logic might not work
    def do_move_cmd(self):
        """
        Reads the players input in which they wish to move, checks if the input is valid, if the input is valid it will
        look in the Dictionary and move in the corresponding input
        :return:
        """
        if self.game.game_state == "MOVING":
            self.valid_input = ["N", "E", "S", "W"]
            self.game.prompt = f'Which way do you wish to move? {self.valid_input}'
            command = self.game.prompt.upper()
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

    # TODO WIP
    def do_rotate_cmd(self, tile: MapTile = None):
        """
        Reads the players input to see their rotation, checks if the input is valid, if the input is valid it will
        then apply the rotation command
        :return:
        """
        if self.game.game_state == "ROTATE":
            self.game.prompt = "Do you wish to Rotate? (Y/N) "
            answer = self.game.prompt.upper()
            if answer == "Y":
                self.game.prompt = "How many times do you wish to rotate? (90º Steps) "
                r = int(self.game.prompt)
                try:
                    for i in range(r):
                        tile.rotate_tile_left()
                except:
                    raise TypeError
                return tile
        else:
            print("Unable to Rotate Tile")

    def do_place_tile(self, type: str = "Indoor"):
        """
        When the game has to draw a tile it will check where the player is - by default they are INDOORs
        It will draw a random tile in which the player then gets given a choice in where to place this tile
        It will then place the tile in accordance to the players choice in which the player can then continue
            playing the game
        :return:
        """
        if type == "Indoor":
            map_tile_list = self.game_data.map_tiles_indoor
        elif type == "Outdoor":
            map_tile_list = self.game_data.map_tiles_outdoor
        random_max_index = random.randint(0, len(map_tile_list) - 1)
        new_tile = map_tile_list.pop(random_max_index)
        self.player.current_location.print_door()
        self.game.prompt = "Which direction do you wish to place a new tile? (up/left/down/right)"
        r = self.game.prompt.lower()
        new_tile = self.do_rotate_cmd(new_tile)
        direction = {"up": self.player.current_location.add_new_room_up(new_tile),
                     "left": self.player.current_location.add_new_room_left(new_tile),
                     "down": self.player.current_location.add_new_room_down(new_tile),
                     "right": self.player.current_location.add_new_room_right(new_tile)}
        direction[r]

    # TODO WIP - Kinda done - Possible to Change
    def do_actions_cmd(self):
        """
        This sets up what actions the player can do only when there are zombies in the room. The following actions can
        be done:
        Attack/Atk - Attacks the zombies for how many attack points the player has. Lose HP on remaining zombies
        Cower - Gains 3HP but loses a Development Card
        Flee - Flees the room, losing 1 HP
        :return:
        """
        if self.player.current_location.zombie_number > 0:
            self.game.game_state = "ZOMBIES"
            self.player.can_cower = True
            self.player.can_attack = True
            self.player.can_flee = True

            self.valid_input = ["Attack", "atk", "Cower", "Flee"]
            self.game.prompt = f'What would you like to do? {self.valid_input}'
            command = self.game.prompt.upper()
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

    # TODO WIP - Probs needs the items stuff done
    def do_item_cmd(self):
        pass

    def do_bury_totem(self):
        """

        :return:
        """
        for item in self.player.inventory:
            if item.name == "Totem" and self.player.current_location.room_name == "Graveyard":
                self.game.prompt = "Do you wish to bury the totem? (Y/N) "
                answer = self.game.prompt.upper()
                if answer == "Y":
                    pass
            else:
                if self.player.current_location.room_name != "Graveyard":
                    print("You cannot bury the totem here")
                else:
                    print("You do not have the item in your inventory")

    def do_item_drop(self):
        if self.game.player_item_cap():
            self.game.prompt = "Would you like to drop an item? (Y/N)"
            command = self.game.prompt.upper()
            match command:
                case "Y":
                    self.do_item_drop()
                case "N":
                    pass

    # TODO TODO WIP - Kinda done - Possible to Change
    def do_help_cmd(self):
        commands_list = ["SAVE", "LOAD", "EXIT", "Movement", "N", "E", "S", "W", "Actions", "Attack", "Atk", "Cower",
                         "Flee", "Rotate", "Start", "-s", "-ns"]
        if self.game.intro_block == "Help" or self.game.intro_block == "?":
            print(f'A list of commands: \n{commands_list}')
            self.game.prompt = "Please type '?' before the command you wish to look at: (? move)"
            command = self.game.prompt.upper()
            match command:
                case "SAVE":
                    print("To save the game simply type 'save' as your input and the process of saving the game will "
                          "start")
                case "LOAD":
                    print("To load the game either in the main menu or at any time type 'load' as your input and the "
                          "process of loading will start")
                case "EXIT":
                    print("To exit the game type 'exit' as your input - you will then be asked to input an argument "
                          "of either -s or -ns")
                case "Movement":
                    print("The player can only move in 4 ways: \nN (? N)\nE (? E)\nS (? S)\nW (? W)")
                case "N":
                    print("The player will move North - either through the door (if possible) or through the wall (if "
                          "possible)")
                case "E":
                    print("The player will move East - either through the door (if possible) or through the wall (if "
                          "possible)")
                case "S":
                    print("The player will move South - either through the door (if possible) or through the wall (if "
                          "possible)")
                case "W":
                    print("The player will move West - either through the door (if possible) or through the wall (if "
                          "possible)")
                case "Actions":
                    print("There are four actions that the player can do when in a new room, after the development "
                          "card has been drawn \n "
                          "Attack (? Attack or ? Atk)\n"
                          "Cower (? Cower\n"
                          "Flee (? Flee)\n"
                          "Rest (? Rest)")
                case "Attack":
                    print("The player will use their attack score to attack the current zombies in the room. \n"
                          "For each point of attack score the player will kill 1 zombie \n"
                          "i.e. if a room has 4 zombies and you have 3 attack score, the player will kill 3 zombies\n"
                          "if the player doesn't have enough attack score to kill all the zombies in the room, "
                          "they will lose equal amount of health to remaining zombies after the attack\n "
                          "Note: You can never lose more than 4 health in a turn")
                case "Atk":
                    print("The player will use their attack score to attack the current zombies in the room. \n"
                          "For each point of attack score the player will kill 1 zombie \n"
                          "i.e. if a room has 4 zombies and you have 3 attack score, the player will kill 3 zombies\n"
                          "if the player doesn't have enough attack score to kill all the zombies in the room, "
                          "they will lose equal amount of health to remaining zombies after the attack\n "
                          "Note: You can never lose more than 4 health in a turn")
                case "Cower":
                    print("You curl up in the corner of the room and hide - You will regen 3 Health but lose time!")
                case "Flee":
                    print("You run to the previous tile you were on, losing 1 Health in the process")
                case "Rotate":
                    print("This is how the player rotates the game tiles around - This will be done in 90 degree "
                          "steps\n "
                          "4 rotates would equate to not rotating at all")
                case "Start":
                    print("This command can only be used in the main menu and it is to start a new game")
                case "-s":
                    print("This is an argument for the 'EXIT' command. Putting -s after exit will SAVE the game on "
                          "Exit ")
                case "-ns":
                    print("This is an argument for the 'EXIT' command. Putting -ns after exit will NOT SAVE the game "
                          "on Exit ")
            if self.game.prompt not in commands_list:
                print("Not a Valid Command - Please look at the commands!")

    # TODO WIP
    def file_handler(self):
        if self.game.prompt == "Save":
            pass
        if self.game.intro_block == "Load" or self.game.prompt == "Load":
            pass

    def do_load_cmd(self):
        pass

    def do_save_cmd(self):
        pass


if __name__ == "__main__":
    Commands().cmdloop()
