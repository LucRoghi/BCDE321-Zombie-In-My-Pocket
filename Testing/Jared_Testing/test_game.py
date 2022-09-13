import unittest
from Model.game import GameController


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.test_game_controller = GameController()

    def test_intro_block(self):
        pass

    def test_game_start(self):
        pass

    def test_room_state_changes(self):
        pass

    def test_time_update(self):
        self.assertIs(len(self.test_game_controller.game_data.dev_cards), 0, self.test_game_controller.time_update())

    def test_player_status(self):
        pass

    def test_player_action_change(self):
        pass

    def test_player_item_cap(self):
        pass

    def test_win_con(self):
        pass

    def test_los_con(self):
        pass

    def player_select_tile_type(self):
        pass


if __name__ == "__main__":
    unittest.main()
