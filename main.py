"""
Game Logic:
At the start, dispose of 2 random development cards from the deck
A player starts with 1 attack / 6 health (You lose health based on Zombie number - Attack
ie 4 Zombies - 1 Attack = 3 Health lost)
If a player flees from a room, you lose one health
Player must place a new tile to a doorway if they wish to travel through a door with no connected room
Player must draw a development card after entering a new room (Even a previously visited one)
If a zombie effect is drawn, the current number of zombies in the room is updated from the number on the card
If a regular effect is drawn, perform the effect (+1 player health, -1 player health, you are scared/nothing etc)
If an item effect is drawn, draw a new development card and put the item in the bottom right corner into inventory
A player can only carry 2 items at a time
A player can perform 3 actions while in a room:
Cower: The player can hide in the corner of the room to recover 1 health BUT a development card is discarded
Flee: The player can leave the room if the risk is too high BUT the player will lose 1 health
Attack: The player can choose to stand his ground and fight the zombies BUT the player will lose health based on
the number of zombies
Time will only progress after a deck reshuffle (9pm to 10pm on first reshuffle and 10pm to 11pm on second reshuffle)
If the player reaches a dead end and cannot place a map tile, 3 zombies will bash down a wall and create an opening
The only way to exit the indoor tile set is to draw the dining room tile such that the exit is not connected
to a current room
Player wins if the totem from the Evil Temple is buried in the Graveyard
Player loses if health drops to 0 OR
"""
