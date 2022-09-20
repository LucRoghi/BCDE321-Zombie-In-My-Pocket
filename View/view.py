import cmd, sys

from Model.game import Game


class ZombieInMyPocket(cmd.Cmd):
    intro = 'Welcome to Zombie In My Pocket. Type help or ? for a list of commands \n'
    prompt = '(Main Menu)'
    game = None

    def do_new_game(self, arg):
        self.game = Game()
        self.prompt = '(Game)'

    def do_draw(self, arg):
        self.prompt = '(Drawing)'
        try:
            arg_dictionary = {"tile": self.game.draw_new_tile(),
                              "devcard": self.game.draw_new_dev_card()}
            arg_dictionary(arg)
        except KeyError:
            print("Invalid Option: Command must have tile or devcard as the arguments")

    def do_tile(self, args):
        try:
            arg_list = args.split()
            if arg_list[0] == "draw":
                self.game.draw_new_tile()
                print(f"Drew a new tile: {self.game.current_tile.room_name}")
            elif arg_list[0] == "rotate":
                self.game.rotate_tile(arg_list[1])
            elif arg_list[0] == "place":
                self.game.attach_new_tile(self.game.current_tile, arg_list[1])
                print(f"Attached tile {self.game.player.current_location.room_name} to {self.game.current_tile} "
                      f"going {arg_list[1]}")
        except ValueError as e:
            print(e)

    def do_get(self, arg):
        if arg == "doors":
            print(self.game.player.current_location.get_doors())

    def do_move(self, arg):
        self.prompt = '(Player)'
        try:
            self.game.move_player(arg)
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
