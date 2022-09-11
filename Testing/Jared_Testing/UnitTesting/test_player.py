import unittest
from Model.player import Player


class TestPlayer(unittest.TestCase):
    def test_drop_item(self):
        Player.inventory = ["A", "B"]
        inv_len = len(Player.inventory)
        print(f"Player's currently holds {inv_len} item's")
        Player.drop_item(self=Player, index=1)
        self.assertIs(inv_len, 1, f"Player's currently holds {inv_len} item")
