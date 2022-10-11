from View.commands import Commands
from Controller.game import Game


class TestGameCreation(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()
        self.game = Game()

    def test_start_makes_new_game(self):
        self.commands.do_start(None)
        self.commands.do_place(None)
        current_tile = self.game.get_current_tile()
        self.assertEqual(current_tile.get_name(), "Foyer")

    def test_load_creates_loaded_game(self):
        pass

    def test_save_saves_current_game(self):
        pass

    def test_restart_restarts_game(self):
        pass


# TODO Make a load of 'Pre Saved' Games
class TestPlayerMovement(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()
        self.commands.do_load(None)

    def test_player_moves_north(self):
        pass

    def test_player_moves_east(self):
        pass

    def test_player_moves_south(self):
        pass

    def test_player_moves_west(self):
        pass

    def test_player_moves_dining_room_to_patio(self):
        pass

    # TODO - Actually implement this
    def test_zombie_breaks_through_walls(self):
        pass

    def test_player_cower_works(self):
        pass


class TestPlayerAttacks(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()

    def test_player_attacks_with_no_weapon(self):
        pass

    def test_player_attacks_with_weapon(self):
        pass

    def test_player_cant_attack_with_two_weapons(self):
        pass

    def test_attack_with_chainsaw_loses_one_charge(self):
        pass

    def test_attack_with_gas_and_chainsaw_gains_charge(self):
        pass

    def test_attack_with_soda_gains_health(self):
        pass

    def test_attack_with_candle_gasoline_kills_zombies(self):
        pass

    def test_attack_with_candle_oil_kills_zombies(self):
        pass

    def test_cant_use_invalid_item(self):
        pass

    def test_attack_with_oil_runs_away(self):
        pass

    def test_cant_attack_with_item_not_in_inventory(self):
        pass

    def test_run_away(self):
        pass


class TestUsingItems(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()

    def test_using_soda_increases_health(self):
        pass

    def test_gasoline_and_chainsaw_gains_charge(self):
        pass

    def test_dropping_item_drops_item(self):
        pass

    def test_cant_use_invalid_item(self):
        pass

    def test_cant_use_item_not_in_inventory(self):
        pass

    def test_pick_up_totem(self):
        pass

    def test_bury_totem_wins_game(self):
        pass


if __name__ == "__main__":
    unittest.main()
