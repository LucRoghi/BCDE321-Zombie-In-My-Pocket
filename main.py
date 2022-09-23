"""
Main executor of the code
"""
import cmd

from View.view import ZombieInMyPocket

if __name__ == "__main__":
    ZombieInMyPocket.cmdloop(cmd.Cmd)
