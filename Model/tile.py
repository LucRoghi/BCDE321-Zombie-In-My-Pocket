"""
Author: Jared Ireland jai0095

Tile Constructor for the two sub tile files (Outdoor and Indoor)
"""
import Model


class Tile:
    def __init__(self, name, x=16, y=16, effect=None, doors=None, entrance=None):
        if doors is None:
            doors = []
        self.name = name
        self.x = x  # x will represent the tiles position horizontally
        self.y = y  # y will represent the tiles position vertically
        self.effect = effect
        self.doors = doors
        self.entrance = entrance

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def change_door_position(self, idx, direction):
        self.doors[idx] = direction

    def set_entrance(self, direction):
        self.entrance = direction

    def rotate_entrance(self):
        if self.entrance == Model.Direction.UP:
            self.set_entrance(Model.Direction.RIGHT)
            return
        if self.entrance == Model.Direction.DOWN:
            self.set_entrance(Model.Direction.LEFT)
            return
        if self.entrance == Model.Direction.RIGHT:
            self.set_entrance(Model.Direction.DOWN)
            return
        if self.entrance == Model.Direction.LEFT:
            self.set_entrance(Model.Direction.UP)
            return

    def rotate_tile(self):  # Will rotate the tile 1 position clockwise
        for door in self.doors:
            if door == Model.Direction.UP:
                self.change_door_position(self.doors.index(door), Model.Direction.RIGHT)
            if door == Model.Direction.RIGHT:
                self.change_door_position(self.doors.index(door), Model.Direction.DOWN)
            if door == Model.Direction.DOWN:
                self.change_door_position(self.doors.index(door), Model.Direction.LEFT)
            if door == Model.Direction.LEFT:
                self.change_door_position(self.doors.index(door), Model.Direction.UP)
