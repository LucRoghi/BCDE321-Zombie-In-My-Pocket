import cmd, sys

from Model.database_handler import Database
from Model.file_handler import Filehandler
from Model.game import Game


class ZombieInMyPocket(cmd.Cmd):
    intro = 'Welcome to Zombie In My Pocket. Type help or ? for a list of commands \n'
    prompt = '(Main Menu)'
    game = None

    def do_start(self, arg):
        if self.prompt == "(Main Menu)":
            self.game = Game()
            self.prompt = '(Game)'

    def do_save(self, arg):
        file_handler = Filehandler()
        if self.prompt == "(Game)":
            print(f"Saving game as {arg}")
            self.game.game_data.database.mydb = None
            self.game.game_data.database.cursor = None
            file_handler.save_object_to_pickle(arg, self.game)

    def do_load(self, arg):
        file_handler = Filehandler()
        if self.prompt == "(Main Menu)":
            print(f"Loading game from {arg}")
            self.game = file_handler.load_object_from_pickle(arg)
            self.game.game_data.database = Database("ZombieInMyPocket.db")
            self.prompt = "(Game)"

    def do_tile(self, arg):
        try:
            if self.prompt == "(Game)":
                self.prompt = "(Tile)"
            else:
                raise ValueError("Cannot switch to tile mode if no game is running")
        except ValueError as e:
            print(e)

    def do_player(self, arg):
        try:
            if self.prompt in ("(Game)", "(Tile)"):
                self.prompt = "(Player)"
            else:
                raise ValueError("Cannot switch to player mode if no game is running")
        except ValueError as e:
            print(e)

    def do_game(self, arg):
        self.prompt = "(Game)"

    def do_draw(self, arg):
        try:
            if self.prompt == "(Tile)":
                self.game.draw_new_tile()
                print(f"Drew a new tile: {self.game.current_tile.room_name}")
            else:
                raise ValueError("You must be in Tile mode to draw a new tile")
        except ValueError as e:
            print(e)

    def do_rotate(self, arg):
        try:
            if self.prompt == "(Tile)":
                self.game.rotate_tile(arg)
            else:
                raise ValueError("You must be in Tile mode to rotate the drawn tile")
        except ValueError as e:
            print(e)

    def do_place(self, arg):
        try:
            if self.game.current_tile is not None and self.prompt == "(Tile)":
                self.game.attach_new_tile(arg)
            else:
                raise ValueError("Map tile is not currently drawn. Use tile draw to get a new tile")
        except ValueError as e:
            print(e)

    def do_get(self, arg):
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
