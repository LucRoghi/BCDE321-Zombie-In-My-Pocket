import unittest

from Model.map_tile import MapTile


class MapTileTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_initial_maptile = MapTile("Test Room 1", None, True, False, True, False)
        self.adding_new_maptile = MapTile("Test Room UP", None, True, False, True, False)

    def test_print_maptile_object(self):
        self.assertEqual(self.test_initial_maptile.print_doors(), "up: True, right: False, down: True, left: False")

    def test_get_door_dict(self):
        self.assertEqual(self.test_initial_maptile.get_doors(),
                         {'down': True, 'left': False, 'right': False, 'up': True})

    def test_rotate_tile_left(self):
        self.test_initial_maptile.rotate_tile_left()
        self.assertEqual(self.test_initial_maptile.get_doors(),
                         {'down': False, 'left': True, 'right': True, 'up': False})

    def test_rotate_tile_right(self):
        self.test_initial_maptile.rotate_tile_right()
        self.assertEqual(self.test_initial_maptile.get_doors(),
                         {'down': False, 'left': True, 'right': True, 'up': False})

    def test_add_new_room_up_able(self):
        self.test_initial_maptile.add_new_room_up(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_up, self.adding_new_maptile)

    def test_add_new_room_up_unable(self):
        self.test_initial_maptile.rotate_tile_left()
        self.test_initial_maptile.add_new_room_up(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_up, None)

    def test_add_new_room_left_able(self):
        self.test_initial_maptile.rotate_tile_left()
        self.adding_new_maptile.rotate_tile_left()
        self.test_initial_maptile.add_new_room_left(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_left, self.adding_new_maptile)

    def test_add_new_room_left_unable(self):
        self.test_initial_maptile.add_new_room_left(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_left, None)

    def test_add_new_room_down_able(self):
        self.test_initial_maptile.add_new_room_down(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_down, self.adding_new_maptile)

    def test_add_new_room_down_unable(self):
        self.test_initial_maptile.rotate_tile_left()
        self.test_initial_maptile.add_new_room_down(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_down, None)

    def test_add_new_room_right_able(self):
        self.test_initial_maptile.rotate_tile_left()
        self.adding_new_maptile.rotate_tile_left()
        self.test_initial_maptile.add_new_room_right(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_right, self.adding_new_maptile)

    def test_add_new_room_right_unable(self):
        self.test_initial_maptile.add_new_room_right(self.adding_new_maptile)
        self.assertEqual(self.test_initial_maptile.room_right, None)


if __name__ == "__main__":
    unittest.main()
