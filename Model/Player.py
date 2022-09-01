from Model.MapTile import MapTile


class Player:
    def __init__(self, name, current_location, attack, health, inventory, has_totem):
        self.name: str = ""
        self.current_location: MapTile = None
        self.attack: int = 1
        self.health: int = 6
        self.inventory = []
        self.has_totem: bool = None

    def move_player_up(self):
        if self.current_location.room_up is not None:
            self.current_location = self.current_location.room_up

    def move_player_right(self):
        if self.current_location.room_right is not None:
            self.current_location = self.cureent_location.room_right

    def move_player_down(self):
        if self.current_location.room_down is not None:
            self.current_location = self.current_location.room_down

    def move_player_left(self):
        if self.current_location.room_left is not None:
            self.current_location = self.current_location.room_left

