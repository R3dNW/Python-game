#Github copy
import random

Floor = 0
class Item:
    name = ""
    description = ""
    effect_type = ""
    boost_type = ""
    potency = 0


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
    stregth_bonus = 0
    defence_bonus = 0
    passive_inventory = []
    active_inventory = []

    def bonus(self):
        for i in self.passive_inventory:
            if i.effect == "P":
                if i.type == "Health":
                    self.life_bonus = i.potencey
                elif i.type == "Defence":
                    self.defence_bonus = i.potencey
                elif i.type == "Strength":
                    self.strength_bonus = i.potencey
                else:
                    life_bonus = 0
                    stregth_bonus = 0
                    defence_bonus = 0
    def item(self):
        counter = 0

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

            for i in range(0,len(items)):


                if i == counter:
                    print("--" + items[i].name)
                    a = items[i].description
                    print(a)

                else:
                    print(items[i].name)
                print()

        print("You selected: " + items[counter].name)
        print("            " + items[counter].description)

        if items[counter].boost_type == "Health":
            self.life_bonus = self.life_bonus + items[counter].potency
        elif items[counter].boost_type == "Defence":
            self.defence_bonus = self.defence_bonus + items[counter].potency
        elif items[counter].boost_type == "Strength":
            self.strength_bonus = self.strength_bonus + items[counter].potency


    def stats(self):
        self.life = (self.level*4) + self.life_bonus
        self.strength = (self.level*4) + self.stregth_bonus
        self.defence = (self.level*2) + self.defence_bonus


class Enemy:
    level = abs(Floor + random.randint(-2,2))+1
    name = ""
    life = level*3
    strength = level*3
    defence = level*2



    def attack(self):
        victim = random.randint(0,partylist.len())

    def defend(self,i):
        print("Ouch!")
        self.life = self.life

    def checklife(self):
        if self.life <= 0:
            print(Name + " is dead")
        else:
            print(str(self.life)+" life left")

def clear():
    print("\n"*50)

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

def create_enemy():
    global enemy_list
    global names_list
    enemy_list = []
    level = abs(Floor + random.randint(-2,2))
    if level == 0:
        level = level + 1
    else:
        level = level
    for i in range(0,level):
        enemy_list.append(0)
        enemy_list[i] = Enemy()
        names_list = ["Jerry","Bob","Karl","Carl","Lebron","James","Steve","Joe","Jack","John","Amy","Sarah","Anne","Micheal","Ian",]

create_party()
create_enemy()




def battle():
    while len(party_list) > 0 and len(enemy_list) > 0:
        for i in party_list:
            i.stats()
            action = input("""What will you do?
        Attack
        Defend
        Item
        Run(15%)
        """)
            action = action.upper()
            if action == "A" or action == "ATTACK":
                i.stats()
                damage = i.strength
                for i in range(0,len(enemy_list)):
                    enemy_list[i].name = names_list[i]
                    print (enemy_list[i].name + "[" + str(i) + "]" )
                    print ("Life: " + str(enemy_list[i].life))
                victim = int(input("Who do you want to attack? "))

                print(enemy_list[victim].life)
                print("defence = " + str(enemy_list[victim].defence) + "and attack power = " + str(damage))
                if enemy_list[victim].defence > int(damage):
                    print("Attack too weak, 0 damage!")
                    print(enemy_list[victim].life)
                else:
                    enemy_list[victim].life = enemy_list[victim].life - (damage - enemy_list[victim].defence)
                    print(enemy_list[victim].life)
                    if enemy_list[victim].life <= 0:
                        enemy_list.pop(victim)
                        print(len(enemy_list))
                        if len(enemy_list) <= 0 or len(party_list) <= 0:
                            break
                    else:
                        print(enemy_list[victim.life])

            elif action == "D" or action == "DEFENCE":
                i.defence = i.defence*2

            elif action == "I" or action == "ITEM":
                print(i.life)
                i.item()
                i.stats()
                print(i.life)

        if len(enemy_list) <= 0 or len(party_list) <= 0:
            break


        for i in enemy_list:
            damage = i.strength
            victim = random.randint(0,len(party_list))
            print(party_list[victim].name)
            print(party_list[victim].life)
            if party_list[victim].defence > damage:
                print("Attack too weak, 0 damage!")
                print(party_list[victim].life)
            else:
                party_list[victim].life = party_list[victim].life - (damage - party_list[victim].defence)
                print(party_list[victim].life)
                if party_list[victim] <= 0:
                    party_list.pop(victim)
                    if len(enemy_list) <= 0 or len(enemy_list):
                        break
                else:
                    print(party_list[victim.life])

        if len(enemy_list) <= 0 or len(enemy_list):
            break
        else:
            print()

            



battle()

print("It ended!")


