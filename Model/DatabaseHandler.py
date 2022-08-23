"""
Author: Luc Roghi - lcr0059
Author: Jared Ireland - jai0095
https://docs.python.org/3/library/sqlite3.html

This module serves as a database handler. It can be used to create, interact and pull data from a database
Attributes:
    self.db_name: (str) The database name you wish to create
    self.mydb: (sqlite3 connection) A connection to the named database set above (If unable to be found or created
    will raise a database error)
    self.cursor: (sqlite3 cursor) A cursor to aid in the writing or reading of data within the database

Methods:
     open_db(self, db_name):
     @Params: db_name: str
     @returns: None

     close_db(self, db_name)
"""
import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.mydb = sqlite3.connect(self.db_name)
        self.cursor = self.mydb.cursor()

    def open_db(self):
        try:
            self.mydb = sqlite3.connect(self.db_name)
            return True
        except sqlite3.DatabaseError as e:
            print(e)
            return False


    def close_db(self):
        try:
            self.mydb.close()
        except sqlite3.DatabaseError as e:
            print(e)
            return False
        return True

    def create_new_table(self, table_name: str, columns: dict):
        table_creation_string = f'''CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY_KEY'''
        for key in columns:
            table_creation_string += f''', {key} {columns[key]}'''
        table_creation_string += f''')'''
        try:
            self.cursor.execute(table_creation_string)
        except sqlite3.DatabaseError as e:
            print(e)
            return False
        return True

    def insert_item_data(self):
        dc_data = [
            # Item, E1, E1C, E2, E2C, E3, E2C, Crg, Has the Card beem Played: False = No. True = Yes -> Pushed to Play Array
            # to be shuffled later -- E means Event - 1 = 9pm, 2 = 10pm, 3 = 11pm
            ("Oil", "Nothing", "None", "Item", "None", "Zombies", "6", "1", False),
            ("Gasoline", "Zombies", "4", "Health", "-1", "Item", "None", "1", False),
            ("Board With Nails", "Item", "None", "Zombies", "4", "Health", "-1", "Unlimited", False),
            ("Machete", "Zombies", "4", "Health", "-1", "Zombies", "6", "Unlimited", False),
            ("Grisly Femur", "Item", "None", "Zombies", "5", "Health", "-1", "Unlimited", False),
            ("Golf Club", "Health", "-1", "Zombies", "4", "Nothing", "None", "Unlimited", False),
            ("Chainsaw", "Zombies", "3", "Nothing", "None", "Zombies", "5", "2", False),
            ("Can of Soda", "Health", "1", "Item", "", "Zombies", "4", "1", False),
            ("Candle", "Nothing", "None", "Health", "1", "Zombies", "4", "Unlimited", False)
        ]
        self.cursor.executemany('INSERT INTO DevCard(item,event_one,e1_consequence,event_two,e2_consequence,event_three'
                                ',e3_consequence,charges,played) VALUES(?,?,?,?,?,?,?,?,?)', dc_data)

    def insert_tile_data(self):
        tile_data = [
            # Tile Name, Action, Type, Door N, Door E, Door S, Door W, Been Played
            ("Graveyard", "Bury Totem", "Outdoor", True, True, False, False, False),
            ("Yard", "None", "Outdoor", True, True, True, False, False),
            ("Sitting Area", "None", "Outdoor", True, True, True, False, False),
            ("Yard", "None", "Outdoor", True, True, True, False, False),
            ("Yard", "None", "Outdoor", True, True, True, False, False),
            ("Patio", "None", "Outdoor", True, True, False, True, False),
            ("Garage", "None", "Outdoor", False, True, True, False, False),
            ("Garden", "Health", "Outdoor", True, True, True, False, False),
            ("Bathroom", "None", "Indoor", False, False, False, True, False),
            ("Family Room", "None", "Indoor", True, False, True, True, False),
            ("Kitchen", "Health", "Indoor", True, False, True, True, False),
            ("Dining Room", "None", "Indoor", True, True, True, True, False),
            ("Storage", "Draw", "Indoor", False, False, False, True, False),
            ("Bedroom", "None", "Indoor", False, False, True, True, False),
            ("Evil Temple", "Find Totem", "Indoor", True, False, True, False, False),
            ("Foyer", "None", "Indoor", True, False, False, False, False)
        ]
        self.cursor.executemany('INSERT INTO Tiles VALUES(?,?,?,?,?,?,?,?)', tile_data)

    def get_dev_card_data(self):
        self.cursor.execute("SELECT * FROM DevCard")
        return self.cursor.fetchall()

    def get_tile_data(self):
        self.cursor.execute("SELECT * FROM Tiles ORDER BY ")
        return self.cursor.fetchall()

if __name__ == "__main__":
    new_db = Database("test.db")
    test_dict = {"hp": "INT", "atk": "INT", "item1": "TEXT", "item2": "TEXT", "currentLocation": "TEXT", "previousLocation": "TEXT"}
    new_db.create_new_table("test_table", test_dict)

