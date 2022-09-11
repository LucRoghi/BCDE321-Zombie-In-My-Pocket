import unittest
from Model.player import Player


class TestPlayer(unittest.TestCase):

    def test_drop_item(self):
        p = Player()
        p.inventory = ["A", "B"]
        inv_len = len(p.inventory)
        print(f"Player's currently holds {inv_len} item's")
        p.drop_item(1)
        self.assertIs(inv_len, 1, "Passed")

