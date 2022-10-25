import pandas


class Load:
    @staticmethod
    def dev_cards():
        path = f"{Path(__file__).parent}\DevCards.xlsx"
        f = open(path)
        data = pandas.read_excel(f)
        return data

    @staticmethod
    def tiles():
        path = f"{Path(__file__).parent}\Tiles.xlsx"
        f = open(path)
        data = pandas.read_excel(f)
        return data


# Debugging Test Case - Ignore
if __name__ == '__main__':
    print(Load.tiles())
