

import dataclasses
from typing import Callable, Generic

from Model import Level, Player
from Model.Level import MapTile


@dataclasses
class Item:
    name: str = ""
    effect: Callable = None
    can_combine: bool = False
    combines_with: Generic = None


@dataclasses
class DevCard:
    nine_oclock: Callable = None
    ten_oclock: Callable = None
    eleven_oclock: Callable = None


def set_room_zombies(player_location: MapTile, zombie_number: int):
    player_location.zombie_number = zombie_number


def decrease_player_health(player: Player, amount: int):
    if amount <= 0:
        raise ValueError("Amount to decrease cannot be less than or equal to 0")
    else:
        player.health -= amount


def increase_player_health(player: Player, amount: int):
    if amount <= 0:
        raise ValueError("Amount to decrease cannot be less than or equal to 0")
    else:
        player.health += amount


def increase_player_attack(player: Player, amount: int):
    if amount <= 0:
        raise ValueError("Amount to decrease cannot be less than or equal to 0")
    else:
        player.attack += amount


def decrease_player_attack(player: Player, amount: int):
    if amount <= 0:
        raise ValueError("Amount to decrease cannot be less than or equal to 0")
    else:
        player.attack -= amount
