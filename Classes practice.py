import random

Floor = 0
class Item:
    name = ""
    


class Party:
    name = ""
    level = 1
    life = level*4
    base_strength = level*3
    base_defence = level*2
    experience = 0
    level = int(experience/10)
            
    def bonuses():
        print()


class Enemy:
    level = abs(Floor + random.randint(-2,2))
    name = ""
    life = level*3
    strength = level*3
    defence = level*2

    

    def attack(self):
        victim = random.randint(1,4)
        
    def defend(self):
        print("Ouch!")
        self.life = self.life - 1
    def checklife(self):
        if self.life <= 0:
            print(Name + " is dead")
        else:
            print(str(self.life)+" life left")
ally1 = Party()
ally2 = Party()
ally3 = Party()
ally4 = Party()

party_list = [ally1,ally2,ally3,ally4]


def create_party():
    print("You have 4 party members ")
    for members in party_list:
        members.name = input("Name of ally: ")

create_party()    
print(party_list[1].name
      )    

enemy1 = Enemy()
enemy2 = Enemy()
    

fight = input("""You are against two enemys.
What would you like to do?
    Fight
    Run(15%)""")
fight = fight.upper()
if fight == "F" or fight == "FIGHT":
    battle()
elif fight == "R" or fight == "RUN":
    RNG = random.randint(0,100)
    if RNG > 15:
        print("You escaped successfully!")
    else:
        print("You couldn't escape!")
        

def battle():
    while party_members > 0 and enemy_numbers > 0:
        action = input("""What will you do?
    Attack
    Defend
    Item
    Run(15%)
    """)
        



    
