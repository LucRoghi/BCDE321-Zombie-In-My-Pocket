import unittest
from Model.player import Player
from Model.map_tile import MapTile


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_player = Player("Test")
        self.test_initial_maptile = MapTile("Test Room 1", None, True, False, True, False)
        self.adding_new_maptile = MapTile("Test Room UP", None, True, False, True, False)

    # Passes
    def test_drop_item(self):
        self.test_player.inventory = ["A", "B"]
        self.test_player.drop_item(1)
        self.assertIs(len(self.test_player.inventory), 1, "Passed")

    # Fails
    def test_flee(self):
        self.test_player.current_location.zombie_number = 5
        self.assertIs(self.test_player.flee(), 1, "Passed")

    # Fails
    def test_attack(self):
        self.test_player.current_location.zombie_number = 5
        self.assertIs(self.test_player.player_attack(), 2, "Passed")

    # Fails
    def test_cower(self):
        self.test_player.current_location.zombie_number = 5
        self.assertIs(self.test_player.cower(), 9, "Passed")

    # Fails
    def test_move_up(self):
        self.test_initial_maptile.add_new_room_up(self.adding_new_maptile)
        self.test_player.move_player_up()
        self.assertEqual(self.test_player.current_location, self.adding_new_maptile)

    # Fails
    def test_move_right(self):
        self.test_initial_maptile.add_new_room_right(self.adding_new_maptile)
        self.test_player.move_player_right()
        self.assertEqual(self.test_player.current_location, self.adding_new_maptile)

    # Fails
    def test_move_down(self):
        self.test_initial_maptile.add_new_room_down(self.adding_new_maptile)
        self.test_player.move_player_down()
        self.assertEqual(self.test_player.current_location, self.adding_new_maptile)

    # Fails
    def test_move_left(self):
        self.test_initial_maptile.add_new_room_left(self.adding_new_maptile)
        self.test_player.move_player_left()
        self.assertEqual(self.test_player.current_location, self.adding_new_maptile)


if __name__ == "__main__":
    unittest.main()
