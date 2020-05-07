# Imports
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "NORTH of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the SOUTH. Dusty
passages run NORTH and EAST."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the NORTH, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from WEST
to NORTH. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
Sadly, it has already been completely emptied by earlier adventurers. 
The ground shakes heavy under your feet and the rocks block the path you came in, so you should feel bad. 
To escape with your life, you can dig a hole SOUTH to see where it leads you."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['foyer']

#
# Main
#

# answer = input('Would you like to start your mini-adventure? (yes/no')

# if answer.lower().strip() == "yes":

#     answer = input("Excellent! Your starting point is outside the cave entrance.")

# else:
#     print('Thats cool too.')


# Make a new player object that is currently in the 'outside' room.

new_player = Player('Erdrick', room['outside'])

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

    elif new_player.current_room.name == room["outside"].name and command == 'n':
        new_player.current_room = room['outside'].n_to

    elif new_player.current_room.name == room["foyer"].name and command == 'n':
        new_player.current_room = room['foyer'].n_to

    elif new_player.current_room.name == room["foyer"].name and command == 's':
        new_player.current_room = room['foyer'].s_to

    elif new_player.current_room.name == room["foyer"].name and command == 'e':
        new_player.current_room = room['foyer'].e_to

    elif new_player.current_room.name == room["overlook"].name and command == 's':
        new_player.current_room = room['overlook'].s_to

    elif new_player.current_room.name == room["narrow"].name and command == 'n':
        new_player.current_room = room['narrow'].n_to

    elif new_player.current_room.name == room["narrow"].name and command == 'w':
        new_player.current_room = room['narrow'].w_to

    elif new_player.current_room.name == room["treasure"].name and command == 's':
        new_player.current_room = room['narrow'].w_to

    else:
        print("THIS IS NOT A VALID DIRECTION. You have opted to think it over some more.")

