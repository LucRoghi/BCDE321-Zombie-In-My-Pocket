"""
Author: Jared Ireland - jai0095
Author: Luc Roghi - lcr0059
For: BCDE311 Assignment2
"""

from Game import Game as g
from DevCards import DevCard as d
import MapNode


class Player:
    def __init__(self, name="", health=0, attack=0, inventory=[], previous_location=""):
        self.name = name
        self.health = health
        self.attack = attack
        self.current_location = MapNode('Foyer', 'None', 'Indoors', 0, 1, 0, 0, 0, 1)
        self.inventory = inventory
        self.can_cower = False
        self.can_attack = False
        self.can_flee = False
        self.previous_location = previous_location

    # FIXME - Logic is broken here
    def cower(self):
        if self.can_cower:
            self.health += 3
            g.dev_card_popper()
            print("You cower in fear, gaining 3 health, but lose time with the dev card")
        else:
            return print("Cannot cower during a zombie door attack")

    # TODO Add prompt to use item - using Command as a temp
    def player_attack(self):
        if self.can_attack:
            self.current_location.zombie_number -= self.attack
            self.health = self.health - self.current_location.zombie_number
            command = "Use Chainsaw"
            print(f'Player lost {self.current_location.zombie_number}. The player now has {self.health}')
        else:
            print("Player can not attack")

    def flee(self):
        if self.can_flee:
            self.health = self.health - self.current_location.zombie_number
            self.current_location = self.previous_location
            print(f'Player has lost {self.current_location.zombie_number} and now has {self.health}.')
            g.dev_card_check()

    # FIXME - Logic is broken here
    def rest(self):
        if self.can_rest:
            self.health += 3
            g.dev_card_popper()