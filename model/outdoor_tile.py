"""
Author: Jared Ireland jai0095

Outdoor Tile setup
"""
import model


class OutdoorTile(model.Tile):
    """
    >>> from model.tile
    >>> from model.directions import Direction
    >>> tile = OutdoorTile("Graveyard", x=0, y=0)
    >>> tile.get_name()
    'Graveyard'
    >>> print(tile)
    Graveyard, [], Outdoor, 0, 0, None
    >>> tile.set_entrance(Direction.DOWN)
    >>> tile.get_entrance()
    <Direction.DOWN: (2,)>
    >>> tile.rotate_entrance()
    >>> tile.rotate_entrance()
    >>> tile.get_entrance()
    <Direction.UP: (1,)>
    >>> tile.set_x(10)
    >>> tile.set_y(15)
    >>> tile.get_x()
    10
    >>> tile.get_y()
    15
    """

    def __init__(self, name, effect=None, doors=None, x=16, y=16, entrance=None):
        if doors is None:
            doors = []
        self.type = "Indoor"
        super().__init__(name, x, y, effect, doors, entrance)

    def __repr__(self):
        return f"{self.name}, {self.doors}, {self.type}, {self.x}, {self.y}, {self.effect}"