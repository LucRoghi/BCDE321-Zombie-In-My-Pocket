import cmd
from Model.new_controller import ZIMPController


class NewCommands(cmd.Cmd):
    intro = "The dead walk the earth. You must search the house for the [EVIL TEMPLE] and find the [ZOMBIE TOTEM]. \n" \
            "Then take the totem outside and bury it in the [GRAVEYARD]... all before the clock strikes midnight!"

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller = ZIMPController()
        self.prompt = ZIMPController().prompt

    def do_start(self):
        """
        HELP: Starts a new game
        :return:
        """
        self.controller.start_game()

    def do_player_status(self):
        """
        HELP: Shows the Player and Game status - Time, HP, Attack, Inventory, Location
        :return:
        """
        self.controller.player_status()

    def do_fix_db(self):
        """
        HELP: In case the database storing the rows is broken, running this function will recreate the database
        from the datafiles in the /Data file
        :return:
        """
        self.controller.fix_db()

    def do_move(self):
        """
        HELP: Moves the player in a given direction on prompt using the Cardinal Directions (N/E/S/W)
        :return:
        """
        self.controller.move_player()

    def do_actions(self):
        """
        HELP: The actions the player can do are:
        Attack / Atk (either are usable) - Attacks the zombies for the current Attack Score,
            a zombie dies per attack sore. Any remaining zombies will deal 1 damage to the player.
            i.e. Player has 2 Attack Score and walks into a room with 3 Zombies, 2 of them will die and the player will
                lose 1 HP
        Cower - The user gains 3 HP but loses 1 Development Card
        Flee - Runs out of the room, taking 1 damage
        :return:
        """
        self.controller.player_actions()

    def do_bury_totem(self):
        """
        HELP: When the player is in the Graveyard with the Totem, they will be able to bury it and Win the game
        :return:
        """
        self.controller.bury_totem()

    def drop_item(self):
        """
        HELP: If a player has too many items in their inventory they will have to drop items to make space!
        :return:
        """
        self.controller.drop_item()

    def do_save(self):
        """
        HELP: Saves the game
        :return:
        """
        self.controller.file_handler_save()

    def do_load(self):
        """
        HELP: Loads the game
        :return:
        """
        self.controller.file_handler_load()

    def do_restart(self):
        """
        HELP: Restarts the game
        :return:
        """
        self.controller.restart_game()

    def do_use_item(self):
        """
        HELP: Uses a selected item
        :return:
        """
        self.controller.use_item()

    def get_totem(self):
        """
        HELP: Enables the player to get the totem if specific conditions are met
        :return:
        """
        self.controller.get_totem()

    def do_exit(self):
        """
        HELP: Exits the game without saving
        :return:
        """
        self.controller.exit_game()


if __name__ == "__main__":
    NewCommands().cmdloop()
