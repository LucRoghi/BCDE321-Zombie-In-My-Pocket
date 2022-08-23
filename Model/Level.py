"""
Author: Luc Roghi
For: BCDE321 Zombie In My Pocket

This module provides the setup for the nodes within the ternary tree within the Level Class
"""
import dataclasses
from typing import Callable

from Model import DatabaseHandler


@dataclasses(order=True)
class MapTile:
    room_name: str = ""
    zombie_number: int = 0
    effect: Callable = None
    is_indoor: bool = False
    door_up = False
    door_right = False
    door_down = False
    door_left = False
    room_up = None
    room_right = None
    room_left = None
    room_down = None


@dataclasses
class Level:
    level_name: str = ""
    tile_data: list[tuple] = DatabaseHandler.get_tile_data()
    root: MapTile = None

    def create_new_map_node(self, single_tile):
        name, effect, is_indoor, door_up, door_right, door_down, door_left, been_played = single_tile
        new_tile = MapTile(name, 0, effect, is_indoor, door_up, door_right, door_down, door_left)
        return new_tile

    def add_new_room_up(self, single_tile: MapTile):
        self.root.room_up = single_tile

    def add_new_room_right(self, single_tile: MapTile):
        self.root.room_right = single_tile

    def add_new_room_down(self, single_tile: MapTile):
        self.root.room_down = single_tile

    def add_new_room_left(self, single_tile: MapTile):
        self.root.room_left = single_tile




if __name__ == "__main__":
    pass
