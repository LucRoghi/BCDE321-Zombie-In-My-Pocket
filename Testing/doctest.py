# Player
# Tile
# DevCard
# Game
if __name__ == "__main__":
    import doctest
    doctest.testfile("Model/player.py")
    doctest.testfile("Model/outdoor_tile.py")
    doctest.testfile("Model/indoor_tile.py")
    doctest.testfile("Model/dev_card.py")
    doctest.testfile("Controller/game.py")
