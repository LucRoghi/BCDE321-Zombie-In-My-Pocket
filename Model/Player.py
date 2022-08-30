import dataclasses

from Model.Cards import Item
from Model.MapTile import MapTile


@dataclasses
class Player:
    name: str = ""
    current_location: MapTile = None
    attack: int = 1
    health: int = 6
    items_1: Item = None
    items_2: Item = None
    has_totem: bool = None

