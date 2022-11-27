from abc import ABC, abstractmethod


class CardFactory(ABC):
    def str_to_bool(self, string: str) -> bool:
        return string.lower() in "true"

    @abstractmethod
    def create_card(self, data_tuple):
        pass
