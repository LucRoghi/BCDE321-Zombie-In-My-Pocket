"""
Author: Jared Ireland jai0095
"""
from Model.map_tile import MapTile
from Model.game_data import GameData


class Player:
    def __init__(self, game_data):
        self.game_data: GameData = game_data
        self.current_location: MapTile = None
        self.previous_location = None
        self.attack: int = 1
        self.health: int = 6
        self.inventory: list = []
        self.has_totem: bool = False
        self.can_cower: bool = False
        self.can_attack: bool = False
        self.can_flee: bool = False

    def move_player_up(self):
        if self.current_location.room_up is not None:
            self.current_location = self.current_location.room_up

    def move_player_right(self):
        if self.current_location.room_right is not None:
            self.current_location = self.current_location.room_right

    def move_player_down(self):
        if self.current_location.room_down is not None:
            self.current_location = self.current_location.room_down

    def move_player_left(self):
        if self.current_location.room_left is not None:
            self.current_location = self.current_location.room_left

    def cower(self):
        if self.can_cower:
            self.health += 3
            print(f"You cower in fear, gaining 3 health, but lose time with the dev card."
                  f" Current Health: {self.health}")
            self.game_data.dev_card_pop()
        else:
            return print("Cannot cower during a zombie door attack")

    def player_attack(self):
        if self.can_attack:
            self.current_location.zombie_number -= self.attack
            self.health = self.health - self.current_location.zombie_number
            print(f'Player lost {self.current_location.zombie_number} health. The player now has {self.health} health '
                  f'remaining')
        else:
            print("Player can not attack")

    def flee(self):
        if self.can_flee:
            new_health = self.health - self.current_location.zombie_number
            health_diff = self.health - new_health
            self.health = new_health
            self.current_location = self.previous_location
            print(f'Player lost {health_diff} health. The player now has {self.health} health '
                  f'remaining')

    def drop_item(self, index):
        self.inventory.pop(index)

