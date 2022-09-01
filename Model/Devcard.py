from typing import Callable

class Devcard:
    def __init__(self, zombie_number, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect):
        zombie_number = zombie_number
        nine_oclock_message = nine_message
        nine_oclock: Callable = nine_effect
        ten_oclock_message = ten_message
        ten_oclock: Callable = ten_effect
        eleven_oclock_message = eleven_message
        eleven_oclock: Callable = eleven_effect