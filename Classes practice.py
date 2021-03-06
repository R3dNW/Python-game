#Github copy
import random
import math
Floor = 2



class Item:
    name = ""
    description = ""
    effect_type = ""
    boost_type = ""
    potency = 0

#------------------------------------------------------------------------------------------------------------------------------------------

Potion_file = open("Items list.txt","r")
Potion = Potion_file.read()
Potion_file.close()
Potion = Potion.split("\n")
Potion_file = open("Items list.txt","r")

items = []

for line in range(0,len(Potion)):
    item = Item()
    potions = Potion_file.readline()
    potions = potions.strip("\n")
    potions = potions.split(";")
    item.name = potions[0]
    item.description = potions[1]
    item.effect_type = potions[2]
    item.boost_type = potions[3]
    item.potency = int(potions[4])
    items.append(item)

Potion_file.close()

#------------------------------------------------------------------------------------------------------------------------------------------



class Party:
    name = ""
    level = 3
    life = 10
    strength = 10
    defence = 10
    experience = 10
    level = int(experience/10)
    inventory = {}
    life_bonus = 0
    strength_bonus = 0
    defence_bonus = 0
    passive_inventory = []
    active_inventory = [items[5]]
    position = ""

    def bonus(self):
        for i in self.passive_inventory:
            if i.effect == "P":
                if i.type == "Health":
                    self.life_bonus = i.potencey
                elif i.type == "Defence":
                    self.defence_bonus = i.potencey
                elif i.type == "Strength":
                    self.strength_bonus = i.potencey

    def item(self):
        counter = 0
        b = 1
        print("Use 'w' and 's' to search and use 'x' to select.")
        while b != "x":
            b = input()
            clear()
            if b == "w":
                counter = counter - 1
            elif b == "s":
                counter = counter + 1
            elif b == "x":
                break
            else:
                c = 0
                
            for i in range(0,len(self.active_inventory)):
                if i == counter:
                    print("--" + self.active_inventory[i].name)
                    a = self.active_inventory[i].description
                    print(a)
                else:
                    print(self.active_inventory[i].name)
                print()
        print("You selected: " + self.active_inventory[counter].name)
        print("            " + self.active_inventory[counter].description)

        if self.active_inventory[counter].boost_type == "Health":
            self.life_bonus = self.life_bonus + self.active_inventory[counter].potency
        elif self.active_inventory[counter].boost_type == "Defence":
            self.defence_bonus = self.defence_bonus + self.active_inventory[counter].potency
        elif self.active_inventory[counter].boost_type == "Strength":
            self.strength_bonus = int(self.strength_bonus) + int(self.active_inventory[counter].potency)
            print(self.active_inventory[counter].potency)
            print(self.strength_bonus)
        self.active_inventory.pop(counter)


    def stats(self):
        print(self.strength_bonus)
        if self.position == "Battle":
            self.life = self.life + self.life_bonus
        else:
            self.life = (self.level*4) + self.life_bonus
        self.strength = (self.level*4) + self.strength_bonus
        self.defence = (self.level*2) + self.defence_bonus
        print(self.strength_bonus)
        print(self.strength)


#------------------------------------------------------------------------------------------------------------------------------------------

class Enemy:
    level = 0
    name = ""
    life = level*3
    strength = level*3
    defence = level*2
    item = []

    def __init__(self):
        boop = random.randint(1,Floor)
        self.level = boop
        names_list = ["Jerry","Bob","Karl","Carl","Lebron","James","Steve","Joe","Jack","John","Amy","Sarah","Anne","Micheal","Ian",]
        chooser = random.randint(0,self.level)
        self.item = items[chooser]
        self.name = names_list[random.randint(0,len(names_list))]


#------------------------------------------------------------------------------------------------------------------------------------------
        
def clear():
    print("\n"*50)

#------------------------------------------------------------------------------------------------------------------------------------------

def create_party():
    global ally_dic
    global party_list
    ally1 = Party()
    ally2 = Party()
    ally3 = Party()
    ally4 = Party()
    party_list = [ally1,ally2,ally3,ally4]
    print("You have 4 party members ")
    for members in party_list:
        members.name = input("Name of ally: ")
    ally_dic = {ally1.name:ally1,ally2.name:ally2,ally3.name:ally3,ally4.name:ally4}

#------------------------------------------------------------------------------------------------------------------------------------------

def create_enemy():
    global enemy_list
    global names_list
    enemy_list = []
    for i in range(0,random.randint(1,Floor)):
        enemy_list.append(0)
        enemy_list[i] = Enemy()

#------------------------------------------------------------------------------------------------------------------------------------------

def choice_A(i):
    damage = i.strength
    victim = int(input("Who do you want to attack? "))
    print("Defence = " + str(enemy_list[victim].defence) + " and attack power = " + str(damage))
    if enemy_list[victim].defence > int(damage):
        print("Attack too weak, 0 damage!")
        print("the enemy has " + str(enemy_list[victim].life) + " life remaing.")
    else:
        enemy_list[victim].life = enemy_list[victim].life - (damage - enemy_list[victim].defence)
        print(i.name + " attacked " + enemy_list[victim].name + " for " + str(damage) + "LIFR points.")
        print(enemy_list[victim].name + " has " + str(enemy_list[victim].life) + " LIFE points remaining.")
        if enemy_list[victim].life <= 0:
            if enemy_list[victim].item.effect_type == "A":               
                i.active_inventory.append(enemy_list[victim].item)
            else:
                i.passive_inventory.append(enemy_list[victim].item)
            print("The enemy dropped a: " + enemy_list[victim].item.name + " and " + i.name + " picked it up.")
            enemy_list.pop(victim)
        else:
            print(enemy_list[victim].life)

#------------------------------------------------------------------------------------------------------------------------------------------

def choice(i):
    for x in range(0,len(enemy_list)):
        print (enemy_list[x].name + "[" + str(x) + "]" )
        print ("Life: " + str(enemy_list[x].life))
    action = input("""What will you do?
        Attack
        Defend
        Item
        Run(15%)
        """)
    action = action.upper()
    if action == "A" or action == "ATTACK":
        choice_A(i)
        

    elif action == "D" or action == "DEFENCE":
        i.defence = i.defence*2

    elif action == "I" or action == "ITEM":
        if len(i.active_inventory) == 0:
            print("You have no items")
            choice(i)
        else:
            i.item()
            i.stats()
            choice(i)
            
#------------------------------------------------------------------------------------------------------------------------------------------


def battle():
    for i in party_list:
        i.position = "Battle"
    while len(party_list) > 0 and len(enemy_list) > 0:
        for i in party_list:
            i.stats()
            choice(i)
            if len(enemy_list) <= 0 or len(party_list) <= 0:
                break
        if len(enemy_list) <= 0 or len(party_list) <= 0:
            break


        for i in enemy_list:
            damage = i.strength
            victim = random.randint(0,(len(party_list)-1))
            if party_list[victim].defence > damage:
                print("Attack too weak, 0 damage!")
                print(party_list[victim].name + "still has " + str(party_list[victim].life) + "HEALTH points.")
            else:
                party_list[victim].life = party_list[victim].life - (damage - party_list[victim].defence)
                print(i.name + " attacked " + party_list[victim].name + " and did " + str(damage) + " points of damage!")
                print(party_list[victim].name + " now has " + str(party_list[victim].life) + " LIFE points remaining!")

                if party_list[victim].life <= 0:
                    party_list.pop(victim)
                    if len(enemy_list) <= 0 or len(party_list) <= 0:                        
                        break
                else:
                    print(party_list[victim].life)

        if len(enemy_list) <= 0 or len(party_list) <= 0:
            break
        else:
            print()

#------------------------------------------------------------------------------------------------------------------------------------------
            
create_party()
create_enemy()
battle()

print("It ended!")




