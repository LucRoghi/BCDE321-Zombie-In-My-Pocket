from abc import ABC, abstractmethod
from Model.CardMaker.AbstractConvert import *
from Model.dev_cards import Devcard


class ConvertMaptiles(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        devcard_list = []
        for card in tuple_list:
            _, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect, item = card
            dev_card = Devcard(nine_message, nine_effect, ten_message, ten_effect,
                               eleven_message, eleven_effect, item)
            devcard_list.append(dev_card)
        return devcard_list
