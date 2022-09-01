import MapTile


def add_1_health(player):
    player.health += 1


def lose_1_health(player):
    player.health -= 1


def bury_totem(player):
    if player.has_totem:
        # win_logic
        pass


def draw_new_card():
    pass


def add_zombies_to_room(zombie_number: int, tile: MapTile):
    pass

def get_new_item():
    pass