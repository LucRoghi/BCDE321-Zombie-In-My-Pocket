from abc import ABC, abstractmethod
from Model.CardMaker.AbstractConvert import *
from Model.map_tile import MapTile


class ConvertMaptiles(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        tile_list = []
        for tile in tuple_list:
            _, room_name, _, door_up, door_right, door_down, door_left, _type = tile
            tile = MapTile(room_name, None, super().str_to_bool(door_up), super().str_to_bool(door_right),
                           super().str_to_bool(door_down), super().str_to_bool(door_left))
            tile_list.append(tile)
        return tile_list
