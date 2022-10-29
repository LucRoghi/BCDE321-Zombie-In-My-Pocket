"""
Author: Jared Ireland jai0095

The lis of commands the player can use to play the game
"""
import cmd

import controller
import view
import sys


class Commands(cmd.Cmd):
    intro = 'Welcome, type help or ? to list the commands or start to start the game'

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.player = view.Player()
        self.game = view.Game(self.player)
        self.graph = view.Graph()
        self.file_handle = controller.FileHandler()
        if len(sys.argv) > 1:
            try:
                self.do_load(sys.argv[1])
            except Exception:
                print("File not found")

    def get_game(self):
        return self.game

    def do_start(self, line):
        """
            Starts a new game
            Syntax: Start
        """
        self.game.game_start()

    def do_restart(self, line):
        """
            Deletes your progress and ends the game
            Syntax: restart
        """
        del self.game
        del self.player
        self.player = view.Player()
        self.game = view.Game(self.player)

    def prompt(self, line):
        """
            Change the interactive prompt
            Syntax: prompt <input>
        """
        if self.prompt == "> ":
            self.prompt = line + ' '
        else:
            self.prompt = "> "

    def do_place(self, line):
        """
            Places the current map tile
            Syntax: place
        """
        self.game.place(line)

    def do_choose(self, direction):
        """
            When there is no valid move directions choose a wall to break - Zombies will enter
            Syntax: choose <direction>
        """
        self.game.choose(direction)

    def do_move(self, direction):
        """
            Movement of the player
            Syntax: move <direction>
        """
        self.game.move(direction)

    def do_attack(self, line):
        """
            Attacks zombies in the room with current attack score
            Syntax: attack
        """
        self.game.attack(line)

    def do_run(self, line):
        """
            Run's away from the zombies - can only run into a previous room - lose 1 HP
            Syntax: run <direction>
        """
        self.game.run(line)

    def do_cower(self, line):
        """
            Cower in the corner - Gain 3 HP - Lose 1 DevCard
            Syntax: cower
        """
        self.game.cower(line)

    def do_use(self, line):
        """
            Player uses an item
            Syntax: use
        """
        self.game.use(line)

    def do_drop(self, line):
        """
            Drops an item from your hand
            Syntax: drop
        """
        self.game.drop(line)

    def do_swap(self, line):
        """
            Swaps an item in you hand with the one in the room
            Syntax: swap
        """
        self.game.swap(line)

    def do_draw(self, line):
        """
            Draws a new development card (Must be done after evey move)
            Syntax: draw
        """
        self.game.draw(line)

    def do_search(self, line):
        """
            Searches for the zombie totem. (Player must be in the evil temple and will have to resolve a dev card)
            Syntax: search
        """
        self.game.search(line)

    def do_bury(self, line):
        """
            Buries the totem. (Player must be in the graveyard and will have to resolve a dev card)
            Syntax: bury
        """
        self.game.bury(line)

    def do_rotate(self, line):
        """
            Rotates the current map piece 1 rotation clockwise
            Syntax: rotate
        """
        self.game.rotate_tile(line)

    def do_give(self, line):
        self.game.give(line)

    def do_give2(self, line):
        self.game.give2(line)

    def do_load(self, line):
        """
            Loads a file from the save folder
            Syntax: load <filename>
        """
        self.file_handle.load(line)

    def do_save(self, line):
        """
            Takes a name and saves it to the save folder
            Syntax: save <filename>
        """
        self.file_handle.save(line)

    def do_exit(self, line):
        """
            Exits the game without saving
            Syntax: Exit
        """
        return True

    def do_status(self, line):
        """
            Shows the status of the player
            Syntax: status
        """
        if self.game.state != "Game Over":
            self.game.get_player_status()

    def do_graph(self, line):
        """
            Shows a graph of the players health over turns
            Syntax: graph
        """
        self.graph.player_health_graph()

    def do_commands(self, line):
        """
            Prints out a list of all the CMD's from a JSON file
            Syntax: commands
        """
        return self.game.help_all()

    def egs(self):
        """IDK if this works :)"""
        return view.FinishScreen.start()

    def do_difficulty(self, line):
        """
            Selects the games difficulty
            Required State: Choosing Difficulty
            Syntax: difficulty <difficulty>
        """
        return self.game.difficulty()