import difficulty


class EasyDifficulty(difficulty.AbstractDifficulty):
    def __init__(self):
        self.game = difficulty.Game(difficulty.Player)

    def set_difficulty(self):
        self.game.difficulty = "Easy"
        player = self.game.get_player()
        player.set_health(10)
        player.set_attack(2)
