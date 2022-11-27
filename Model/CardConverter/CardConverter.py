from abc import ABC, abstractmethod


class CardConverter():
    def __int__(self):
        self.__behavior = None

    def set_maker_behavior(self, converter_behavior):
        self.__behavior = converter_behavior

    def tuple_to_objects(self, tuple_list):
        return self.__behavior.tuple_to_objects(tuple_list)
