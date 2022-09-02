import matplotlib.pyplot as plt
from Model.Player import Player


class Graphing:
    def __init__(self):
        self.player = Player()

    def player_health_graph(self):
        x = 1  # [self.player.turn]
        y = 1  # [self.player.health]
        plt.plot(y, x)
        plt.xlabel("Turns")
        plt.ylabel(f"{self.player.name} Health")
        plt.title(f'{self.player.name} Health over Turns')
        plt.show()
