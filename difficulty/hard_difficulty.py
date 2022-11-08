import difficulty


class HardDifficulty(difficulty.AbstractDifficulty):
    def __init__(self):
        self.game = difficulty.Game(difficulty.Player)

    def set_difficulty(self):
        self.game.difficulty = "Hard"
        player = self.game.get_player()
        player.set_health(4)
        player.set_attack(1)
