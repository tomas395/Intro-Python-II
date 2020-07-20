from random import randrange

class Player:

    def __init__(self, name, current_room):
        self.current_room = current_room
        self.max_hp = 20
        self.current_hp = 20
        self.inventory = []
        self.name = name

    def move_to(self, direction):
        if direction == 'n':
            room_index = 0
        elif direction == 'e':
            room_index = 1
        elif direction == 's':
            room_index = 2
        elif direction == 'w':
            room_index = 3

        if self.current_room.exits[room_index] == None:
            print("\033[1;31;40mYou cannot move in that direction!\n")
            return None
        else:
            return self.current_room.exits[room_index]

    def attack(self, monster):
        if 'wood sword' in self.inventory:
            attack_dmg = randrange(3, 8)
            weapon_name = 'wood sword'
            crit_chance = 10
        elif 'sunsword' in self.inventory:
            attack_dmg = randrange(7, 14)
            weapon_name = 'sunsword'
            crit_chance = 5
            
        else:
            attack_dmg = randrange(1,4)
            weapon_name = 'fists'
            crit_chance = 20


        if randrange(1,crit_chance) == 1:
            attack_dmg = attack_dmg * 2
            print("\033[1;31;40mTERRIFIC BLOW!!! You smashed %s with your %s for %s damage!\n" % (monster.name, weapon_name, attack_dmg))
        else:
            print("\033[1;31;40mYou deal %s damage to %s with your %s!\n" % (attack_dmg, monster.name, weapon_name))

        monster.current_hp = monster.current_hp - attack_dmg

        if monster.current_hp <= 0:
            print("\033[1;31;40mYou have slain the beast! X__X\n")
            self.current_room.items.append('torch')

