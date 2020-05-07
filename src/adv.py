# Imports
from room import Room
from player import Player

# Declare all the rooms and link them together

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "NORTH of you, the cave mount beckons", ['foyer', None, None, None], ['wooden broad sword']),

    'foyer':    Room("Foyer", """Dim light filters in from the SOUTH. Dusty
passages run NORTH and EAST.""", ['overlook', 'narrow', 'outside', None], ['shield']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the NORTH, a light flickers in
the distance, but there is no way across the chasm.""", [None, None, 'foyer', None], ['torch']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from WEST
to NORTH. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer'], []), 

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
Sadly, it has already been completely emptied by earlier adventurers. 
""", [None, None, 'narrow', None], [])
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
    print('\033[1;33;40mCurrent room:', new_player.current_room.name)
    if new_player.current_room.name == 'Treasure Chamber': 
        if 'torch' in new_player.inventory:
            print(new_player.current_room.description)
        else:
            print("It's too dark to see!")
    else: 
        print(new_player.current_room.description)

    if len(new_player.current_room.items) > 0:
        items_in_room = ', '.join(new_player.current_room.items)
        print("You notice %s here." % (items_in_room))
    command = input('\033[1;32;40mWhich direction would you like to move? [n] North, [e] East, [s] South, [w] West, or [q] Quit\n')

    if command == 'q':
        print("\033[1;31;40mYou have opted to quit.\n")
        break
    if command == 'i':
        if len(new_player.inventory) > 0:
            player_items = ', '.join(new_player.inventory)
            print("Items in iventory: %s" % (player_items))
        else:
            print("You got nothin...")
    
    if command in ['n', 's', 'e', 'w']:
        new_room = new_player.move_to(command)
        if new_room != None:
            new_player.current_room = rooms[new_room]
        continue
    if command[:4] == 'get ':
        item_name = command [4:len(command)]
        if item_name in new_player.current_room.items:
            new_player.inventory.append(item_name)
            new_player.current_room.items.remove(item_name)
            print("You got the %s." %(item_name))
        else:
            print("There is no %s in the room." % (item_name))
    if command[:5] == 'drop ':
        item_name = command [5:len(command)]
        if item_name in new_player.inventory:
            new_player.inventory.remove(item_name)
            new_player.current_room.items.append(item_name)
            print("You've dropped the %s." %(item_name))
        else:
            print("You dont have a %s, man..." % (item_name))
