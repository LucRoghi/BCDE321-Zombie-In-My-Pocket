import pandas


class Load:
    @staticmethod
    def dev_cards():
        return pandas.read_excel(r'DevCards.xlsx')

    @staticmethod
    def tiles():
        return pandas.read_excel(r'Tiles.xlsx')

    @staticmethod
    def load_file():
        return "elp"


# Debugging Test Case - Ignore
if __name__ == '__main__':
    print(Load.tiles())
