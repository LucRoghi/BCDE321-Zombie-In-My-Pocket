import cmd, sys

from Model.game import Game


class ZombieInMyPocket(cmd.Cmd):
    intro = 'Welcome to Zombie In My Pocket. Type help or ? for a list of commands \n'
    prompt = '(Main Menu)'
    game = None

    def do_new_game(self, arg):
        self.game = Game()
        self.prompt = '(Game)'

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
            if self.prompt == "(Game)":
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
