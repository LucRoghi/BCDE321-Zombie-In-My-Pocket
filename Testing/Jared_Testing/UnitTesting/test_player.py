import unittest
from Model.player import Player


class TestPlayer(unittest.TestCase):

    def test_drop_item(self):
        p = Player()
        p.inventory = ["A", "B"]
        print(f"Player's currently holds {len(p.inventory)} item's")
        print("Testing Running...")
        p.drop_item(1)
        self.assertIs(len(p.inventory), 1, "Passed")
        print(f"Player's currently holds {len(p.inventory)} item's")

