from abc import ABC, abstractmethod
from Model.CardConverter.AbstractConvert import *
from Model.CardMaker.DevCardFactory import DevCardFactory
from Model.dev_cards import Devcard


class ConvertDevCards(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        devcard_list = []
        devcard_factory = DevCardFactory()
        for card in tuple_list:
            devcard_list.append(devcard_factory.create_card(card))
        return devcard_list
