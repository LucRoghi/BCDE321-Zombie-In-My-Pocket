from abc import ABC, abstractmethod
from Model.CardMaker.AbstractConvert import *
from Model.item import Item


class ConvertMaptiles(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        item_list = []
        for item in tuple_list:
            _, name, effect, can_combine, combines_with_1, combines_with_2, makes_1, makes_2, uses = item
            new_item = Item(name, effect, can_combine, [combines_with_1, combines_with_2], [makes_1, makes_2], uses)
            new_item.effect = getattr(new_item, effect, None)
            item_list.append(new_item)
        return item_list