"""
Author: Jared Ireland jai0095

Indoor Tile setup
"""
import Model


class IndoorTile(Model.Tile):
    """
    >>> from Model.tile import Tile
    >>> from Model.directions import Direction
    >>> tile = IndoorTile("Family Room", x=0, y=0)
    >>> tile.get_name()
    'Family Room'
    >>> print(tile)
    Family Room, [], Indoor, 0, 0, None
    >>> tile.set_entrance(Direction.UP)
    >>> tile.get_entrance()
    <Direction.UP: (1,)>
    >>> tile.rotate_entrance()
    >>> tile.get_entrance()
    <Direction.RIGHT: (3,)>
    >>> tile.set_x(1)
    >>> tile.set_y(1)
    >>> tile.get_x()
    1
    >>> tile.get_y()
    1
    """

    def __init__(self, name, effect=None, doors=None, x=16, y=16, entrance=None):
        if doors is None:
            doors = []
        self.type = "Indoor"
        super().__init__(name, x, y, effect, doors, entrance)

    def __repr__(self):
        return f"{self.name}, {self.doors}, {self.type}, {self.x}, {self.y}, {self.effect}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
