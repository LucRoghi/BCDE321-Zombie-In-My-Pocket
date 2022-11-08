from abc import ABC, abstractmethod

import strategy


class Move:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strat):
        self.__strategy = strat

    def process(self):
        return self.__strategy.process()


class Strategy(ABC):
    @staticmethod
    @abstractmethod
    def process():
        NotImplemented


class UpStrategy(Strategy):
    def __init__(self):
        self.game = strategy.Game

    def process(self):
        self.game.move_dic("up")
        self.game.get_game()


class RightStrategy(Strategy):
    def __init__(self):
        self.game = strategy.Game

    def process(self):
        self.game.move_dic("right")
        self.game.get_game()


class DownStrategy(Strategy):
    def __init__(self):
        self.game = strategy.Game

    def process(self):
        self.game.move_dic("down")
        self.game.get_game()


class LeftStrategy(Strategy):
    def __init__(self):
        self.game = strategy.Game

    def process(self):
        self.game.move_dic("left")
        self.game.get_game()


if __name__ == "__main__":
    move_strat = Move()

    strat_direction = "up"
    move_strat.set_strategy(UpStrategy)
    print(move_strat.process())

    strat_direction = "right"
    move_strat.set_strategy(RightStrategy)
    print(move_strat.process())

    strat_direction = "down"
    move_strat.set_strategy(DownStrategy)
    print(move_strat.process())

    strat_direction = "left"
    move_strat.set_strategy(LeftStrategy)
    print(move_strat.process())
