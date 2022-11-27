from abc import ABC, abstractmethod

class AbstractConvert(ABC):
    def str_to_bool(self, string: str) -> bool:
        return string.lower() in "true"

    @abstractmethod
    def tuple_to_objects(self, tuple_list: [tuple]):
        pass