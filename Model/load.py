import pandas


class Load:
    @staticmethod
    def dev_cards():
        return pandas.read_excel(r'./Model/DevCards.xlsx')

    @staticmethod
    def tiles():
        return pandas.read_excel(r'./Model/Tiles.xlsx')

    @staticmethod
    def load_file():
        return "elp"

    # def dev_cards():
    #     filepath = input("Please input a filepath for where the Dev Cards are is: ")
    #     filename = input("Please input the name of the xlsx for the tiles: ")
    #
    #     try:
    #         return pandas.read_excel(f'{filepath}/{filename}.xlsx', "r")
    #     except:
    #         print("ERROR! You have not entered a valid filepath or filename. "
    #               "\n Keep in mind that the Dev Cards document does need to be of an .xlsx format - this is an Excel "
    #               "Sheet")
    #
    # @staticmethod
    # def tiles():
    #     filepath = input("Please input a filepath for where the tiles are is: ")
    #     filename = input("Please input the name of the xlsx for the tiles: ")
    #
    # try: return pandas.read_excel(f'{filepath}/{filename}.xlsx', "r") except: print("ERROR! You have not entered a
    # valid filepath or filename. " "\n Keep in mind that the Tiles document does need to be of an .xlsx format -
    # this is an Excel Sheet")


# Debugging Test Case - Ignore
if __name__ == '__main__':
    print(Load.dev_cards())
