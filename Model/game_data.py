"""
Author: Luc Roghi lcr0059

Game Data is a class designed to hold all the instantiated object being used within the game. The items are converted
from string format to object format within the 3 static methods at the top of the file.

GAME DATA MAPTILES:
        >>> test_game_data = GameData()
        >>> print(len(test_game_data.map_tiles_indoor))
        8
        >>> print(test_game_data.map_tiles_indoor) #doctest: +ELLIPSIS
        [<Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object
        at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile
         object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>]
        >>> print(test_game_data.map_tiles_indoor[-1])
        Foyer Available Doors [UP LEFT DOWN RIGHT ]
        >>> print(test_game_data.map_tiles_indoor[0].room_name)
        Bathroom
        >>> test_game_data.map_tiles_outdoor[0].get_doors()
        {'up': 'False', 'right': 'True', 'down': 'True', 'left': 'True'}
        >>> test_game_data.map_tiles_outdoor[0].rotate_tile_left()
        >>> test_game_data.map_tiles_outdoor[0].get_doors()
        {'up': 'True', 'right': 'True', 'down': 'True', 'left': 'False'}
        >>> test_game_data.map_tiles_outdoor[0].rotate_tile_right()
        >>> test_game_data.map_tiles_outdoor[0].get_doors()
        {'up': 'False', 'right': 'True', 'down': 'True', 'left': 'True'}

GAME DATA DEVCARDS:
        >>> print(len(test_game_data.dev_cards))
        9
        >>> print(test_game_data.dev_cards) #doctest: +ELLIPSIS
        [<Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard obje
        ct at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.D
        evcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.
        dev_cards.Devcard object at ...>]
        >>> print(test_game_data.dev_cards[0]) #doctest: +ELLIPSIS
        <Model.dev_cards.Devcard object at ...>
"""

from random import randint

from Model.CardConverter.CardConverter import CardConverter
from Model.CardConverter.ConvertDevCards import ConvertDevCards
from Model.CardConverter.ConvertMaptiles import ConvertMaptiles
from Model.CardConverter.ConvertItems import ConvertItems
from Model.dev_cards import Devcard
from Model.database_handler import Database
from Model.file_handler import Filehandler
from Model.item import Item
from Model.map_tile import MapTile


def str_to_bool(string: str) -> bool:
    return string.lower() in "true"


class GameData:
    def __init__(self):
        self.map_tiles_indoor: list[MapTile] = []
        self.map_tiles_outdoor: list[MapTile] = []
        self.dev_cards: list[Devcard] = []
        self.items: list[Item] = []
        self.database: Database = Database("ZombieInMyPocket.db")
        self.card_converter = CardConverter()
        self.file_handler: Filehandler = Filehandler()
        self.reset_database()

    def reset_database(self):
        """
        :return:
        """
        self.database.delete_database()
        self.database = Database("ZombieInMyPocket.db")
        self.populate_db()

    def initialize_game_data(self):
        """
        Imports the data from the database and converts them into the respective objects to be stored within game data
        get_map_tiles_indoors populates the self.map_tiles_indoors list
        get_map_tiles_outdoors populate the self.map_tiles_outdoors list
        get_dev_card populates the self.dev_card list
        get_items populates the self.item list
        :return:
        """
        self.get_map_tiles_indoors()
        self.get_map_tiles_outdoors()
        self.get_dev_cards()
        self.get_items()

    def populate_db(self):
        """
        Grabs the data from the Data folder and inserts it into the database. The database does not need to
        exist for this to occur
        :return:
        """
        self.add_maptiles_to_db()
        self.add_devcards_to_db()
        self.add_items_to_db()

    def add_maptiles_to_db(self):
        """
        Creates a new table for maptile objects within the database and insert the data from the csv file
        within /Data/
        :return:
        """
        maptile_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "maptiles")
        self.database.create_new_table("Maptiles", maptile_table)
        self.database.insert_tile_data()
        self.database.commit_db()

    def add_devcards_to_db(self):
        """
        Creates a new table for DevCard object within the database and insert the data from the csv file
        within /Data/
        :return:
        """
        dev_card_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "dev_cards")
        self.database.create_new_table("Devcards", dev_card_table)
        self.database.insert_dev_card_data()
        self.database.commit_db()

    def add_items_to_db(self):
        """
        Creates a new table for Items objects within the database and inserts the data from the csv file
        within /Data/
        :return:
        """
        item_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "items")
        self.database.create_new_table("Items", item_table)
        self.database.insert_item_data()
        self.database.commit_db()

    def get_map_tiles_indoors(self):
        """
        Queries the database for map tile data and then converts the tuples into objects using the
        convert_tuples_to_maptiles function to get a list of Maptile objects for the self.map_tiles_indoors list
        :return:
        """
        self.card_converter.set_maker_behavior(ConvertMaptiles())
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Indoor")
        self.map_tiles_indoor = self.card_converter.tuple_to_objects(map_tuples)

    def get_map_tiles_outdoors(self):
        """
        Queries the database for map tile data and then converts the tuples into objects using the
        convert_tuples_to_maptiles function to get a list of Maptile objects for the self.map_tiles_outdoors list
        :return:
        """
        self.card_converter.set_maker_behavior(ConvertMaptiles())
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Outdoor")
        self.map_tiles_outdoor = self.card_converter.tuple_to_objects(map_tuples)

    def get_dev_cards(self):
        """
        Queries the database for the dev card data and then converts the tuples into DevCard objects using
        the convert_tuples_to_devcard function to get a list of DevCard objects for the self.dev_cards list
        :return:
        """
        self.card_converter.set_maker_behavior(ConvertDevCards())
        dev_card_tuples = self.database.query_all_data_from_table("Devcards")
        self.dev_cards = self.card_converter.tuple_to_objects(dev_card_tuples)

    def get_items(self):
        """
        Queries the database for the item data then converts them into the Item objects using
        the convert_tuples_to_items functions to get a list of Item objects for the self. Items list
        :return:
        """
        self.card_converter.set_maker_behavior(ConvertItems())
        item_tuples = self.database.query_all_data_from_table("Items")
        self.items = self.card_converter.tuple_to_objects(item_tuples)

    def dev_card_pop(self):
        """
        Returns a devcard object from a random index in the list and then removes it from the list
        :return:
        """
        if len(self.dev_cards) > 0:
            max_dev_card_index = len(self.dev_cards) - 1
            random_index = randint(0, max_dev_card_index)
            return self.dev_cards.pop(random_index)
