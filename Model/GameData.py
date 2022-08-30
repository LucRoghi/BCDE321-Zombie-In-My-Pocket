from typing import List

from Model.DatabaseHandler import Database
from Model.MapTile import MapTile


def convert_tuples_to_maptile(tuple_list: tuple) -> list[MapTile]:
    tile_list = []
    for tile in tuple_list:
        room_name, effect, door_up, door_right, door_down, door_left = tile
        tile = MapTile(room_name, 0, effect, door_up, door_right, door_down, door_left)
        tile_list.append(tile)
    return tile_list


class GameData:
    def __init__(self):
        self.map_tiles_indoor = []
        self.map_tiles_outdoor = []
        self.dev_cards = []
        self.items = []

    def populate_map_tiles(self):
        db_connection = Database("ZombieInMyPocket.db")
        # GET ALL INDOOR TILES
        map_tuples = db_connection.query_data_from_table("map_tiles", "type", "indoor")
        self.map_tiles_indoor = convert_tuples_to_maptile(map_tuples)

        # GET ALL OUTDOOR TILES
        map_tuples = db_connection.query_data_from_table("map_tiles", "type", "outdoor")
        self.map_tiles_outdoor = convert_tuples_to_maptile(map_tuples)

    def populate_dev_cards(self):
        pass

    def populate_items(self):
        pass