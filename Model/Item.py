import dataclasses
from typing import Callable, Generic


@dataclasses
class Item:
    name: str = ""
    effect: Callable = None
    can_combine: bool = False
    combines_with: list[str] = None
    makes: list[str] = None
    uses: int = 0