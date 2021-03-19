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
        h. Human
        o. Orc
        e. Elf
        """)
        if (choice == "h"):
            character = Hero("Human", 100, 50, 25)
        elif (choice == "o"):
            character = Hero("Orc", 100, 25, 75)
        elif (choice == "e"):
            character = Hero("Elf", 100, 25, 50)
        else:
            print("Please follow my rules and enter a valid choice.")

    return character


def characterAttacks(character, minion):
    print(f"{character.name} attacks {minion.name}")
    print(f"{minion.name} takes 5 damage")
    minion.takeDamage()
    print(f"{minion.name} gets wrecked.")
    print(f"{minion.name}'s remaining health is {minion.hp}")
    character.coinTransaction()


character = selectChar()
print(f"""
        Your class is: {character.name} \n
        Health: {character.hp} \n
        Defense: {character.defense} \n
        Attack: {character.attack} \n
    """)
characterAttacks(character, minion)

# combat
