from abc import ABC, abstractmethod


class CardMaker(object):
    def __int__(self, maker_behavior):
        self.__behavior = maker_behavior

    def set_maker_behavior(self, maker_behavior):
        self.__behavior = maker_behavior

    def tuple_to_objects(self, tuple_list):
        return self.__behavior.tuple_to_objects(tuple_list)
