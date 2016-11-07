import random

Floor = 0


class Item:
    name = ""


class Ally:
    name = ""
    level = 1
    life = level * 4
    base_strength = level * 3
    base_defence = level * 2
    experience = 0
    level = int(experience / 10)

    def bonuses(self):
        print()


class Enemy:
    level = abs(Floor + random.randint(-2, 2))
    name = ""
    life = level * 3
    strength = level * 3
    defence = level * 2

    def attack(self):
        victim = random.randint(1, 4)

    def defend(self):
        print("Ouch!")
        self.life = self.life - 1

    def check_life(self):
        if self.life <= 0:
            print(self.name + " is dead")
        else:
            print(str(self.life) + " life left")


def battle():
    while party_members > 0 and enemy_numbers > 0:
        action = input("""What will you do?
    Attack
    Defend
    Item
    Run(15%)
    """)


ally1 = Ally()
ally2 = Ally()
ally3 = Ally()
ally4 = Ally()

party = [ally1, ally2, ally3, ally4]


def create_party():
    print("You have 4 party members ")
    for members in party:
        members.name = input("Name of ally: ")


create_party()
print(party[1].name
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
    RNG = random.randint(0, 100)
    if RNG > 15:
        print("You escaped successfully!")
    else:
        print("You couldn't escape!")