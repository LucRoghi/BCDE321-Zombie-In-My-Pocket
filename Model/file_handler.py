"""
Author: Luc Roghi lcr0059
Filehandler is a class designed to be able to read and write
files of multiple types and return them into usable format

NOTE: FOR ALL FUNCTIONS FILE EXTENSIONS ARE NOT TO BE USED WITHIN THE FILENAME

FILE HANDLING) JSON ::
    >>> temp_filehandler = Filehandler()
    >>> temp_filehandler.write_file_into_json("/Data/Test_Data/", "json_write", {"test1": 1, "test2": 2})
    >>> print(temp_filehandler.read_file_from_json("/Data/Test_Data/", "json_write"))
    {'test1': 1, 'test2': 2}

FILE HANDLING CSV::
    >>> print(temp_filehandler.read_csv_data_into_list("/Data/Test_Data/", "test_csv"))
    [['this', 'is', 'a', 'test', 'csv'], ['it', 'reads', 'comma', 'separated', 'values'], ['from', 'a', 'designated',
    'file', 'location']]

FILE HANDLING PICKLE::
    >>> from Model.item import Item
    >>> temp_item = Item("test_item",None,None,None,None,None)
    >>> temp_filehandler.save_object_to_pickle("/Saves", temp_item)
    >>> loaded_object = temp_filehandler.load_object_from_pickle("/Saves", f'{datetime.now().strftime("%d%m%Y")}')
    >>> print(loaded_object.name)
    test_item
"""

import csv
import datetime
import json
import os.path
import pickle
from pathlib import Path
from datetime import datetime


class Filehandler:
    """
    File Handle Class:
        Attributes:
            root_dir: Grabs the root directory of the project to ensure that all paths are relative and not absolute
        Methods:
            write_file_into_json:
                :
    """

    def __init__(self):
        self.root_dir = Path(__file__).parent.parent

    def read_file_from_json(self, path: str, filename: str) -> dict:
        """
        Returns a dictionary from a json file specified in the above parameters
        :param path: str
        :param filename: str
        :return: :dict
        """
        file = open(str(self.root_dir) + str(path) + filename + ".json")
        return json.load(file)

    def write_file_into_json(self, path: str, filename: str, contents: dict):
        """
        Writes the contents of a dictionary to a json file specified at the path
        :param path: str
        :param filename: str
        :param contents: dict
        :return:
        """
        json_file = json.dumps(contents, indent=4)
        with open(str(self.root_dir) + str(path) + filename + ".json", "w") as writer:
            writer.write(json_file)

    def read_csv_data_into_list(self, path: str, filename: str) -> list:
        """
        Returns the data from a csv file as a list
        :param path:
        :param filename:
        :return: :list
        """
        with open(str(self.root_dir) + path + filename + ".csv", newline='') as data_file:
            csv_data = list(csv.reader(data_file))
        return csv_data

    def print_csv_data(self, path: str, filename: str):
        """
        Prints all the contents of a csv file as a string
        :param path:
        :param filename:
        :return:
        """
        with open(str(self.root_dir) + path + filename + ".csv", newline='') as data_file:
            csv_data = csv.reader(data_file)
            for line in csv_data:
                print("".join(line))

    def check_if_save_exists(self, save_name):
        """
        Returns a boolean based on whether a file in a directory exists
        :param save_name:
        :return: bool
        """
        return os.path.exists(str(self.root_dir) + '/Saves/' + save_name + '.pickle')

    def save_object_to_pickle(self, save_name: str, object_):
        """
        Uses the pickle library to save an object to a directory specified
        :param object_:
        :param save_name:
        :return:
        """
        if self.check_if_save_exists(save_name + '.pickle'):
            save_name += '_1'
        with open(str(self.root_dir) + "/Saves/" + save_name + '.pickle', 'wb') as file:
            pickled_object = pickle.dumps(object_)
            file.write(pickled_object)

    def load_object_from_pickle(self, save_name: str):
        """
        Loads an object from a pickle file designated above
        :param save_name:
        :return: :Generic
        """
        file_name = str(self.root_dir) + "/Saves/" + save_name + '.pickle'
        file = open(file_name, 'rb')
        loaded_object = pickle.load(file)
        file.close()
        return loaded_object


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
