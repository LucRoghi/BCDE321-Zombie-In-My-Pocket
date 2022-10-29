import model


class MediumDifficulty(AbstractDifficulty):
    def __init__(self, game):
        self.game = game

    def set_difficulty(self):
        self.game.difficulty = "Medium"
        player = self.game.get_player()
        player.set_health(6)
        player.set_attack(1)