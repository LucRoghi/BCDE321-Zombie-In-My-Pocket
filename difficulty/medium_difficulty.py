import difficulty


class MediumDifficulty(difficulty.AbstractDifficulty):
    def __init__(self):
        self.game = difficulty.Game(difficulty.Player)

    def set_difficulty(self):
        self.game.difficulty = "Medium"
        player = self.game.get_player()
        player.set_health(6)
        player.set_attack(1)
