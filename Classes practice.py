#Github copy
import random

Floor = 0
class Item:
    name = ""
    catogory = ""
    effect = 0
    hold_space = ""

    
class Party:
    name = ""
    level = 3
    life = 10
    strength = 10
    defence = 10
    experience = 10
    level = int(experience/10)
    inventory = {}
    life_bonus = 200
    stregth_bonus = 200
    defence_bonus = 200


            
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
    enemy_list = []
    level = abs(Floor + random.randint(-2,2))
    if level == 0:
        level = level + 1
    else:
        level = level
    for i in range(0,level):
        enemy_list.append(0)
        enemy_list[i] = Enemy()
    
create_party()       
create_enemy()


        

def ally_battle():
    while len(party_list) > 0 and len(enemy_list) > 0:
        for i in party_list:
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
                    enemy_list[i].name = str(i)
                    print ("Grunt number " + enemy_list[i].name)
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
                    else:
                        print(enemy_list[victim.life])
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
                else:
                    print(party_list[victim.life])





ally_battle()


