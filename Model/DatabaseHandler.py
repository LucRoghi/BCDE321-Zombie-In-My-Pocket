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

from Model.Filehandler import Filehandler


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.mydb = sqlite3.connect(self.db_name)
        self.cursor = self.mydb.cursor()
        self.file_handler = Filehandler()

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
        table_creation_string = f'''CREATE TABLE IF NOT EXISTS {table_name} (id INT PRIMARY_KEY'''
        for key in columns:
            table_creation_string += f''', {key} {columns[key]}'''
        table_creation_string += f''')'''
        try:
            self.cursor.execute(table_creation_string)
            self.mydb.commit()
        except sqlite3.DatabaseError as e:
            print(e)
            return False
        return True

    def drop_table_in_db(self, table_name: str):
        self.cursor.execute(f'''DROP TABLE IF EXISTS {self.mydb}.{table_name}''')
        self.mydb.commit()

    def delete_all_rows_in_db(self, table_name: str):
        self.cursor.execute(f'''DELETE FROM {table_name}''')
        self.mydb.commit()

    def insert_item_data(self):
        pass

    def insert_tile_data(self):
        tile_data = self.file_handler.read_csv_data_into_list("/Data/", "maptiles_data")
        if self.cursor.execute('SELECT COUNT(*) from Maptiles') == 0:
            for tile in tile_data:
                self.cursor.execute('INSERT INTO Maptiles VALUES(?,?,?,?,?,?,?,?)', tile)
                self.mydb.commit()

    def insert_dev_card_data(self):
        item_data = self.file_handler.read_csv_data_into_list("/Data/", "items_data")
        if self.cursor.execute('SELECT COUNT(*) from Items') == 0:
            for tile in item_data:
                self.cursor.execute('INSERT INTO Devcards VALUES(?,?,?,?,?,?,?,?)', tile)
                self.mydb.commit()

    def get_dev_card_data(self):
        self.cursor.execute("SELECT * FROM DevCard")
        return self.cursor.fetchall()

    def get_tile_data(self):
        self.cursor.execute("SELECT * FROM Tiles ORDER BY ")
        return self.cursor.fetchall()

    def query_all_data_from_table(self, table_name: str) -> tuple:
        self.cursor.execute(f"SELECT * FROM {table_name}")
        self.mydb.commit()
        return self.cursor.fetchall()

    def query_data_from_table(self, table_name: str, column: str, query: str):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column}='{query}'")
        return self.cursor.fetchall()


if __name__ == "__main__":
    pass
