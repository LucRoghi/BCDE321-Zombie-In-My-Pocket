import unittest

from Model.database_handler import Database
from Model.file_handler import Filehandler


class DatabaseHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.database = Database("test.db")
        self.file_handler = Filehandler()

    def test_open_new_db(self):
        self.assertEqual(self.database.db_name, "test.db")

    def test_close_db(self):
        self.assertEqual(self.database.close_db(), True)

    def test_create_new_table(self):
        result = self.database.create_new_table("test_table", {"Full Name": "TEXT", "Age": "INTEGER"})
        self.assertEqual(result, True)

    def test_create_new_table_no_columns(self):
        result = self.database.create_new_table("test_table_2", {})
        self.assertEqual(result, False)

    def test_delete_all_rows_in_table(self):
        result = self.database.delete_all_rows_in_table("test_table")
        self.assertEqual(result, True)

    def test_delete_all_rows_in_table_invalid_name(self):
        result = self.database.delete_all_rows_in_table("not_the_test_table")
        self.assertEqual(result, False)

    def test_drop_table_from_db(self):
        result = self.database.drop_table_in_db("test_table")
        self.assertEqual(result, True)

    def test_drop_table_from_db_not_in_db(self):
        result = self.database.drop_table_in_db("not_the_test_table")
        self.assertEqual(result, True)

    def test_insert_maptile_data(self):
        maptile_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "maptiles")
        self.database.create_new_table("Maptiles", maptile_table)
        result = self.database.insert_tile_data()
        self.database.commit_db()
        self.assertEqual(result, True)

    def test_insert_maptile_data_exception(self):
        maptile_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "not_maptiles")
        self.database.create_new_table("Maptiles", maptile_table)
        result = self.database.insert_tile_data()
        self.database.commit_db()
        self.assertEqual(result, False)

    def test_insert_dev_card(self):
        dev_card_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "dev_cards")
        self.database.create_new_table("Devcards", dev_card_table)
        result = self.database.insert_dev_card_data()
        self.database.commit_db()
        self.assertEqual(result, True)

    def test_insert_item_data(self):
        item_table = self.file_handler.read_file_from_json("/Data/Database_Schema/Tables/", "items")
        self.database.create_new_table("Items", item_table)
        result = self.database.insert_item_data()
        self.database.commit_db()
        self.assertEqual(result, False)
