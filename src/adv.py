from player import Player
from room import Room

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

# Print the current_room name and any items in the room the player is in. the treasure chamber will be special in that you will
# Only see the contents if you have a torch in your inventory, else it will be too dark to see.


def drawroom(player):
    print('\033[1;37;40mCurrent room:', player.current_room.name)
    if player.current_room.name == 'Treasure Chamber':
        if 'torch' in player.inventory:
            print(player.current_room.description)
        else:
            print('\033[1;31;40mIt is way too dark to see! x__x')
    else:
        print(player.current_room.description)

    if len(player.current_room.items) > 0:
        # This is going to join the items in the array within a single string to be displayed.
        items_in_room = ', '.join(player.current_room.items)
        print('\033[1;34;40mYou notice %s here.' % (items_in_room))

# Placing the logic for the commands to a single function.
# This function will display the result of the command and will return true or false whether or not to quit the game.


def parse_input(command, player):
    if command == 'q':
        print('\033[1;31;40mYou have opted to quit.\n')
        return False

    if command == 'i':
        if len(player.inventory) > 0:
            player_items = ', '.join(player.inventory)
            print('\033[1;32;40m%s is carrying: \033[1;34;40m%s.' %
                  (player.name, player_items))
        else:
            print(
                '\033[1;34;40mItems in inventory: \033[1;31;40mYou got nothin...!')

    if command in ['n', 's', 'e', 'w']:
        new_room = player.move_to(command)
        if new_room != None:
            player.current_room = rooms[new_room]

# Check the first four characters of the command.
    if command[:4] == 'get ':
        item_name = command[4:len(command)]
        if item_name in player.current_room.items:
            player.inventory.append(item_name)
            player.current_room.items.remove(item_name)
            print('\033[1;34;40mYou put the %s in your inventory.' %
                  (item_name))
        else:
            print('\033[1;31;40mThere is no %s in the room!' % (item_name))

# Check the first five characters of the command.
    if command[:5] == 'drop ':
        item_name = command[5:len(command)]
        if item_name in player.inventory:
            player.inventory.remove(item_name)
            player.current_room.items.append(item_name)
            print('\033[1;31;40mYou have dropped the %s.' % (item_name))
        else:
            print('\033[1;31;40mYou dont have a %s, man...' % (item_name))
    return True


# Get the user's input for their name.
player_name = input('\033[1;33;40mWhat is your name, Adventurer?\n').strip()
print('\033[1;32;40mYour journey begins....%s!' % (player_name))
# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name, rooms['outside'])

# Main game loop:
# 1. Display info of the current room including items.
# 2. Ask the user how they want to proceed on their next command.
# 3. Parse the command and figure out the result of their action.
# 4. Determine whether or not to continue the game based ont eh result of the prvious action.

while True:
    drawroom(new_player)
    command = input(
        '\033[1;33;40mWhich direction would you like to move? [n] North, [e] East, [s] South, [w] West, [i]Inventory, or [q] Quit\n')
    keep_going = parse_input(command.strip(), new_player)
    if keep_going == False:
        break
