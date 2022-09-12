import unittest
from Model.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_player = Player("Test")

    def test_drop_item(self):
        p = Player()
        p.inventory = ["A", "B"]
        p.drop_item(1)
        self.assertIs(len(p.inventory), 1, "Passed")

    def test_flee(self):
        p = Player()
        p.current_location.zombie_number = 5
        self.assertIs(p.flee(), 1, "Passed")

    def test_attack(self):
        p = Player()
        p.current_location.zombie_number = 5
        self.assertIs(p.player_attack(), 2, "Passed")

    def test_cower(self):
        p = Player()
        p.current_location.zombie_number = 5
        self.assertIs(p.cower(), 9, "Passed")
