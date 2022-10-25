import unittest
import testing


class TestPlayerAttacks(unittest.TestCase):
    def setUp(self) -> None:
        self.commands = testing.Commands()

    def test_player_attacks_with_no_weapon(self):
        self.commands.do_load("test_chainsaw_gasoline")
        self.commands.do_attack("")
        game = self.commands.get_game()
        player = game.get_player()
        self.assertEqual(player.get_health(), 3)

    def test_player_attacks_with_weapon(self):
        self.commands.do_load("test_chainsaw_gasoline")
        self.commands.do_attack("Chainsaw")
        game = self.commands.get_game()
        player = game.get_player()
        self.assertEqual(player.get_health(), 6)

    def test_player_cant_attack_with_two_weapons(self):
        self.commands.do_load("test_two_weapons")
        self.commands.do_attack("Machete, Golf Club")
        game = self.commands.get_game()
        self.assertEqual(game.state, "Attacking")

    def test_attack_with_chainsaw_loses_one_charge(self):
        self.commands.do_load("test_chainsaw_gasoline")
        self.commands.do_attack("Chainsaw")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_items()[0][1], 1)

    def test_attack_with_gas_and_chainsaw_gains_charge(self):
        self.commands.do_load("test_chainsaw_gasoline")
        self.commands.do_attack("Chainsaw, Gasoline")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_items()[0][1], 3)

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
