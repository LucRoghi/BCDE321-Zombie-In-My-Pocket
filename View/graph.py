"""
Author: Jared Ireland jai0095

This class here, over time, takes in the data of all the players moves making it into a 'turn' and also taking the
players health at every turn. When the player loses or wins the graph will then be displayed as an "End of Game" result
"""
import matplotlib.pyplot as plt
import View


class Graph:
    def __init__(self):
        self.player = View.Player()
        self.turn = 0
        self.turn_list = []
        self.health_list = []

    def turn_count(self):
        """
        Generates a Counter for how many Turns have passed based on amount of Move's the player has done
        Used in Graphing the Players Health over Time
        :return:
        """
        if View.Commands.do_move_up or View.Commands.do_move_down or View.Commands.do_move_left or \
                View.Commands.do_move_right:
            self.turn += 1

    def player_health_graph(self):
        """
        Generates a Graph based on the Users Health and Turns as a means to display Health over Time
        :return:
        """
        # x = self.turn_list.append(self.turn)
        # y = self.health_list.append(self.player.get_health())
        # plt.plot(y, x)
        self.turn_list.append(self.turn)
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
