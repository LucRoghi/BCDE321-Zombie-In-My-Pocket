"""
Author: Jared Ireland jai0095
For: BCDE311 Assignment2
"""

import random

from Database import Database
from Game import Game
from MapNode import MapNode
from old_player import Player


class DevCard:
    def __init__(self, item, event_one, event_two, event_three):
        self.item = item
        self.e_one = event_one
        self.e_two = event_two
        self.e_three = event_three
        self.has_played = bool
        self.dev_cards = []

    # TODO This should load from the Database, apened to the dev_cards list, then shuffles it
    def load_dev_cards(self):
        card_data = Database.get_dev_card_data()
        for card in card_data:
            card_item = card(Database.get_dev_card_data(item))
            e_one = card(Database.get_dev_card_data(event_one), Database.get_dev_card_data(e1_consequence))
            e_two = card(Database.get_dev_card_data(event_two), Database.get_dev_card_data(e2_consequence))
            e_three = card(Database.get_dev_card_data(event_three), Database.get_dev_card_data(e3_consequence))
            has_played = card(Database.get_dev_card_data(played))
            dev_card = DevCard(card_item, e_one, e_two, e_three, has_played)
            self.dev_cards.append(dev_card)
        random.shuffle(self.dev_cards)

    # TODO The functionality of the dev card when it gets played needs to be put here where the print is
    #   Note: This doesn't need a shuffle - DevCard[] should shuffle when the game Starts and when the hour "ticks over"
    #   i.e. 9pm -> 10pm
    #   pop can return -> push to new list?

    # TODO I think this technically works - assuming that Database actually works lmao
    def dev_card_play(self):
        print(self.dev_cards(0))
        command = Game.get_time()
        match command:
            case 9:
                self.load_dev_cards.e_one
            case 10:
                self.load_dev_cards.e_two
            case 11:
                self.load_dev_cards.e_three
        self.dev_cards.pop(0)

    # TODO To make it so the Consequence knows what to do i.e. if event = zombies add consequence to tile

    # TODO Fix this up lmao - most likely can make seperate match cases to call from i.e. instead of having 3 zombie
    #   match cases have 1 match case and call from that
    def event_consequence(self):
        command = Game.get_time()
        match command:
            case 9:
                e1 = self.load_dev_cards.e_one([0])
                e1c = self.load_dev_cards.e_one([1])
                match e1:
                    case "Nothing":
                        print("Nothing happened")
                    case "Zombies":
                        match e1c:
                            case 3:
                                MapNode.zombie_number += 3
                            case 4:
                                MapNode.zombie_number += 3
                    case "Health":
                        match e1c:
                            case -1:
                                Player.health -= 1
                            case 1:
                                Player.health += 1
                    case "Item":
                        print("You find a Grisly Femur")  # Need an add item here

            case 10:
                e2 = self.load_dev_cards.e_two([0])
                e2c = self.load_dev_cards.e_two([1])
                match e2:
                    case "Nothing":
                        print("Nothing happened")
                    case "Zombies":
                        match e2c:
                            case 3:
                                MapNode.zombie_number += 3
                            case 4:
                                MapNode.zombie_number += 3
                            case 5:
                                MapNode.zombie_number += 5
                    case "Health":
                        match e2c:
                            case -1:
                                Player.health -= 1
                            case 1:
                                Player.health += 1
                    case "Item":
                        match e2c:
                            case "Oil":
                                print("Picked up Oil")
                            case "Can of Soda":
                                print("Picked up a can of soda")

            case 11:
                e3 = self.load_dev_cards.e_three([0])
                e3c = self.load_dev_cards.e_three([1])
                match e3:
                    case "Nothing":
                        print("Nothing happened")
                    case "Zombies":
                        match e3c:
                            case 3:
                                MapNode.zombie_number += 3
                            case 4:
                                MapNode.zombie_number += 3
                            case 6:
                                MapNode.zombie_number += 6
                    case "Health":
                        Player.health -= 1
                    case "Item":
                        print("You find a Gas Can")  # Need an add item here
        pass

    # Structured like an actual Dev Card:
    # +--------------------------+
    # |  Item: Board With Nails  |
    # +--------------------------+
    # | Nothing             None |
    # +--------------------------+
    # | Zombies                4 |
    # +--------------------------+
    # | Health                -1 |
    # +--------------------------+