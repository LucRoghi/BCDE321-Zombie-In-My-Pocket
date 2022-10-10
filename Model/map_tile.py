"""
Author: Luc Roghi
For: BCDE321 Zombie In My Pocket

This module provides the setup for the nodes within the ternary tree within the MapTile Class
"""
from typing import Callable


class MapTile:
    def __init__(self, room_name: str = "", effect: Callable = None, door_up: bool = False,
                 door_right: bool = False, door_down: bool = False, door_left: bool = False):
        self.room_name: str = room_name
        self.zombie_number: int = 0
        self.effect: Callable = effect
        self.door_up: bool = door_up
        self.door_right: bool = door_right
        self.door_down: bool = door_down
        self.door_left: bool = door_left
        self.room_up = None
        self.room_right = None
        self.room_down = None
        self.room_left = None

    def __str__(self):
        return f"UP: {self.door_up}, RIGHT: {self.door_right}, DOWN: {self.door_down}, LEFT: {self.door_left}"

    def add_new_room_up(self, tile):
        if self.door_up and tile.door_down and self.room_up is None:
            tile.room_down = self
            self.room_up = tile
            return True
        else:
            return False

    def add_new_room_right(self, tile):
        if self.door_right and tile.door_left and self.room_right is None:
            tile.room_left = self
            self.room_right = tile
            return True
        else:
            return False

    def add_new_room_down(self, tile):
        if self.door_down and tile.door_up and self.room_down is None:
            tile.room_up = self
            self.room_down = tile
            return True
        else:
            return False

    def add_new_room_left(self, tile):
        if self.door_left and tile.door_right and self.room_left is None:
            tile.room_right = self
            self.room_left = tile
            return True
        else:
            return False

    def rotate_tile_left(self):
        if (self.room_up and self.room_right and self.room_down and self.room_left) is None:
            door_list = [self.door_up, self.door_right, self.door_down, self.door_left]
            self.door_up = door_list[-3]
            self.door_right = door_list[-2]
            self.door_down = door_list[-1]
            self.door_left = door_list[0]

    def rotate_tile_right(self):
        if (self.room_up and self.room_right and self.room_down and self.room_left) is None:
            door_list = [self.door_up, self.door_right, self.door_down, self.door_left]
            self.door_up = door_list[-1]
            self.door_right = door_list[-2]
            self.door_down = door_list[-3]
            self.door_left = door_list[0]

    def print_doors(self):
        final_string = f"Available doors are: "
        if self.door_up:
            final_string += "UP "
        if self.door_left:
            final_string += "LEFT "
        if self.door_down:
            final_string += "RIGHT "
        if self.door_right:
            final_string += "DOWN "
        return final_string

    def get_doors(self):
        return {"up": self.door_up, "right": self.door_right, "down": self.door_down, "left": self.door_left}


if __name__ == "__main__":
    test_tile = MapTile("test_room", None, True, False, True, False)
    test_tile.rotate_tile_right()
    test_tile.rotate_tile_left()
    test_tile_2 = MapTile("test_room_2", None, True, False, False, True)
    test_tile.add_new_room_up(test_tile_2)
    test_tile_2.rotate_tile_left()
    test_tile_2.rotate_tile_left()
    test_tile.add_new_room_up(test_tile_2)
    test_tile_3 = MapTile("test_room_3", None, True, False, True, True)
    test_tile_2.add_new_room_up(test_tile_3)
    test_tile_2.add_new_room_right(test_tile_3)
    print(test_tile_3)
    test_tile_3.rotate_tile_left()
    print(test_tile_3)
    test_tile_3.rotate_tile_left()
    print(test_tile_3)
