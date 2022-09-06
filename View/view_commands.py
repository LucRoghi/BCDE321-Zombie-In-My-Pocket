"""
Author: Jared Ireland - jai0095
For: BCDE311 Assignment2
"""
import cmd
import Model.Player as p
import Model.GameData as g
from time import sleep


# Commands needed:
# Start Command
#
# Move Command
# Rotate Command
#
# Attack Command
# Flee Command
# Rest Command
# Cower Command
#
# Item "Search" Command -- Pick up the item
# Drop Item
# Bury Totem
#
# Help

# Load
# Save

# FIXME SuperSet Commands
#   This is for Global Commands - Mainly to Exit, Load, Save and Quit to main menu
#   Quit might have Quit -app and Quit -menu as Arguments


class Commands(cmd.Cmd):
    def __init__(self):
        cmd.CMD.__init__(self)
        self.prompt = ">>> "
        self.player = p.Player()
        self.game = g.Game(self.player)

# TODO: Done
    def intro_block(self):
        welcome = "Welcome to Zombies In My Pocket. A free to play card based print and play game made in Python"
        hint_one = "Type 'help' or '?' to get a list of useable commands - This is recommended for first time players!"
        hint_two = "Type 'rules' to get the rules and how to play - This is recommended for first time players!"
        hint_three = "When closing the game please use the 'exit' command. This will automatically save the game for " \
                     "you! "
        self.prompt = "You are currently in the 'Main Menu' of the game - you have 3 options: 'Load' 'Start' " \
                      "'Help'/'?' "
        intro = welcome, sleep(0.5), hint_one, sleep(0.5), hint_two, sleep(0.5), hint_three, sleep(0.5)

# TODO - Logic might not work
    def do_move_cmd(self):
        if g.game_state == "MOVING":
            valid_input = ["N", "E", "S", "W"]
            self.prompt = f'Which way do you wish to move? {valid_input}'
            command = self.prompt.upper()
            match command:
                case "N":
                    p.move_player_up()
                case "E":
                    p.move_player_right()
                case "S":
                    p.move_player_down()
                case "W":
                    p.move_player_left()
            if self.prompt not in valid_input:
                print("Please look at the Help command for valid Movement")
        else:
            print("Player can not move at this time")

# TODO WIP
    def do_rotate_cmd(self):
        if g.game_state == "ROTATE":
            self.prompt = "Do you wish to Rotate? (Y/N) "
            answer = self.prompt.upper()
            if answer == "Y":
                self.prompt = "How many times do you wish to rotate? (90º Steps) "
                r = self.prompt
            # rotate(r)
            # place()
        else:
            print("Unable to Rotate Tile")

# TODO WIP - Kinda done - Possible to Change
    def do_actions_cmd(self):
        if p.current_location.zombie_number > 0:
            g.game_state == "ZOMBIES"
            p.can_cower = True
            p.can_attack = True
            p.can_flee = True
            p.can_rest = True

            valid_input = ["Attack", "atk", "Cower", "Flee"]
            self.prompt = f'What would you like to do? {valid_input}'
            command = self.prompt.upper()
            match command:
                case "Attack":
                    p.player_attack()
                case "atk":
                    p.player_attack()
                case "Cower":
                    p.cower()
                case "Flee":
                    p.flee()
                case "Rest":
                    p.rest()
            if self.prompt not in valid_input:
                print("Please look at the Help command for valid Actions")

# TODO WIP - Probs needs the items stuff done
    def do_item_cmd(self):
        # if Inventory = 2 -- Always check this!
            #do_drop_item_cmd
        # if DevCard Drawn
            # do_item_search_cmd
        # if p.current_location = "Temple" and p.current_item contains "Totem"
            # self.prompt = "Do you wish to bury the totem? (Y/N) "
            # answer = self.prompt.upper()
            # if answer == "Y"
                #do_bury_item_cmd
        pass

# TODO TODO WIP - Kinda done - Possible to Change
    def do_help_cmd(self):
        commands_list = ["SAVE", "LOAD", "EXIT", "Movement", "N", "E", "S", "W", "Actions", "Attack", "Atk", "Cower",
                         "Flee", "Rotate", "Start", "-s", "-ns"]
        if self.intro_block.text == "Help" or self.intro_block.text == "?":
            print(f'A list of commands: \n{commands_list}')
            self.prompt = "Please type '?' before the command you wish to look at: (? move)"
            command = self.prompt.upper()
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
            if self.prompt not in commands_list:
                print("Not a Valid Command - Please relook at the commands!")

# TODO WIP
    def file_handler(self):
        if self.prompt == "Save":
            pass
        if self.intro_block.text == "Load" or self.prompt == "Load":
            pass

    def do_load_cmd(self):
        pass

    def do_save_cmd(self):
        pass