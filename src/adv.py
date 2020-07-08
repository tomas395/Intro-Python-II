from player import Player
from room import Room

rooms = {
    'outside':  Room("Outside Cave Entrance.",
                     "To the NORTH of you, the cave mount beckons!", ['foyer', None, None, None]),

    'foyer':    Room("Foyer.", """\nDim light filters in from the SOUTH and dusty
passages run NORTH and EAST...""", ['overlook', 'narrow', 'outside', None]),

    'overlook': Room("Grand Overlook.", """\nA steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but it's a shame there is no way across the chasm.""", [None, None, 'foyer', None]),

    'narrow':   Room("Narrow Passage.", """\nThe narrow passage bends here from WEST
to NORTH. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer']),

    'treasure': Room("Treasure Chamber.", """\nYou've found the long-lost treasure
chamber!!! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the SOUTH.""", [None, None, 'narrow', None]),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']


# Make a new player object that is currently in the 'outside' room.
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
    print('\033[1;33;40mYou are now in the',
          new_player.current_room.name, new_player.current_room.description)
    player_input = input(
        '\n\033[1;33;40mPress which direction you would like to move:  [n] North, [e] East, [s] South, [w] West, or [q] Quit\n')
    if player_input == 'q':
        print("\033[1;31;40mYou have opted to quit.\n")
        break
    if player_input in ['n', 's', 'e', 'w']:
        new_room = new_player.move_to(player_input)
    if new_room != None:
        new_player.current_room = rooms[new_room]
