import csv
import json

from pathlib import Path


class Filehandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.shelve = None

    def read_file_from_json(self, path: str, filename: str) -> dict:
        file = open(str(self.root_dir) + str(path) + filename + ".json")
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

    def read_csv_data_into_list(self, path: str, filename: str):
        with open(str(self.root_dir) + path + filename + ".csv", newline='') as data_file:
            tile_data = list(csv.reader(data_file))
        return tile_data


if __name__ == "__main__":
    pass
