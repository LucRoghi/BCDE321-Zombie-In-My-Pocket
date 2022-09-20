import cmd, sys

from Model.game import Game


class ZombieInMyPocket(cmd.Cmd):
    intro = 'Welcome to Zombie In My Pocket. Type help or ? for a list of commands \n'
    prompt = '(Main Menu)'
    game = None

    def do_new_game(self, arg):
        self.game = Game()
        self.game.start_game()
        self.prompt = '(Game)'

    def do_draw(self, arg):
        self.prompt = '(Drawing)'
        try:
            arg_dictionary = {"tile": self.game.draw_new_tile(),
                              "devcard": self.game.draw_new_dev_card()}
            arg_dictionary(arg)
        except KeyError:
            print("Invalid Option: Command must have tile or devcard as the arguments")

    def do_tile(self, arg):
        try:
            if arg.lower() in ["up", "down", "left", "right"]:
                tile = self.game.draw_new_tile()
                print(f'Drew the {tile.room_name} card')
                self.game.attach_new_tile(tile, arg)
                print(f'Attached {tile.room_name} to {self.game.player.current_location.room_name}')
            else:
                print("Argument must be up, down, left or right")
        except ValueError as e:
            print(e)

    def do_get(self, arg):
        if arg == "doors":
            self.game.player.current_location.print_doors()
    def do_move(self, arg):
        self.prompt = '(Player)'
        self.game.move_player(arg)
        print(f"Current location is: {self.game.player.current_location.room_name}")

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
