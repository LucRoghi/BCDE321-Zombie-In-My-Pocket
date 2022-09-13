"""
Author: Jared Ireland jai0095
"""

import matplotlib.pyplot as plt
from Model.player import Player
from View.view_commands import Commands


class Graph:
    def __init__(self, turn, turn_list, health_list):
        self.player = Player()
        self.turn = 0
        self.turn_list = []
        self.health_list = []

    # Make Turn here
    def turn_count(self):
        if Commands.do_move_cmd == "N" or "E" or "S" or "W":
            self.turn += 1

    def player_health_graph(self):
        x = self.turn_list.append(self.turn)
        y = self.health_list.append(self.player.health)
        plt.plot(y, x)
        plt.xlabel("Turns")
        plt.ylabel("Health")
        plt.title('Health over Turns')
        plt.show()


# health=6, turn=9
# name, current_location, attack, health, inventory=None, has_totem=None, turn=9
if __name__ == "__main__":
    print(Graph.player_health_graph())
