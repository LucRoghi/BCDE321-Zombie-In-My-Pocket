from typing import Callable
from Model.player import Player


class Devcard:
    def __init__(self, zombie_number, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect):
        self.zombie_number = zombie_number
        self.nine_oclock_message = nine_message
        self.nine_oclock: Callable = self.set_effect(nine_effect)
        self.ten_oclock_message = ten_message
        self.ten_oclock: Callable = self.set_effect(ten_effect)
        self.eleven_oclock_message = eleven_message
        self.eleven_oclock: Callable = self.set_effect(eleven_effect)

    def set_effect(self, effect_string):
        if effect_string.isnumeric():
            self.zombie_number = int(effect_string)
            return getattr(Devcard, 'add_zombies_to_room')
        elif effect_string == 'None':
            return None
        else:
            self.zombie_number = 0
            return getattr(Devcard, effect_string, None)

    def add_zombies_to_room(self, player: Player, zombie_number):
        player.current_location.zombie_number = zombie_number

    def lose_1_health(self, player, _):
        player.health -= 1

    def add_1_health(self, player, _):
        player.health += 1

    def get_new_item(self, player, _):
        if player.inventory < 2:


if __name__ == "__main__":
    test_devcard = Devcard(0, "", "", "", "", "", "")
    test_func = getattr(Devcard, 'add_zombies_to_room')
    print(test_func)
