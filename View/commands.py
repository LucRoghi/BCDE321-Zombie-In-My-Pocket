"""
Author: Jared Ireland jai0095

The lis of commands the player can use to play the game
"""
import os
import pickle
import cmd
import shelve

import View
import sys


class Commands(cmd.Cmd):
    intro = 'Welcome, type help or ? to list the commands or start to start the game'

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.player = View.Player()
        self.game = View.Game(self.player)
        self.graph = View.Graph()
        if len(sys.argv) > 1:
            try:
                self.do_load(sys.argv[1])
            except Exception:
                print("File not found")

    def get_game(self):
        return self.game

    def do_start(self, line):
        """Starts a new game"""
        if self.game.state == "Starting":
            self.game.start_game()
            self.game.get_game()
        else:
            print("Game has already Started")

    # TODO - Add arguments for multiple rotation
    def do_rotate(self, line):
        """Rotates the current map piece 1 rotation clockwise"""
        if self.game.state == "Rotating":
            self.game.rotate()
            self.game.get_game()
        else:
            print("Tile not chosen to rotate")

    def do_place(self, line):
        """Places the current map tile"""
        if self.game.state == "Rotating":
            if self.game.chosen_tile.name == "Foyer":
                self.game.place_tile(16, 16)
            elif self.game.check_dining_room_has_exit() is False:
                return print("Dining room entrance must face an empty tile")
            else:
                if self.game.get_current_tile().name == "Dining Room" \
                        and self.game.current_move_direction == self.game.get_current_tile().entrance:
                    if self.game.check_entrances_align():
                        self.game.place_tile(self.game.chosen_tile.x, self.game.chosen_tile.y)
                        self.game.move_player(self.game.chosen_tile.x, self.game.chosen_tile.y)
                elif self.game.check_doors_align(self.game.current_move_direction):
                    self.game.place_tile(self.game.chosen_tile.x, self.game.chosen_tile.y)
                    self.game.move_player(self.game.chosen_tile.x, self.game.chosen_tile.y)
                else:
                    print(" Must have at least one door facing the way you came from")
            self.game.get_game()
        else:
            print("Tile not chosen to place")

    def do_choose(self, direction):
        """When a zombie door attack is completeDirection. Use this command to select an exit door with a valid
        direction """
        valid_inputs = ["up", "right", "down", "left"]
        if direction.lower() not in valid_inputs:
            return print("Input a valid direction. (Check choose help for more information)")
        if direction.lower() == 'up':
            direction = View.Direction.UP
        if direction.lower() == "right":
            direction = View.Direction.RIGHT
        if direction.lower() == "down":
            direction = View.Direction.DOWN
        if direction.lower() == "left":
            direction = View.Direction.LEFT
        if self.game.state == "Choosing Door":
            self.game.can_cower = False
            self.game.choose_door(direction)
        else:
            print("Cannot choose a door right now")

    # TODO - Pattern Matching https://peps.python.org/pep-0636/
    def do_move(self, direction):
        move_dic = View.Game.move_dic
        if self.game.state == "Moving":
            if direction is None:
                print("Can not move!")
            if direction == 'up':
                self.game.move_dic("up")
                self.game.get_game()
            if direction == "right":
                self.game.move_dic("right")
                self.game.get_game()
            if direction == "down":
                self.game.move_dic("down")
                self.game.get_game()
            if direction == "left":
                self.game.move_dic("left")
                self.game.get_game()

    # def do_move_up(self, line):
    #     """Moves the player North"""
    #     if self.game.state == "Moving":
    #         self.game.select_move(View.Direction.UP)
    #         self.game.get_game()
    #     else:
    #         print("Player not ready to move")
    #
    # def do_move_right(self, line):
    #     """Moves the player East"""
    #     if self.game.state == "Moving":
    #         self.game.select_move(View.Direction.RIGHT)
    #         self.game.get_game()
    #     else:
    #         print("Player not ready to move")
    #
    # def do_move_down(self, line):
    #     """Moves the player South"""
    #     if self.game.state == "Moving":
    #         self.game.select_move(View.Direction.DOWN)
    #         self.game.get_game()
    #     else:
    #         print("Player not ready to move")
    #
    # def do_move_left(self, line):
    #     """Moves the player West"""
    #     if self.game.state == "Moving":
    #         self.game.select_move(View.Direction.LEFT)
    #         self.game.get_game()
    #     else:
    #         print("Player not ready to move")

    def do_save(self, name):
        """Takes a filepath and saves the game to a file"""
        if not name:
            return print("Must enter a valid file name")
        else:
            name = name.lower().strip()
            file_name = name + ".db"
            game_shelve = shelve.open("../save/" + file_name)
            game_shelve["game"] = self.game
            self.game.get_game()
            game_shelve.close()

    def do_load(self, name):
        """Loads a game specifically from the 'save' sub-folder"""
        if not name:
            return print("Must enter a valid file name")
        else:
            name = name.lower().strip()
            if ".db" not in name:
                file_name = name + ".db"
            else:
                file_name = name
            try:
                file_exists = os.path.exists("../save/" + file_name + ".dat")
                if not file_exists:
                    raise FileNotFoundError
<<<<<<< HEAD
                game_shelve = shelve.open("../save/" + file_name)
                save = self.game
                game_shelve["game"] = save
=======
                game_shelve = shelve.open("../save/" + name)
                save = game_shelve["game"]
                self.game = save
>>>>>>> parent of 62df723 (DocTest work UnitTest Dont)
                self.game.get_game()
                game_shelve.close()
            except FileNotFoundError:
                print(f"No File with this name, {file_name} exists")

    def do_restart(self, line):
        """Deletes your progress and ends the game"""
        del self.game
        del self.player
        self.player = View.Player()
        self.game = View.Game(self.player)

    def do_attack(self, line):
        """Player attacks the zombies"""
        arg1 = ''
        arg2 = 0
        if "," in line:
            arg1, arg2 = [item for item in line.split(", ")]
        else:
            arg1 = line

        if self.game.state == "Attacking":
            if arg1 == '':
                self.game.trigger_attack()
            elif arg2 == 0:
                self.game.trigger_attack(arg1)
            elif arg1 != '' and arg2 != 0:
                self.game.trigger_attack(arg1, arg2)

            if len(self.game.chosen_tile.doors) == 1 and self.game.chosen_tile.name != "Foyer":
                self.game.state = "Choosing Door"
                self.game.get_game()
            if self.game.state == "Game Over":
                print("You lose, game over, you have succumbed to the zombie horde")
                print("To play again, type 'restart'")
            else:
                self.game.get_game()
        else:
            print("You cannot attack right now")

    def do_use(self, line):
        """Player uses item"""
        arg1 = ''
        arg2 = 0
        if "," in line:
            arg1, arg2 = [item for item in line.split(", ")]
        else:
            arg1 = line

        if self.game.state == "Moving":
            if arg1 == '':
                return
            if arg2 == 0:
                self.game.use_item(arg1)
            elif arg1 != '' and arg2 != 0:
                self.game.use_item(arg1, arg2)
        else:
            print("You cannot do that right now")

    # Not finished yet, needs testing for spelling
    def do_drop(self, item):
        """Drops an item from your hand"""
        if self.game.state != "Game Over":
            self.game.drop_item(item)
            self.game.get_game()

    def do_swap(self, line):
        """Swaps an item in you hand with the one in the room"""
        if self.game.state == "Swapping Item":
            self.game.drop_item(line)
            self.game.player.add_item(self.game.room_item[0], self.game.room_item[1])
            self.game.room_item = None
            self.game.get_game()

    def do_draw(self, line):
        """Draws a new development card (Must be done after evey move)"""
        self.game.draw_dev_card()

    # DELETE LATER, DEV COMMANDS FOR TESTING
    def do_give(self, line):
        self.game.player.add_item("Oil", 2)

    def do_give2(self, line):
        self.game.player.add_item("Candle", 1)

    def do_run(self, direction):
        """Given a direction will flee attacking zombies at a price of one health"""
        if self.game.state == "Attacking":
            if direction == 'n':
                self.game.trigger_run(View.Direction.UP)
            elif direction == 'e':
                self.game.trigger_run(View.Direction.RIGHT)
            elif direction == 's':
                self.game.trigger_run(View.Direction.DOWN)
            elif direction == 'w':
                self.game.trigger_run(View.Direction.LEFT)
            else:
                print("Cannot run that direction")
            if len(self.game.get_current_tile().doors) == 1 and self.game.chosen_tile.name != "Foyer":
                self.game.state = "Choosing Door"
                self.game.get_game()
        else:
            print("Cannot run when not being attacked")

    def do_cower(self, line):
        """When attacked use this command to cower. You will take no damage but will advance the time"""
        if self.game.state == "Moving":
            self.game.trigger_cower()
        else:
            print("Cannot cower while right now")

    def do_search(self, line):
        """Searches for the zombie totem. (Player must be in the evil temple and will have to resolve a dev card)"""
        if self.game.state == "Moving":
            self.game.search_for_totem()
        else:
            print("Cannot search currently")

    def do_bury(self, line):
        """Buries the totem. (Player must be in the graveyard and will have to resolve a dev card)"""
        if self.game.state == "Moving":
            self.game.bury_totem()
        else:
            print("Cannot currently bury the totem")

    def do_prompt(self, line):
        """Change the interactive prompt"""
        if self.prompt == "> ":
            self.prompt = line + ' '
        else:
            self.prompt = "> "

    def do_exit(self, line):
        """Exits the game without saving"""
        return True

    def do_status(self, line):
        """Shows the status of the player"""
        if self.game.state != "Game Over":
            self.game.get_player_status()

    def do_graph(self, line):
        """Shows a graph of the players health over turns"""
        self.graph.player_health_graph()
