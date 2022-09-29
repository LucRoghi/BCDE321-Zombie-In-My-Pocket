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
