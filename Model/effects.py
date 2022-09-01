import Player
import MapTile


def add_1_health(player: Player):
    player.health += 1


def lose_1_health(player: Player):
    player.health -= 1


def bury_totem(player: Player):
    if player.has_totem:
        # win_logic
        pass


def draw_new_card():
    pass


def add_zombies_to_room(zombie_number: int, tile: MapTile):
    pass
