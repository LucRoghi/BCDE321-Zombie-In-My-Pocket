import dataclasses
from typing import Callable, Generic



class Item:
    def __init__(self):
        self.name = ""
        self.effect: Callable = None
        self.can_combine: bool = False
        self.combines_with: list[str] = None
        self.makes: list[str] = None
        self.uses: int = 0