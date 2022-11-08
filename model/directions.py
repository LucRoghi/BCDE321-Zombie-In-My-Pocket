"""
Author: Jared Ireland jai0095

ENUM for the directions the player can move and where the tiles can be placed
"""
import enum


class Direction(enum.Enum):
    UP = 1,
    RIGHT = 3,
    DOWN = 2,
    LEFT = 4
