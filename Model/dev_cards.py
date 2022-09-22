"""
Author: Luc Roghi lcr0059
"""
from typing import Callable


class Devcard:
    def __init__(self, zombie_number, nine_message, nine_effect,
                 ten_message, ten_effect, eleven_message, eleven_effect, item):
        self.zombie_number: int = zombie_number
        self.nine_oclock_message: str = nine_message
        self.nine_oclock_effect: str = nine_effect
        self.ten_oclock_message: str = ten_message
        self.ten_oclock_effect: str = ten_effect
        self.eleven_oclock_message: str = eleven_message
        self.eleven_oclock_effect: str = eleven_effect
        self.item: str = item