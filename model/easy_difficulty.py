import model


class EasyDifficulty(model.AbstractDifficulty):
    def __init__(self, game):
        self.game = game

    def set_difficulty(self):
        self.game.difficulty = "Easy"
        player = self.game.get_player()
        player.set_health(10)
        player.set_attack(2)
