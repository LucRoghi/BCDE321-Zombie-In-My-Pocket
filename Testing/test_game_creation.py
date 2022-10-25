import unittest
from os.path import exists
import testing


class TestGameCreation(unittest.TestCase):
    def setUp(self) -> None:
        self.commands = testing.Commands()

    def test_start_creates_new_game(self):
        self.commands.do_start(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        current_tile = game.get_current_tile()
        self.assertEqual(current_tile.get_name(), "Foyer")

    def test_load_creates_loaded_game(self):
        self.commands.do_load("../save/test_move.db.dat")
        game = self.commands.get_game()
        player_pos = game.get_player_x(), game.get_player_y()
        self.assertEqual(player_pos, (16, 16))

    def test_save_saves_current_game(self):
        self.commands.do_start(None)
        self.commands.do_place(None)
        self.commands.do_save("test_saving")
        self.assertTrue(exists("../save/test_saving.db.dat"))
        pass

    def test_restart_restarts_game(self):
        self.commands.do_start(None)
        self.commands.do_load("test_bury_totem")
        self.commands.do_restart(None)
        self.commands.do_start(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        current_tile = game.get_current_tile()
        self.assertEqual(current_tile.get_name(), "Foyer")


if __name__ == "__main__":
    unittest.main()
