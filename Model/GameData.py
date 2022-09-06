from typing import List

from Model.Devcard import Devcard
from Model.DatabaseHandler import Database
from Model.Filehandler import Filehandler
from Model.Item import Item
from Model.MapTile import MapTile


def convert_tuples_to_maptile(tuple_list: tuple) -> list[MapTile]:
    tile_list = []
    for tile in tuple_list:
        _, room_name, effect, door_up, door_right, door_down, door_left, type = tile
        tile = MapTile(room_name, effect, door_up, door_right, door_down, door_left)
        tile.effect = getattr(tile, effect, None)
        tile_list.append(tile)
    return tile_list


def convert_tuples_to_dev_card(tuple_list: tuple) -> list[Devcard]:
    devcard_list = []
    for card in tuple_list:
        _, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect, item = card
        dev_card = Devcard(0, nine_message, nine_effect, ten_message, ten_effect,
                           eleven_message, eleven_effect)

        if nine_effect.isnumeric():
            dev_card.zombie_number = nine_effect
            dev_card.nine_effect = getattr(dev_card, "add_zombies_to_room")
        elif ten_effect.isnumeric():
            dev_card.zombie_number = ten_effect
            dev_card.ten_effect = getattr(dev_card, "add_zombies_to_room")
        elif eleven_effect.isnumeric():
            dev_card.zombie_number = eleven_effect
            dev_card.eleven_effect = getattr(Devcard, "add_zombies_to_room")
        else:
            dev_card.nine_effect = None
            dev_card.ten_effect = None
            dev_card.eleven_effect = None
            dev_card.zombie_number = 0

        if nine_effect != (None or 'add_zombies_to_room'):
            dev_card.nine_effect = getattr(Devcard, str(nine_effect), None)

        if ten_effect != (None or 'add_zombies_to_room'):
            dev_card.ten_effect = getattr(Devcard, str(ten_effect), None)

        if eleven_effect != (None or 'add_zombies_to_room'):
            dev_card.eleven_effect = getattr(Devcard, str(eleven_effect), None)

        devcard_list.append(dev_card)
    return devcard_list


def convert_tuples_to_items(tuple_list: tuple) -> list[Item]:
    item_list = []
    for item in tuple_list:
        _, name, effect, can_combine, combines_with_1, combines_with_2, makes_1, makes_2, uses = item
        new_item = Item(name, effect, can_combine, [combines_with_1, combines_with_2], [makes_1, makes_2], uses)
        new_item.effect = getattr(new_item, effect, None)
        item_list.append(new_item)
    return item_list


class GameData:
    def __init__(self):
        self.map_tiles_indoor = []
        self.map_tiles_outdoor = []
        self.dev_cards = []
        self.items = []
        self.database = Database("ZombieInMyPocket.db")
        self.file_handler = Filehandler()

    def initialize_game_data(self):
        self.get_map_tiles()
        self.get_dev_cards()
        self.get_items()

    def populate_db(self):
        # Maptile Insert
        maptile_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "maptiles")
        self.database.create_new_table("Maptiles", maptile_table)
        self.database.insert_tile_data()
        self.database.commit_db()

        # Dev card Insert
        dev_card_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "dev_cards")
        self.database.create_new_table("Devcards", dev_card_table)
        self.database.insert_dev_card_data()
        self.database.commit_db()

        # Item insert
        item_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "items")
        self.database.create_new_table("Items", item_table)
        self.database.insert_item_data()
        self.database.commit_db()

    def get_map_tiles(self):
        # GET ALL INDOOR TILES
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Indoor")
        self.map_tiles_indoor = convert_tuples_to_maptile(map_tuples)

        # GET ALL OUTDOOR TILES
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Outdoor")
        self.map_tiles_outdoor = convert_tuples_to_maptile(map_tuples)

    def get_dev_cards(self):
        dev_card_tuples = self.database.query_all_data_from_table("Devcards")
        self.dev_cards = convert_tuples_to_dev_card(dev_card_tuples)

    def get_items(self):
        item_tuples = self.database.query_all_data_from_table("Items")
        self.items = convert_tuples_to_items(item_tuples)


if __name__ == "__main__":
    test_game_data = GameData()
    test_game_data.database.drop_table_in_db("Maptiles")
    test_game_data.database.drop_table_in_db("Devcards")
    test_game_data.database.drop_table_in_db("Items")
    test_game_data.populate_db()
    test_game_data.initialize_game_data()
