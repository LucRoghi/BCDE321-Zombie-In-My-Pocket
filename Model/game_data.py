"""
Author: Luc Roghi lcr0059

Game Data is a class designed to hold all the instantiated object being used within the game. The items are converted
from string format to object format within the 3 static methods at the top of the file.

GAME DATA MAPTILES:
        >>> test_game_data = GameData()
        >>> print(len(test_game_data.map_tiles_indoor))
        8
        >>> print(test_game_data.map_tiles_indoor) #doctest: +ELLIPSIS
        [<Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>, <Model.map_tile.MapTile object at ...>]
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
        [<Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>, <Model.dev_cards.Devcard object at ...>]
        >>> print(test_game_data.dev_cards[0]) #doctest: +ELLIPSIS
        <Model.dev_cards.Devcard object at ...>
"""

from random import random
from Model.dev_cards import Devcard
from Model.database_handler import Database
from Model.file_handler import Filehandler
from Model.item import Item
from Model.map_tile import MapTile


def convert_tuples_to_maptile(tuple_list: tuple) -> list[MapTile]:
    """
    When given a tuple it will attempt to convert it into a Maptile object and then append it to a list.
    It will then return the list of MapTile objects
    :param tuple_list:
    :return:
    """
    tile_list = []
    for tile in tuple_list:
        _, room_name, effect, door_up, door_right, door_down, door_left, type = tile
        tile = MapTile(room_name, effect, door_up, door_right, door_down, door_left)
        tile.effect = getattr(tile, effect, None)
        tile_list.append(tile)
    return tile_list


def convert_tuples_to_dev_card(tuple_list: tuple) -> list[Devcard]:
    """
    When given a tuple it will attempt to convert it into a DevCard object and then append to a list. During the
    conversion, if the effect is an integer it will convert it to a call to a function within the MapTile Class to
    add_zombies_to_room. If the effect is non-numeric, the other functions will be attached to the effect
    :param tuple_list:
    :return:
    """
    devcard_list = []
    for card in tuple_list:
        _, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect, item = card
        dev_card = Devcard(0, nine_message, nine_effect, ten_message, ten_effect,
                           eleven_message, eleven_effect, item)

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
    """
    When given a tuple will attempt to convert it to an Item object. The effect will get an attribute from within the
    item class to be stored as a callable. It will then be appended to a list and then the list is returned
    :param tuple_list:
    :return:
    """
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
        self.initialize_game_data()

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
        Creates a new table for DevCard pbject within the database and insert the data from the csv file
        within /Data/
        :return:
        """
        dev_card_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "dev_cards")
        self.database.create_new_table("Devcards", dev_card_table)
        self.database.insert_dev_card_data()
        self.database.commit_db()

    def add_items_to_db(self):
        """
        Creates a new table for Items objefts within the database and inserts the data from the csv file
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
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Indoor")
        self.map_tiles_indoor = convert_tuples_to_maptile(map_tuples)

    def get_map_tiles_outdoors(self):
        """
        Queries the database for map tile data and then converts the tuples into objects using the
        convert_tuples_to_maptiles function to get a list of Maptile objects for the self.map_tiles_outdoors list
        :return:
        """
        map_tuples = self.database.query_data_from_table("Maptiles", "type", "Outdoor")
        self.map_tiles_outdoor = convert_tuples_to_maptile(map_tuples)

    def get_dev_cards(self):
        """
        Queries the database for the dev card data and then converts the tuples into DevCard objects using
        the convert_tuples_to_devcard function to get a list of DevCard objects for the self.dev_cards list
        :return:
        """
        dev_card_tuples = self.database.query_all_data_from_table("Devcards")
        self.dev_cards = convert_tuples_to_dev_card(dev_card_tuples)

    def get_items(self):
        """
        Queries the database for the item data then converts them into the Item objects using
        the convert_tuples_to_items functions to get a list of Item objects for the self.items list
        :return:
        """
        item_tuples = self.database.query_all_data_from_table("Items")
        self.items = convert_tuples_to_items(item_tuples)

    def dev_card_pop(self):
        """
        Returns a devcard object from a random index in the list and then removes it from the list
        :return:
        """
        max_dev_card_index = len(self.dev_cards) - 1
        random_index = random.randint(0, max_dev_card_index)
        return self.dev_cards.pop(random_index)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)