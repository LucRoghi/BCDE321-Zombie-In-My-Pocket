import cmd, sys

from Model.database_handler import Database
from Model.file_handler import Filehandler
from Model.game import Game


class ZombieInMyPocket(cmd.Cmd):
    intro = 'Welcome to Zombie In My Pocket. Type help or ? for a list of commands \n'
    prompt = '(Main Menu)'
    game = None

    def do_help(self, arg):
        if arg == "all":
            help(ZombieInMyPocket)

    def do_start(self, arg):
        """
        Starts a new game of Zombie In My Pocket.
        Syntax:
        (Main Menu)start
        """
        if self.prompt == "(Main Menu)":
            self.game = Game()
            self.prompt = '(Game)'

    def do_save(self, arg):
        """
        Saves the current game to a .pickle file within the saves' folder.
        A game must be running as indicated by the (Game) prompt.
        Syntax:
        (Game)save [save name]
        """
        file_handler = Filehandler()
        if self.prompt == "(Game)":
            print(f"Saving game as {arg}")
            self.game.game_data.database.mydb = None
            self.game.game_data.database.cursor = None
            file_handler.save_object_to_pickle(arg, self.game)

    def do_load(self, arg):
        """
        Loads a saved .pickle game from within the saves' folder.
        Must be within the main menu as indicated by the (Main Menu)
        Syntax:
        (Main Menu)load [save_name]
        """
        file_handler = Filehandler()
        if self.prompt == "(Main Menu)":
            print(f"Loading game from {arg}")
            self.game = file_handler.load_object_from_pickle(arg)
            self.game.game_data.database = Database("ZombieInMyPocket.db")
            self.prompt = "(Game)"

    def do_tile(self, arg):
        """
        Switches the current command set to (Tile). This allows the Draw, Rotate, Place commands to be used
        Can only switch to Tile Mode if a game is active as indicated by (Game) prompt
        Syntax:
        (Game)tile
        """
        try:
            if self.prompt == "(Game)":
                self.prompt = "(Tile)"
            else:
                raise ValueError("Cannot switch to tile mode if no game is running")
        except ValueError as e:
            print(e)

    def do_player(self, arg):
        """
        Switches the current command set to (Player). This allows the Move, Attack, UseItem, Flee, Cower
        Can only switch to Player Mode if a game is active as indicated by (Game) prompt
        Syntax:
        (Game)player
        """
        try:
            if self.prompt in ("(Game)", "(Tile)", "(Player)", "(Devcard)"):
                self.prompt = "(Player)"
            else:
                raise ValueError("Cannot switch to player mode if no game is running")
        except ValueError as e:
            print(e)

    def do_devcard(self, arg):
        """
        Switched the current command set to (Devcard). This allows the Draw and Use command to be used.
        Can only switch to Devcard Mode if a game is active as indicated by (Game) prompt
        Syntax:
        (Game)devcard
        """
        try:
            if self.prompt in ("(Game)", "(Tile)", "(Player)", "(Devcard)"):
                self.prompt = "(Devcard)"
            else:
                raise ValueError("Cannot switch to devcard mode if no game is running")
        except ValueError as e:
            print(e)
    def do_game(self, arg):
        """
        Switched the current command set to (Game). This allows the Draw and Use command to be used.
        Can only switch to Game Mode if a game is active as indicated by (Game) prompt
        Syntax:
        (Game) game
        """
        try:
            if self.prompt in ("(Game)", "(Tile)", "(Player)", "(Devcard)"):
                self.prompt = "(Game)"
            else:
                raise ValueError("Cannot switch to game mode if no game is running")
        except ValueError as e:
            print(e)
    def do_draw(self, arg):
        """
        Can only be used in within Tile Mode as indicated by (Tile) and switched to using the tile command
        This draws a new tile and stores it as a current_tile within the game. This can be rotated and places using
        rotate and place commands
        Syntax:
        (Tile) draw
        """
        try:
            if self.prompt == "(Tile)":
                self.game.draw_new_tile()
                print(f"Drew a new tile: {self.game.current_tile.room_name}")
            else:
                raise ValueError("You must be in Tile mode to draw a new tile")
        except ValueError as e:
            print(e)

    def do_rotate(self, arg):
        """
        Can only be used in within Tile Mode as indicated by (Tile) and switched to using the tile command
        Rotates the current tile selected using the draw command. By rotating the tile, the location of the doors can
        change such that they can match the previous tile. This command can take left or right as an argument.
        Syntax:
        (Tile) rotate [arg]
        arg = left, right
        """
        try:
            if self.prompt == "(Tile)":
                self.game.rotate_tile(arg)
            else:
                raise ValueError("You must be in Tile mode to rotate the drawn tile")
        except ValueError as e:
            print(e)

    def do_place(self, arg):
        """
        Can only be used in within Tile Mode as indicated by (Tile) and switched to using the tile command
        Places the current tile if the doors match and there is no room in the direction you wish to place the tile
        can only be placed if a tile has been drawn and stored within the current_tile
        Syntax:
        (Tile) place [arg]
        arg: up, right, down, left
        """
        try:
            if self.game.current_tile is not None and self.prompt == "(Tile)":
                self.game.attach_new_tile(arg)
            else:
                raise ValueError("Map tile is not currently drawn. Use tile draw to get a new tile")
        except ValueError as e:
            print(e)

    def do_get(self, arg):
        """
        Prints the doors currently available to the player in their current tile location. If there is a door, the
        direction will have True otherwise it will have False
        Syntax:

        """
        try:
            if self.prompt == "(Game)" and arg == "doors":
                print(self.game.player.current_location)
            elif self.prompt == "(Tile)" and arg == "doors":
                if self.game.current_tile is not None:
                    print(self.game.current_tile)
                else:
                    raise ValueError("No tile is currently drawn")
        except ValueError as e:
            print(e)

    def do_look(self, arg):
        try:
            self.game.print_tile(arg)
        except ValueError as e:
            print(e)

    def do_move(self, arg):
        try:
            if self.prompt == "(Player)":
                self.game.move_player(arg)
            else:
                raise ValueError("You must be in player mode to move the player")
        except ValueError as e:
            print(e)

    def do_attack(self):
        self.prompt = '(Player)'
        self.game.player_attack()

    def do_flee(self, arg):
        self.prompt = '(Player)'
        self.game.player_flee(arg)

    def do_cower(self):
        self.prompt = '(Player)'
        self.game.player_cower()


if __name__ == "__main__":
    ZombieInMyPocket().cmdloop()
