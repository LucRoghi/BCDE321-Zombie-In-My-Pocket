"""
Author: Jared Ireland - jai0095
Author: Luc Roghi - lcr0059
For: BCDE311 Assignment2
"""

from Model.player import Player
from DevCards import DevCard
from TileCards import TileCard
from Model.map_tile import MapTile
from View.view_commands import Commands
from Model.game_data import GameData


@staticmethod
def stop_game(stop_game_confirm=None):
    if stop_game_confirm:
        pass
    else:
        pass


class Game:
    def __init__(self, time=9, game_state=""):
        self.time = time
        self.game_state = game_state

    def dev_card_popper(self):
        current_game_self = self.game_state
        match current_game_self:
            case ["START", self.dev_card_check()]:
                x = 2
            case "Memes":
                x = 1
        if x != 0:
            for x in current_game_self:
                GameData.dev_cards.pop(0)

    def dev_card_check(self):
        if self.dev_card is None and self.game_state is "PLAY":
            self.time += 1
            print(f'It is now {self.time}pm')

    def game_start(self):
        self.game_state = "START"
        l.initialize_map()
        # I don't know if this is technically how it works? its possible this might duplicate the intro block
        c.intro_block()
        self.dev_card_popper()

        pass
        # Get the DevCards loaded
        # Get the Tiles loaded
        # Get the Foyer placed - DONE

    def main_menu(self):  # Maybe have this so when the player "Quits" they can return to main menu? Quits = Main Menu
        # | Exit = Close Game?
        pass

    def get_time(self):
        return self.time

    def player_status(self):
        return print(f'It is {self.get_time()}pm \n'
                     f'The player currently has {p.health} health \n'
                     f'The player currently has {p.attack} attack \n'
                     f'The players items are {p.currentItems} \n'
                     f'The players current location is {p.currentLocation}')

    def dev_card_check(self):  # This is probs doesn't work logically lol... It actually might? Just don't have a
        # devcard array
        if self.dev_card is None and self.game_state is "PLAY":
            self.time += 1
            print(f'It is now {self.time}pm')
            dev_card_popper()

    def game_lost(self):
        if p.health <= 0:
            print(f'{p.name} has died - GAME OVER')
            self.game_state = "DEAD"
            self.game_end

        if self.time == 12:
            print(f'The time is {self.time}am. The zombies have risen in greater force and have overrun the world. - '
                  f'GAME OVER')
            self.game_state = "END"
            self.game_end

    def game_end(self):  # Changed this to be a Switch case of 3 choices - choices currently have nothing due to
        # there being currently no implementation
        if self.game_state == "END" or self.game_state == "DEAD":
            choice = ["QUIT", "RESTART", "LOAD"]
            if self.game_state == "END":  # Micro IF ELSE statement to simply change the message of the prompt so the
                # player knows what happened - Pls no hate :(
                self.prompt = f'Time has ran out. Do you wish to {choice}? '
            else:
                self.prompt = f'You have died. Do you wish to {choice}? '
            command = self.prompt.upper()
            match command:
                case "QUIT":
                    pass
                case "RESTART":
                    self.game_start()
                case "LOAD":
                    pass
        if self.prompt not in choice:
            print(f'You have not entered one of the following: {choice} - Please do so!')

    def view(self):
        # What should this be technically doing?
        print("HELLO WORLD!")
        pass

    def settings(self):
        # UH?
        pass

    def level(self):
        # Am I technically doing this in the game_start?
        pass

    def help_cmd(self):
        # This needs to call the Help command from CMD
        c.do_help_cmd()  # which I guess is just this?
        pass

    def change_settings(self):
        # UH?_2.0
        pass
