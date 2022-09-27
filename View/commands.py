"""
Author: Jared Ireland jai0095

The lis of commands the player can use to play the game
"""
import pickle
import cmd
import View


class Commands(cmd.Cmd):
    intro = 'Welcome, type help or ? to list the commands or start to start the game'

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.player = View.Player()
        self.game = View.Game(self.player)
        self.graph = View.Graph()

    def do_start(self, line):
        """Starts a new game"""
        if self.game.state == "Starting":
            self.game.start_game()
            self.game.get_game()
        else:
            print("Game has already Started")

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
        valid_inputs = ["n", "e", "s", "w"]
        if direction not in valid_inputs:
            return print("Input a valid direction. (Check choose help for more information)")
        if direction == 'n':
            direction = View.Direction.UP
        if direction == "e":
            direction = View.Direction.RIGHT
        if direction == "s":
            direction = View.Direction.DOWN
        if direction == "w":
            direction = View.Direction.LEFT
        if self.game.state == "Choosing Door":
            self.game.can_cower = False
            self.game.choose_door(direction)
        else:
            print("Cannot choose a door right now")

    def do_move_up(self, line):
        """Moves the player North"""
        if self.game.state == "Moving":
            self.game.select_move(View.Direction.UP)
            self.game.get_game()
        else:
            print("Player not ready to move")

    def do_move_right(self, line):
        """Moves the player East"""
        if self.game.state == "Moving":
            self.game.select_move(View.Direction.RIGHT)
            self.game.get_game()
        else:
            print("Player not ready to move")

    def do_move_down(self, line):
        """Moves the player South"""
        if self.game.state == "Moving":
            self.game.select_move(View.Direction.DOWN)
            self.game.get_game()
        else:
            print("Player not ready to move")

    def do_move_left(self, line):
        """Moves the player West"""
        if self.game.state == "Moving":
            self.game.select_move(View.Direction.LEFT)
            self.game.get_game()
        else:
            print("Player not ready to move")

    def do_save(self, line):
        """Takes a filepath and saves the game to a file"""
        if not line:
            return print("Must enter a valid file name")
        else:
            if len(self.game.tiles) == 0:
                return print("Cannot save game with empty map")
            file_name = line + '.pickle'
            with open(file_name, 'wb') as f:
                pickle.dump(self.game, f)

    def do_load(self, name):
        """Takes a filepath and loads the game from a file"""
        if not name:
            return print("Must enter a valid file name")
        else:
            file_name = name + '.pickle'
            try:
                with open(file_name, 'rb') as f:
                    self.game = pickle.load(f)
                    self.game.get_game()
            except FileNotFoundError:
                print("No File with this name exists")

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
        if self.game.state == "Drawing Dev Card":
            self.game.trigger_dev_card(self.game.time)
        else:
            print("Cannot currently draw a card")

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
        self.prompt = line + ': '

    def do_exit(self, line):
        """Exits the game without saving"""
        return True

    def do_status(self, line):
        """Shows the status of the player"""
        if self.game.state != "Game Over":
            self.game.get_player_status()

    def do_graph(self):
        """Shows a graph of the players health over turns"""
        self.graph.player_health_graph()