from typing import Callable, Generic


class Item:
    def __init__(self, name, effect, can_combine, combines_with, uses):
        self.name: str = name
        self.effect: Callable = effect
        self.can_combine: bool = can_combine
        self.combines_with: Generic = combines_with
        self.uses: int = uses