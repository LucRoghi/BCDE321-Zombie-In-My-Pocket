"""
Author: Luc Roghi lcr0059
"""


class Devcard:
    def __init__(self, nine_message, nine_effect,
                 ten_message, ten_effect, eleven_message, eleven_effect, item):
        self.time_nine: tuple = (nine_message, nine_effect)
        self.time_ten: tuple = (ten_message, ten_effect)
        self.time_eleven: tuple = (eleven_message, eleven_effect)
        self.item: str = item
