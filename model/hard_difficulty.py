import model


class HardDifficulty(model.AbstractDifficulty):
    def __init__(self, game):
        self.game = game

    def set_difficulty(self):
        self.game.difficulty = "Hard"
        player = self.game.get_player()
        player.set_health(4)
        player.set_attack(1)