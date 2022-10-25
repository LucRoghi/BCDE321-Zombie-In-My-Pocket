import abfac
from abc import ABCMeta


class Tile(metaclass=ABCMeta):
    def __init__(
            self, name, x=16, y=16, effect=None, doors=None, entrance=None
    ):
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
        if self.entrance == abfac.Direction.UP:
            self.set_entrance(abfac.Direction.RIGHT)
            return
        elif self.entrance == abfac.Direction.DOWN:
            self.set_entrance(abfac.Direction.LEFT)
            return
        elif self.entrance == abfac.Direction.RIGHT:
            self.set_entrance(abfac.Direction.DOWN)
            return
        else:
            self.set_entrance(abfac.Direction.UP)
            return

    # Will rotate the tile one position clockwise
    def rotate_tile(self):
        for door in self.doors:
            if door == abfac.Direction.UP:
                self.change_door_position(
                    self.doors.index(door), abfac.Direction.RIGHT)
            if door == abfac.Direction.RIGHT:
                self.change_door_position(
                    self.doors.index(door), abfac.Direction.DOWN)
            if door == abfac.Direction.DOWN:
                self.change_door_position(
                    self.doors.index(door), abfac.Direction.LEFT)
            if door == abfac.Direction.LEFT:
                self.change_door_position(
                    self.doors.index(door), abfac.Direction.UP)
