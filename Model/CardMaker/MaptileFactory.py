from Model.CardMaker.CardFactory import CardFactory
from Model.map_tile import MapTile


class MaptileFactory(CardFactory):
    def create_card(self, tuple):
        _, room_name, _, door_up, door_right, door_down, door_left, _type = tuple
        tile = MapTile(room_name, None, super().str_to_bool(door_up), super().str_to_bool(door_right),
                       super().str_to_bool(door_down), super().str_to_bool(door_left))
        return tile
