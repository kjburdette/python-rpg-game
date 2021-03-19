class Hero:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.characterClass = "Hero"
    
# class Hero(Characters):
#     pass
    # def coinTransaction(self, coinPurse, coin):
    #     self.coinPurse = coinPurse
    #     self.coin = coin
    #     coinPurse += coin
    #     print(f"{coin} coin's have been added to your coin purse")
#^^^ needs revision ^^^

# Heros

# Villans
# villainMinion = Characters("Minion", 100, 20, 20)
# villainBoss = Characters("Boss", 100, 75, 75)

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
        if ( choice == "h"):
            character = Hero("Human", 100, 50, 25)
        elif ( choice == "o"):
            character = Hero("Orc", 100, 25, 75)  
        elif ( choice == "e"):
            character = Hero("Elf", 100, 25, 50)
        else:
            print("Please follow my rules and enter a valid choice.")
    return character



character = selectChar()
print(f"""
        Your class is: {character.name} \n
        Health: {character.hp} \n
        Defense: {character.defense} \n
        Attack: {character.attack} \n
    """)

# print(character.name)

