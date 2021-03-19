class Characters:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        # self.characterClass = "Hero"


class Hero(Characters):
    # def __init__(self, coinPurse):
    coinPurse = 0
    # self.coin = coin

    def coinTransaction(self):
        self.coinPurse += 1
        print(
            f"""\nOne coin has been added to your coin purse you now have {character.coinPurse} coin.""")

    def takeDamage(self):
        self.hp -= 5


class Villain(Characters):
    def takeDamage(self):
        self.hp -= 5

# Heros


# Villans
minion = Villain("Minion", 100, 20, 20)
boss = Villain("Boss", 100, 75, 75)

# print(heroHuman.name)
# print(villanBoss.name)


def selectChar():
    # charName = input("What is your name?")
    character = ""
    while character == "":
        choice = input("""Please select a character
        1. Human
        2. Orc
        3. Elf
        """)
        if (choice == "1"):
            character = Hero("Human", 100, 50, 25)
        elif (choice == "2"):
            character = Hero("Orc", 100, 25, 75)
        elif (choice == "3:"):
            character = Hero("Elf", 100, 25, 50)
        else:
            print("Please follow my rules and enter a valid choice.")

    return character


# combat

def characterAttacks(character, minion):
    print(f"{character.name} attacks {minion.name}")
    print(f"{minion.name} takes 5 damage")
    minion.takeDamage()
    print(f"{minion.name} gets wrecked.")
    print(f"{minion.name}'s remaining health is {minion.hp}")
    character.coinTransaction()


def minionAttacks(minion, character):
    print(f"{minion.name} attacks {character.name}")
    print(f"{character.name} takes 5 damage")
    character.takeDamage()
    print(f"{character.name}'s remaining health is {character.hp}")


def bossAttacks(boss, character):
    print(f"{boss.name} attacks {character.name}")
    print(f"{boss.name} takes 5 damage")
    minion.takeDamage()
    # print(f"{boss.name} is unphased.")
    print(f"{boss.name}'s remaining health is {boss.hp}")


def mainMenu():
    selection = input("""
        What would you like to do next? Please select an option:
        1. Fight minion
        2. Fight boss
        3. Barracks
        4. Quit
    """)
    return selection


character = selectChar()
print(f"""
        Your class is: {character.name} \n
        Health: {character.hp} \n
        Defense: {character.defense} \n
        Attack: {character.attack} \n
    """)


adventureOption = ""
while adventureOption != "4":
    adventureOption = mainMenu()
    if (adventureOption == "1"):
        minionAttacks(character, minion)
    elif (adventureOption == "2"):
        bossAttacks(character, boss)
    elif (adventureOption == "3"):
        adventureOption = barracks()
    else:
        pass
