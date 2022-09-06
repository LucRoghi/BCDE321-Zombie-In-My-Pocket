import MapTile


def add_1_health(player):
    player.health += 1


def add_2_health(player):
    player.health += 2


def lose_1_health(player):
    player.health -= 1


def add_1_attack(player):
    player.attack += 1


def add_2_attack(player):
    player.attack += 2


def add_3_attack(player):
    player.attack += 3


def bury_totem(player):
    if player.has_totem:
        # win_logic
        pass


def add_zombies_to_room(zombie_number: int, tile: MapTile):
    tile.zombie_number = zombie_number
    return tile


def kill_all_zombies(player):
    player.current_location.zombie_number = 0


def get_new_item():
    pass
