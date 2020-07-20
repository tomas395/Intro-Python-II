from random import randrange

class Monster:

    def __init__(self, name, current_hp, mindmg, maxdmg, weapon_name):
        self.name = name
        self.current_hp = current_hp
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.weapon_name = weapon_name

    def attack(self, user):
        attack_dmg = randrange(self.mindmg, self.maxdmg)
        
        # If they have a shield, subtract 3-6 damage.
        if 'shield' in user.inventory:
            attack_dmg = attack_dmg - randrange(3,6)

        # Dont allow negative attacks.
        if attack_dmg < 0:
            attack_dmg = 0

        # Subtract the damage from the players hp.
        user.current_hp = user.current_hp - attack_dmg
        
        if attack_dmg > 0:
            print("\033[1;31;40m%s deals %s damage to you with it's %s!\n" % (self.name, attack_dmg, self.weapon_name))
        else:
            print('You have blocked the attack from %s!' % (self.name))