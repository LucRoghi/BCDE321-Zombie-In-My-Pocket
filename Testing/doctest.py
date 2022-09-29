# Player
# Tile
# DevCard
# Game

if __name__ == "__main__":
    import doctest
    print(doctest.__file__)
    doctest.testfile("player_doctest.txt")
    doctest.testfile("outdoor_tile_doctest.txt")
    doctest.testfile("indoor_tile_doctest.txt")
    doctest.testfile("dev_card_doctest.txt")
    doctest.testfile("game_doctest.txt")
