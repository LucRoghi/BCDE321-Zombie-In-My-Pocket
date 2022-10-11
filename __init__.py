"""
Main executor of the code
"""

from cmd import *
from View.view import ZombieInMyPocket

if __name__ == "__main__":
    game_instance = ZombieInMyPocket()
    game_instance.cmdloop(Cmd)
