from player import Player
from room import Room
from monster import Monster

some_monster = Monster('batman', 23, 3, 9, 'fiery breath')
boss_monster = Monster('bossman', 40, 5, 15, 'super soaker 2000')

rooms = {
    'outside':  Room("Outside Cave Entrance", "NORTH of you, the cave mount beckons", ['foyer', None, None, None], ['wood sword'], []),
    'foyer':    Room("Foyer", """Dim light filters in from the SOUTH. Dusty passages run NORTH and EAST.""", ['overlook', 'narrow', 'outside', None], ['shield'], []),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, Falling into the darkness. Ahead to the NORTH, a light flickers in the distance, but there is no way across the chasm.""", [None, None, 'foyer', None], [], [some_monster]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from WEST to NORTH. The smell of gold faintly lingers the air.""", ['treasure', None, None, 'foyer'], [], []),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure(..cough... whiskey) chamber! On a golden pedestal in the center of the room, the Sunsword is shining light towards the direction facing NORTH...""", ['boss', None, 'narrow', None], ['sunsword', 'whiskey'], []),
    'boss': Room("Damp Cavern", """This room is filled with the smell of rot and decay. The big-bad of the cavern exits his coffin and is startled to see you.""", [None, None, 'treasure', None], [], [boss_monster]),
}

# Print the current_room name and any items in the room the player is in. The treasure chamber will be special in that you will
# Only see the contents if you have a torch in your inventory, else it will be too dark to see.

def drawitems(player):
    if len(player.current_room.items) > 0:
        # This is going to join the items in the array within a single string to be displayed.
        items_in_room = ', '.join(player.current_room.items)
        print('\033[1;34;40mYou notice %s here.' % (items_in_room))

def drawmonsters(player):
    if len(player.current_room.monsters) > 0:
        print('\033[1;34;40mEnemy alert: %s! Attack or chicken out.' % (player.current_room.monsters[0].name))


def drawroom(player):
    print('\033[1;37;40mCurrent room:', player.current_room.name)
    if player.current_room.name == 'Treasure Chamber' or player.current_room.name == 'Damp Cavern':
        if 'torch' in player.inventory:
            print(player.current_room.description)
            drawitems(player)
            drawmonsters(player)
        else:
            print('\033[1;31;40mIt is way too dark to see! :(')
    else:
        print(player.current_room.description)
        drawitems(player)
        drawmonsters(player)





# Placing the logic for the commands to a single function.
# This function will display the result of the command and will return true or false whether or not to quit the game.


def parse_input(command, player):
    if player.current_room.name == 'Treasure Chamber' or player.current_room.name == 'Damp Cavern':
        if 'torch' in player.inventory:
            user_can_see = True
        else:
            user_can_see = False
    else:
        user_can_see = True

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
    if command[:4] == 'get ' and user_can_see:
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
    
    if command[:7] == 'attack ' and user_can_see:
        monster_name = command[7:len(command)]
        if any(monster.name == monster_name for monster in player.current_room.monsters):
            target_monster = player.current_room.monsters[0]
            player.attack(target_monster)
            if target_monster.current_hp > 0:
                target_monster.attack(player)
            else:
                player.current_room.monsters.remove(target_monster)
        else:
            print('\033[1;31;40mYou do not see a %s here. Thank god.' % (monster_name))
    
    if command == 'drink whiskey' and 'whiskey' in player.inventory:
        player.current_hp = 25
        player.max_hp = 25
        player.inventory.remove('whiskey')
        print("\033[1;34;40mREFRESHING!!! Your health has been fully restored and dulls your sensation to pain.")

    return True


# Get the user's input for their name.
player_name = input('\033[1;33;40mWhat is your name, Adventurer?\n').strip()
print('\033[1;32;40mYour journey begins....%s!' % (player_name))
# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name, rooms['outside'])

# Main game loop:
# 0. Determine if the player has died or beaten the game.
# 1. Display info of the current room including items.
# 2. Ask the user how they want to proceed on their next command.
# 3. Parse the command and figure out the result of their action.
# 4. Determine whether or not to continue the game based on the result of the previous action.

while True:
    if new_player.current_hp <= 0:
       print("\033[1;33;41mYou have been slain! GAME OVER.\n")
       break
    if boss_monster.current_hp <= 0:
       print("\033[1;37;42m!!! You have beaten the game !!! A winner is you !!!\n")
       break
    drawroom(new_player)
    command = input(
        '\033[1;33;40m[HP: %s/%s] Which direction would you like to move? [n] North, [e] East, [s] South, [w] West, [i]Inventory, or [q] Quit\n' % (new_player.current_hp, new_player.max_hp))
    keep_going = parse_input(command.strip().lower(), new_player)
    if keep_going == False:
        break
