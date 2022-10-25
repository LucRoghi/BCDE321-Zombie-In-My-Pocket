import unittest
import testing


class TestUsingItems(unittest.TestCase):
    def setUp(self):
        self.commands = testing.Commands()

    def test_using_soda_increases_health(self):
        self.commands.do_load("test_give_soda")
        self.commands.do_use("Can of Soda")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_health(), 8)

    def test_gasoline_and_chainsaw_gains_charge(self):
        self.commands.do_load("test_use_chainsaw_gasoline")
        self.commands.do_use("Chainsaw, Gasoline")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_items()[0][1], 4)

    def test_dropping_item_drops_item(self):
        self.commands.do_load("test_give_soda")
        self.commands.do_drop("Can of Soda")
        game = self.commands.get_game()
        self.assertEqual(len(game.get_player().get_items()), 0)

    def test_cant_use_invalid_item(self):
        self.commands.do_load("test_use_chainsaw_gasoline")
        self.commands.do_use("Chainsaw")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_items()[0][1], 2)

    def test_cant_use_item_not_in_inventory(self):
        self.commands.do_load("test_totem_pickup")
        self.commands.do_use("Chainsaw, Gasoline")
        game = self.commands.get_game()
        self.assertEqual(game.get_player().get_items()[0], ["Gasoline", 1])

    def test_pick_up_totem(self):
        self.commands.do_load("test_totem_pickup")
        self.commands.do_search("testing")
        game = self.commands.get_game()
        self.assertTrue(game.get_player().get_totem())

    def test_bury_totem_wins_game(self):
        self.commands.do_load("test_bury_totem")
        self.commands.do_bury("testing")
        game = self.commands.get_game()
        self.assertEqual(game.state, "Game Over")
