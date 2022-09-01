import dataclasses

from Model.MapTile import MapTile


@dataclasses
class Player:
    name: str = ""
    current_location: MapTile = None
    attack: int = 1
    health: int = 6
    inventory = []
    has_totem: bool = None

