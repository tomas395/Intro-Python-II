# Imports
from room import Room
from player import Player

# Declare all the rooms and link them together

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "NORTH of you, the cave mount beckons", ['foyer', None, None, None]),

    'foyer':    Room("Foyer", """Dim light filters in from the SOUTH. Dusty
passages run NORTH and EAST.""", ['overlook', 'narrow', 'outside', None]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the NORTH, a light flickers in
the distance, but there is no way across the chasm.""", [None, None, 'foyer', None]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from WEST
to NORTH. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
Sadly, it has already been completely emptied by earlier adventurers. 
""", [None, None, 'narrow', None])
}

#
# Main
#

# answer = input('Would you like to start your mini-adventure? (yes/no')

# if answer.lower().strip() == "yes":

#     answer = input("Excellent! Your starting point is outside the cave entrance.")

# else:
#     print('Thats cool too.')


# Make a new player object that is currently in the 'outside' room.
# you can make name = input later?
new_player = Player('Erdrick', rooms['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print("Current room:", new_player.current_room.name)
    print(new_player.current_room.description)

    command = input('Which direction would you like to move? [n] North, [e] East, [s] South, [w] West, or [q] Quit\n')

    if command == 'q':
        break
    if command in ['n', 's', 'e', 'w']:
        new_room = new_player.move_to(command)
        if new_room != None:
            new_player.current_room = rooms[new_room]
        continue