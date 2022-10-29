import os
import shelve
import controller


class FileHandler:
    def __int__(self):
        self.player = controller.Player()
        self.game = controller.Game(self.player)

    def save(self, line, name):
        if not name:
            return print("Must enter a valid file name")
        else:
            name = name.lower().strip()
            file_name = name + ".db"
            game_shelve = shelve.open("../save/" + file_name)
            game_shelve["game"] = self.game
            self.game.get_game()
            game_shelve.close()

    def load(self, name):
        if not name:
            return print("Must enter a valid file name")
        else:
            name = name.lower().strip()
            try:
                file_exists = os.path.exists("../save/" + name + ".dat")
                if not file_exists:
                    raise FileNotFoundError
                game_shelve = shelve.open("../save/" + name)
                game_shelve["game"] = self.game
                self.game.get_game()
                game_shelve.close()
            except FileNotFoundError:
                print(f"No File with this name, {name} exists")
