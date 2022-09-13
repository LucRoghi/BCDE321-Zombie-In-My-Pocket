import unittest

from Model.database_handler import Database
from Model.file_handler import Filehandler
from Model.player import Player
from Model.map_tile import MapTile
from Model.game_data import GameData
from Model.game import GameController


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_player = Player("Test")
        self.test_game_data = GameData()
        self.test_controller = GameController()
        self.database = Database("test.db")
        self.file_handler = Filehandler()
        self.previous_room = MapTile("Previous Room", None, True, True, True, True)
        self.a_room = MapTile("New Room", None, True, True, True, True)
        self.previous_room.zombie_number = 5
        self.test_player.current_location = self.previous_room
        self.test_player.health = 6
        self.test_player.can_cower = True
        self.test_player.can_flee = True
        self.test_player.can_attack = True

    # Passes
    def test_drop_item(self):
        self.test_player.inventory = ["A", "B"]
        self.test_player.drop_item(1)
        self.assertIs(len(self.test_player.inventory), 1, "Passed")

    # Technically Passes
    def test_flee(self):
        self.test_player.flee()
        self.assertIs(self.test_player.health, 1, "Flee Passed")

    # Passes
    def test_attack(self):
        self.test_player.player_attack()
        self.assertIs(self.test_player.health, 2, "Attack Passed")

    # Passes
    def test_cower_health_gain(self):
        self.test_player.cower()
        self.assertIs(self.test_player.health, 9, "Cower Passed")

    def test_cower_dev_card(self):
        old_dev_len = len(self.test_game_data.dev_cards())
        self.test_player.cower()
        new_dev_len = len(self.test_game_data.dev_cards())
        dev_len_compare = new_dev_len > old_dev_len
        self.assertIs(dev_len_compare, True, "Passed")
        pass

    def test_cower_time_change(self):
        cur_time = self.test_controller.time
        self.test_player.cower()
        new_time = self.test_controller.time_update()
        time_compare = new_time > cur_time
        self.assertIs(time_compare, True, "Passed")

    # Fails
    def test_move_up(self):
        self.test_player.move_player_up()
        self.assertIs(self.test_player.current_location, self.a_room)

    # Fails
    def test_move_right(self):
        self.test_player.move_player_right()
        self.assertIs(self.test_player.current_location, self.a_room)

    # Fails
    def test_move_down(self):
        self.test_player.move_player_down()
        self.assertIs(self.test_player.current_location, self.a_room)

    # Fails
    def test_move_left(self):
        self.test_player.move_player_left()
        self.assertIs(self.test_player.current_location, self.a_room)


if __name__ == "__main__":
    unittest.main()
