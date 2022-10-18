# TODO - TestFile broken
if __name__ == "__main__":
    import doctest

    doctest.testfile("../Model/player.py")
    doctest.testfile("../Model/outdoor_tile.py")
    doctest.testfile("../Model/indoor_tile.py")
    doctest.testfile("../Model/dev_card.py")
    doctest.testfile("../Controller/game.py")

"""
    Note: This is still broken - for some reason doctest.testfile() doesn't exist yet wiki says otherwise:
    https://docs.python.org/3/library/doctest.html
    Its best to just go to the files listed above and run the doctests in there
"""