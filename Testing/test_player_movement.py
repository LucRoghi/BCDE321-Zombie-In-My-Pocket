import unittest
import testing


class TestPlayerMovement(unittest.TestCase):
    def setUp(self) -> None:
        self.commands = testing.Commands()
        self.commands.do_load("test_move")

    def test_player_moves_north(self):
        self.commands.do_move("up")
        self.commands.do_rotate(None)
        self.commands.do_rotate(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        player_pos = game.get_player_x(), game.get_player_y()
        self.assertEqual(player_pos, (15, 14))

    def test_player_moves_south(self):
        self.commands.do_move("down")
        self.commands.do_rotate(None)
        self.commands.do_rotate(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        player_pos = game.get_player_x(), game.get_player_y()
        self.assertEqual(player_pos, (15, 16))

    def test_player_moves_east(self):
        self.commands.do_move("right")
        self.commands.do_place(None)
        game = self.commands.get_game()
        player_pos = game.get_player_x(), game.get_player_y()
        self.assertEqual(player_pos, (15, 15))

    def test_player_moves_west(self):
        self.commands.do_move("left")
        self.commands.do_rotate(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        player_pos = game.get_player_x(), game.get_player_y()
        self.assertEqual(player_pos, (14, 15))

    def test_north_from_dining_room_goes_to_patio(self):
        self.commands.do_move("up")
        self.commands.do_rotate(None)
        self.commands.do_rotate(None)
        self.commands.do_place(None)
        game = self.commands.get_game()
        current_tile = game.get_current_tile()
        self.assertEqual(current_tile.get_name(), "Patio")

    def test_zombies_break_through_wall(self):
        self.commands.do_load("test_zombie_break_wall")
        self.commands.do_choose("up")
        game = self.commands.get_game()
        self.assertEqual(game.state, "Attacking")

    def test_cower_gains_health(self):
        self.commands.do_cower(None)
        game = self.commands.get_game()
        player = game.get_player()
        self.assertEqual(player.get_health(), 7)
