from abc import ABC, abstractmethod
from Model.CardConverter.AbstractConvert import *
from Model.CardMaker.ItemFactory import ItemFactory
from Model.item import Item


class ConvertItems(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        item_list = []
        item_factory = ItemFactory()
        for item in tuple_list:
            item_list.append(item_factory.create_card(item))
        return item_list
