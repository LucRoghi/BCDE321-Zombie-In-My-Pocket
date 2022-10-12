import unittest
from os.path import exists

from View.commands import Commands


class TestUsingItems(unittest.TestCase):
    def setUp(self) -> None:
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