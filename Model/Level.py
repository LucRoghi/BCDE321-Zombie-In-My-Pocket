"""
Author: Luc Roghi
For: BCDE321 Zombie In My Pocket

This module provides the setup for the nodes within the ternary tree within the Level Class
"""
import dataclasses
from typing import Callable


@dataclasses
class Doors:
    door_up: bool
    door_right: bool
    door_down: bool
    door_left: bool


@dataclasses(order=True)
class MapTile:
    room_name: str = ""
    zombie_number: int = 0
    effect: Callable = None
    doors: Doors = Doors(False, False, False, False)
    room_up = None
    room_right = None
    room_left = None
    room_down = None


def create_new_map_tile(room_name: str, effect: Callable, doors: Doors, room_up: MapTile, room_right: MapTile,
                        room_down: MapTile, room_left: MapTile) -> MapTile:
    """
    Handles the creation of the MapTile to be inserted into the Level Ternary tree to create the map
    :param room_name:
    :param effect:
    :param doors:
    :param room_up:
    :param room_right:
    :param room_down:
    :param room_left:
    :return MapTile:
    """
    return MapTile(room_name, 0, effect, doors, room_up, room_right, room_down, room_left)


if __name__ == "__main__":
    pass
