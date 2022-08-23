"""
Author: Luc Roghi
For: BCDE321 Zombie In My Pocket

This module provides the setup for the nodes within the ternary tree within the Level Class
"""
import dataclasses
from typing import Callable


@dataclasses(order=True)
class MapTile:
    room_name: str = ""
    zombie_number: int = 0
    effect: Callable = None
    door_up = False
    door_right = False
    door_down = False
    door_left = False
    room_up = None
    room_right = None
    room_left = None
    room_down = None


def create_new_map_tile(room_name: str,
                        effect: Callable,
                        door_up: bool,
                        door_right: bool,
                        door_down: bool,
                        door_left: bool,
                        room_up: MapTile,
                        room_right: MapTile,
                        room_down: MapTile,
                        room_left: MapTile) -> MapTile:

    new_map_tile = MapTile(room_name, 0, effect, door_up, door_right, door_down,
                           door_left, room_up, room_right, room_down, room_left)
    return new_map_tile


if __name__ == "__main__":
    pass
