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

USING DATABASE HANDLER::
    >>> test_database = Database("test.db")
    >>> print(test_database.db_name)
    test.db
    >>> print(test_database.mydb) #doctest: +ELLIPSIS
    <sqlite3.Connection object at ...>
    >>> print(test_database.open_db())
    True
    >>> test_database.db_name = "not_test.db"
    >>> print(test_database.open_db())
    True
    >>> print(test_database.close_db())
    True
    >>> test_database.create_new_table("test_table", {"Full Name": "TEXT", "Age": "INTEGER"})
    Create table test_table
    True
    >>> test_database.drop_table_in_db("test_table")
    True
    >>> test_database.delete_all_rows_in_table("test_table")
    True

"""
import doctest
import sqlite3
from typing import List, Any

from Model.file_handler import Filehandler


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.mydb = sqlite3.connect(self.db_name)
        self.cursor = self.mydb.cursor()
        self.file_handler = Filehandler()

    def open_db(self):
        """
        Creates a new database connection
        :return: Bool
        """
        try:
            self.mydb = sqlite3.connect(self.db_name)
            return True
        except sqlite3.DatabaseError as e:
            print(e)
            return False

    def close_db(self):
        """
        Closes the current database connection
        :return: Bool
        """
        try:
            self.mydb.close()
            return True
        except sqlite3.DatabaseError as e:
            print(e)
            return False

    def create_new_table(self, table_name: str, columns: dict):
        """
        Create a new table within the current connection with a name and columns. The columns are a dictionary
        to define the column name and type
        :param table_name:
        :param columns:
        :return:
        """
        table_creation_string = f'''CREATE TABLE IF NOT EXISTS {table_name} (id INT PRIMARY_KEY'''
        for key in columns:
            table_creation_string += f''', {key} {columns[key]}'''
        table_creation_string += f''')'''
        try:
            self.cursor.execute(table_creation_string)
            print(f"Create table {table_name}")
        except sqlite3.DatabaseError as e:
            print(e)
            return False
        return True

    def drop_table_in_db(self, table_name: str):
        """
        Removes a table from the current schema
        :param table_name:
        :return:
        """
        self.cursor.execute(f'''DROP TABLE IF EXISTS {table_name}''')
        return True

    def delete_all_rows_in_table(self, table_name: str):
        self.cursor.execute(f'''DELETE FROM {table_name}''')
        return True

    def commit_db(self):
        self.mydb.commit()

    def insert_tile_data(self):
        tile_data = self.file_handler.read_csv_data_into_list("/Data/", "maptiles_data")
        for tile in tile_data:
            self.cursor.execute('INSERT INTO Maptiles VALUES(?,?,?,?,?,?,?,?)', tile)

    def insert_dev_card_data(self):
        dev_card_data = self.file_handler.read_csv_data_into_list("/Data/", "dev_cards_data")
        for dev_card in dev_card_data:
            self.cursor.execute('INSERT INTO Devcards VALUES(?,?,?,?,?,?,?,?)', dev_card)

    def insert_item_data(self):
        item_data = self.file_handler.read_csv_data_into_list("/Data/", "items_data")
        for item in item_data:
            self.cursor.execute('INSERT INTO Items VALUES(?,?,?,?,?,?,?,?,?)', item)

    def get_dev_card_data(self):
        self.cursor.execute("SELECT * FROM Devcards")
        return self.cursor.fetchall()

    def get_tile_data(self):
        self.cursor.execute("SELECT * FROM Tiles")
        return self.cursor.fetchall()

    def query_all_data_from_table(self, table_name: str):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        self.mydb.commit()
        return self.cursor.fetchall()

    def query_data_from_table(self, table_name: str, column: str, query: str):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column}='{query}'")
        self.mydb.commit()
        return self.cursor.fetchall()


if __name__ == "__main__":
    doctest.testmod()
