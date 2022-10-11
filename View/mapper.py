"""
ATTEMPTED TO IMPLEMENT BUT COULD NOT GET IMAGES TO STITCH UP CORRECTLY
"""

from pathlib import Path


class Mapper:
    def __init__(self):
        self.map = None
        self.image_directory = str(Path(__file__).parent.parent) + "/Data/TileImages/"

    def add_row(self):
        pass

    def add_column(self):
        pass

    def shift_row_down(self):
        pass

    def shift_columns_right(self):
        pass

    def insert_image(self):
        pass

    def merge_map(self):
        pass

    def print_map(self):
        pass
