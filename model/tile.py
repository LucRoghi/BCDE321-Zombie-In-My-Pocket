"""
Author: Jared Ireland jai0095

Tile Constructor for the two sub tile files (Outdoor and Indoor)
"""
import model


class Tile:
    def __init__(self, name, x=16, y=16, effect=None, doors=None, entrance=None):
        self.name = name
        self.x = x
        self.y = y
        self.effect = effect
        self.doors = doors
        self.entrance = entrance

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def change_door_position(self, idx, direction):
        self.doors[idx] = direction

    def get_door_position(self, idx):
        return self.doors[idx]

    def get_doors(self):
        return self.doors

    def get_entrance(self):
        return self.entrance

    def set_entrance(self, direction):
        self.entrance = direction

    def rotate_entrance(self):
        if self.entrance == model.Direction.UP:
            self.set_entrance(model.Direction.RIGHT)
            return
        if self.entrance == model.Direction.DOWN:
            self.set_entrance(model.Direction.LEFT)
            return
        if self.entrance == model.Direction.RIGHT:
            self.set_entrance(model.Direction.DOWN)
            return
        if self.entrance == model.Direction.LEFT:
            self.set_entrance(model.Direction.UP)
            return

    def rotate_tile(self):  # Will rotate the tile 1 position clockwise
        for door in self.doors:
            if door == model.Direction.UP:
                self.change_door_position(
                    self.doors.index(door), model.Direction.RIGHT)
            if door == model.Direction.RIGHT:
                self.change_door_position(
                    self.doors.index(door), model.Direction.DOWN)
            if door == model.Direction.DOWN:
                self.change_door_position(
                    self.doors.index(door), model.Direction.LEFT)
            if door == model.Direction.LEFT:
                self.change_door_position(
                    self.doors.index(door), model.Direction.UP)
