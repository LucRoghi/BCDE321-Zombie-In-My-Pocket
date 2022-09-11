"""
Author: Luc Roghi lcr0059
"""
import dataclasses
from typing import Callable, Generic


class Item:
    def __init__(self, name, effect, can_combine, combines_with, makes, uses):
        self.name = name
        self.effect: Callable = effect
        self.can_combine: bool = can_combine
        self.combines_with: list[str] = combines_with
        self.makes: list[str] = makes
        self.uses: int = uses

    def negate_damage(self, player):
        pass

    def add_1_attack(self, player):
        player.attack += 1

    def add_2_attack(self, player):
        player.attack += 2

    def add_3_attack(self, player):
        player.attack += 3

    def kill_all_zombies(self, player):
        player.current_location.zombie_number = 0