import pandas


class Load:
    @staticmethod
    def dev_cards():
        return pandas.read_excel(r'./Model/DevCards.xlsx')

    @staticmethod
    def tiles():
        return pandas.read_excel(r'./Model/Tiles.xlsx')


# Debugging Test Case - Ignore
if __name__ == '__main__':
    print(Load.dev_cards())
