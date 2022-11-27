import unittest

from Model.game_data import *


class GameDataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.game_data = GameData()
        self.game_data.reset_database()

    def test_default_maptiles_indoor_empty(self):
        self.assertEqual(self.game_data.map_tiles_indoor, [])

    def test_default_maptiles_outdoor_empty(self):
        self.assertEqual(self.game_data.map_tiles_outdoor, [])

    def test_default_maptiles_devcards_empty(self):
        self.assertEqual(self.game_data.dev_cards, [])

    def test_default_item_emtpy(self):
        self.assertEqual(self.game_data.items, [])

    def test_connected_to_db(self):
        self.assertEqual(self.game_data.database.db_name, "ZombieInMyPocket.db")

    def test_initialize_game_data(self):
        self.game_data.initialize_game_data()
        self.assertNotEqual(len(self.game_data.map_tiles_indoor), 0)
        self.assertNotEqual(len(self.game_data.map_tiles_outdoor), 0)
        self.assertNotEqual(len(self.game_data.dev_cards), 0)
        self.assertNotEqual(len(self.game_data.items), 0)

    def test_add_maptiles_to_db(self):
        result = self.game_data.database.cursor.execute("SELECT * FROM Maptiles").fetchall()
        self.assertEqual(result, [
            (0, 'Garden', 'add_1_health', 'False', 'True', 'True', 'True', 'Outdoor'),
            (1, 'Sitting Area', 'None', 'False', 'True', 'True', 'True', 'Outdoor'),
            (2, 'Yard1', 'None', 'False', 'True', 'True', 'True', 'Outdoor'),
            (3, 'Yard2', 'None', 'False', 'True', 'True', 'True', 'Outdoor'),
            (4, 'Yard3', 'None', 'False', 'True', 'True', 'True', 'Outdoor'),
            (5, 'Graveyard', 'bury_totem', 'False', 'True', 'True', 'False', 'Outdoor'),
            (6, 'Garage', 'None', 'False', 'False', 'True', 'True', 'Outdoor'),
            (7, 'Patio', 'enter_indoors', 'True', 'True', 'True', 'False', 'Outdoor'),
            (8, 'Bathroom', 'None', 'True', 'False', 'False', 'False', 'Indoor'),
            (9, 'Kitchen', 'add_1_health', 'True', 'True', 'False', 'False', 'Indoor'),
            (10, 'Storage', 'find_an_item', 'True', 'False', 'False', 'False', 'Indoor'),
            (11, 'Evil Temple', 'find_totem', 'False', 'True', 'False', 'True', 'Indoor'),
            (12, 'Family Room', 'None', 'True', 'True', 'False', 'True', 'Indoor'),
            (13, 'Dining Room', 'enter_outdoors', 'True', 'True', 'True', 'True', 'Indoor'),
            (14, 'Bedroom', 'None', 'True', 'False', 'False', 'True', 'Indoor'),
            (15, 'Foyer', 'None', 'True', 'False', 'False', 'False', 'Indoor')
        ])

    def test_add_devcards_to_db(self):
        result = self.game_data.database.cursor.execute("SELECT * FROM Devcards").fetchall()
        self.assertEqual(result, [
            (0, 'You try hard no to wet yourself', 'None', 'None', 'get_new_item', 'None', '6', 'Oil'),
            (1, 'None', '4', 'You sense your impending doom', 'lose_1_health', 'None', 'get_new_item', 'Gasoline'),
            (2, 'None', 'get_new_item', 'None', '4', 'Something icky in your mouth', 'lose_1_health', 'Board with Nails'),
            (3, 'None', '4', 'A bat poops in your eye', 'lose_1_health', 'None', '6', 'Machete'),
            (4, 'None', 'get_new_item', 'None', '5', "Your soul isn't wanted here", 'lose_1_health', 'Grisly Femur'),
            (5, 'Slip on nasty goo', 'lose_1_health', 'None', '4', 'The smell of blood is in the air', 'None', 'Golf '
                                                                                                               'Club'),
            (6, 'None', '3', 'You hear terrible screams', 'None', 'None', '5', 'Chainsaw'),
            (7, 'Candybar in your pocket', 'add_1_health', 'None', 'get_new_item', 'None', '4', 'Can of Soda'),
            (8, 'Your body shiver uncontrollably', 'None', 'You feel a spark of hope', 'add_1_health', 'None', '4','Candle')
        ])

    def test_add_items_to_db(self):
        result = self.game_data.database.cursor.execute("SELECT * FROM Items").fetchall()
        self.assertEqual(result, [
            (0, 'Oil', 'negate_damage', 'True', 'Candle', 'None', 'Oil with Candle', 'None', 1),
            (1, 'Gasoline', 'None', 'True', 'Candle', 'Chainsaw', 'Oil with Candle', 'Filled Chainsaw', 1),
            (2, 'Board w/ Nails', 'add_1_attack', 'False', 'None', 'None', 'None', 'None', 1),
            (3, 'Can of Soda', 'add_2_health', 'False', 'None', 'None', 'None', 'None', 1),
            (4, 'Grisly Femur', 'add_1_attack', 'False', 'None', 'None', 'None', 'None', 1),
            (5, 'Golf Club', 'add_1_attack', 'False', 'None', 'None', 'None', 'None', 1),
            (6, 'Candle', 'None', 'True', 'Oil', 'Gasoline', 'Oil with Candle', 'Gasoline with Candle', 1),
            (7, 'Chainsaw', 'add_3_attack', 'True', 'Gasoline', 'None', 'Chainsaw', 'None', 2),
            (8, 'Machete', 'add_2_attack', 'False', 'None', 'None', 'None', 'None', 1),
            (9, 'Oil with Candle', 'kill_all_zombies', 'False', 'None', 'None', 'None', 'None', 1),
            (10, 'Gasoline with Candle', 'kill_all_zombies', 'False', 'None', 'None', 'None', 'None', 1),
            (11, 'Totem', 'None', 'False', 'None', 'None', 'None', 'None', 1)
        ])

    def test_get_maptiles_indoors_count(self):
        self.game_data.initialize_game_data()
        self.assertEqual(len(self.game_data.map_tiles_indoor), 8)

    def test_get_maptiles_outdoors_count(self):
        self.game_data.initialize_game_data()
        self.assertEqual(len(self.game_data.map_tiles_outdoor), 8)

    def test_get_devcards_count(self):
        self.game_data.initialize_game_data()
        self.assertEqual(len(self.game_data.dev_cards), 9)

    def test_get_item_count(self):
        self.game_data.initialize_game_data()
        self.assertEqual(len(self.game_data.items), 12)

    def test_dev_card_pop(self):
        self.game_data.initialize_game_data()
        before_pop_count = len(self.game_data.dev_cards)
        self.game_data.dev_card_pop()
        after_pop_count = len(self.game_data.dev_cards)
        self.assertEqual(before_pop_count - after_pop_count, 1)

    def test_str_to_bool_true(self):
        self.assertEqual(str_to_bool("True"), True)

    def test_str_to_bool_false(self):
        self.assertEqual(str_to_bool("False"), False)