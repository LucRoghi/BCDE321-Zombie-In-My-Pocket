import json
import shelve

from DatabaseHandler import Database
from pathlib import Path


class Filehandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.shelve = None

    def read_file_from_json(self, path: str, filename: str) -> dict:
        file = open(str(self.root_dir) + str(path) + filename)
        return json.load(file)

    def write_file_into_json(self, path: str, filename: str, contents: dict):
        json_file = json.dumps(contents, indent=4)
        with open(str(self.root_dir) + str(path) + filename + ".json", "w") as writer:
            writer.write(json_file)

    def open_shelve(self, name: str):
        return self.shelve.open(name)

    def add_new_object_to_shelve(self, db_name: str, object_name, object):
        with self.shelve.open(db_name, "w") as shelf:
            shelf[object_name] = object

    def read_text_file_into_list(self, path: str, filename: str):
        data_file = open(str(self.root_dir) + path + filename + ".txt", "r")
        data = data_file.readlines()
        data_list = []
        for line in data:
            data_list.append(line)
        for line in data_list:

            print(line)
        print(data_list)
        return data



if __name__ == "__main__":
    test_filehandler = Filehandler()
    test_db = Database("test_db.db")
    root = test_filehandler.root_dir
    columns_maptile = test_filehandler.read_file_from_json("/Data/Database_Schema/Tables/", "maptiles.json")
    test_db.create_new_table("maptiles", columns_maptile)
    print(test_db.mydb.execute('''SELECT * from maptiles''').description)
    test_filehandler.write_file_into_json("/Data/Database_Schema/Tables/", "test", columns_maptile)
    test_filehandler.read_text_file_into_list("/Data/", "maptiles_data")
