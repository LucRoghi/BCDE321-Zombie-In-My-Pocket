from Model.map_tile import MapTile
from Model.game_data import GameData


class Player:
    def __init__(self):
        self.current_location = None
        self.previous_location = None
        self.attack: int = 1
        self.health: int = 6
        self.inventory: list = []
        self.has_totem: bool = False

    def move_player_up(self):
        if self.current_location.room_up is not None:
            self.current_location = self.current_location.room_up
        else:
            return ValueError("The room going up does not exist, cannot travel")

    def move_player_right(self):
        if self.current_location.room_right is not None:
            self.current_location = self.current_location.room_right
        else:
            return ValueError("The room going right does not exist, cannot travel")

    def move_player_down(self):
        if self.current_location.room_down is not None:
            self.current_location = self.current_location.room_down
        else:
            return ValueError("The room going down does not exist, cannot travel")

    def move_player_left(self):
        if self.current_location.room_left is not None:
            self.current_location = self.current_location.room_left
        else:
            return ValueError("The room going left does not exist, cannot travel")

    def cower(self):
        self.health += 3
        return f"You cower in fear, gaining 3 health, but lose time with the dev card \n Current Health: {self.health}"

    def player_attack(self):
        self.current_location.zombie_number -= self.attack
        self.health = self.health - self.current_location.zombie_number
        return f'Player lost {self.current_location.zombie_number} health. The player now has {self.health} ' \
               f'health remaining'

    def flee(self):
        new_health = self.health - self.current_location.zombie_number
        health_diff = self.health - new_health
        self.health = new_health
        self.current_location = self.previous_location
        return f'Player lost {health_diff} health. The player now has {self.health} health remaining'

    def drop_item(self, index):
        self.inventory.pop(index)
