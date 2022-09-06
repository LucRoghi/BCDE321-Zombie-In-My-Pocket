"""
Author: Jared Ireland jai0095
For: BCDE311 Assignment2
"""

# Dictionary: Items
# Dictionary: UsedItems
# Dictionary: CombinableItems(Items)
# Array: PlayerInventory
# Dictionary: PlayerCombineItems
# Before Attack:
#     Prompt: Do you wish to combine {PlayerCombineItems}?
#         Case: [0]
#         Case: [1]
#         Case: [2]

# FIXME This whole file LMAO

from Database import Database
from old_player import Player


class Item:
    def __init__(self):
        game_storage = Database()
        game_storage.setup_db()
        self.items = game_storage.get_item_data()
        print(self.items)
        self.combine_items = game_storage.get_combine_items()
        print(self.combine_items)
        self.used_items = []
        self.inventory = []

    def player_combine_items(self):
        self.inventory = ["Can of Soda"]
        if self.inventory in self.items and self.combine_items:
            print("Memes")

    def max_item(self):
        if len(self.inventory) == 2:
            print("You can no longer pick any items up!")

    # TODO add the functionality of the Chainsaw Charges/Uses - Default 2, Gasoline adds
    #   I wish to point out that "Uses" "Combine" "Command" and "Words" are place holders

    # TODO I forgot we actually have the chargers in the Database....
    def charges(self):
        uses = 0
        combine = "Yes"
        command = "Use Chainsaw"  # Temp
        words = "Use Chainsaw"
        if self.items("Chainsaw") in self.inventory:
            uses = 2
        if words == command:
            uses -= 1
        if uses == 0:
            print("Can not use this item - Fill it up with Gasoline")
        if self.items("Gasoline") in self.inventory and combine == "Yes":
            uses += 2
        pass


if __name__ == '__main__':
    Item().player_combine_items()