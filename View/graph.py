"""
Author: Jared Ireland jai0095

This class here, over time, takes in the data of all the players moves making it into a 'turn' and also taking the
players health at every turn. When the player loses or wins the graph will then be displayed as an "End of Game" result
"""
import matplotlib.pyplot as plt
import view


class Graph:
    def __init__(self):
        self.player = view.Player()
        self.turn_list = []
        self.health_list = []

    def player_health_graph(self):
        """
        Generates a Graph based on the Users Health and Turns as a means to display Health over Time
        """
        self.turn_list.append(self.player.get_move_count())
        self.health_list.append(self.player.get_health())
        plt.plot(self.health_list, self.turn_list)
        plt.xlabel("Turns")
        plt.ylabel("Health")
        plt.title('Health over Turns')
        plt.show()


# health=6, turn=9
# name, current_location, attack, health, inventory=None, has_totem=None, turn=9
if __name__ == "__main__":
    print(Graph.player_health_graph)
