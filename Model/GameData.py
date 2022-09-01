from typing import List

from Model.DatabaseHandler import Database
from Model.Filehandler import Filehandler
from Model.MapTile import MapTile


def convert_tuples_to_maptile(tuple_list: tuple) -> list[MapTile]:
    tile_list = []
    for tile in tuple_list:
        _, room_name, effect, door_up, door_right, door_down, door_left, type = tile
        tile = MapTile(room_name, effect, door_up, door_right, door_down, door_left)
        tile_list.append(tile)
    return tile_list


class GameData:
    def __init__(self):
        self.map_tiles_indoor = []
        self.map_tiles_outdoor = []
        self.dev_cards = []
        self.items = []
        self.database = Database("ZombieInMyPocket.db")
        self.file_handler = Filehandler()

    def populate_db(self):
        # Maptile Insert
        maptile_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "maptiles")
        self.database.create_new_table("Maptiles", maptile_table)
        self.database.insert_tile_data()

        # Dev card Insert
        dev_card_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "items")
        self.database.create_new_table("Items", dev_card_table)
        self.database.insert_dev_card_data()

    def populate_map_tiles(self):
        # GET ALL INDOOR TILES
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Indoor")
        self.map_tiles_indoor = convert_tuples_to_maptile(map_tuples)

        # GET ALL OUTDOOR TILES
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Outdoor")
        self.map_tiles_outdoor = convert_tuples_to_maptile(map_tuples)

    def populate_dev_cards(self):
        pass

    def populate_items(self):
        pass


if __name__ == "__main__":
    test_game_data = GameData()
    test_game_data.database.delete_all_rows_in_db("Maptiles")
    test_game_data.populate_db()
    test_game_data.populate_map_tiles()
