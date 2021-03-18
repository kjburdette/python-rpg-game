class Characters:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack


class Hero(Characters):
    def coinTransaction(self, coinPurse):
        self.coinPurse = coinPurse


# Heros
heroHuman = Hero("Human", 100, 50, 25)
heroOrc = Hero("Orc", 100, 25, 75)
heroElf = Hero("Elf", 100, 75, 25)

# Villans
villanMinion = Characters("Minion", 100, 20, 20)
villanBoss = Characters("Boss", 100, 75, 75)

print(heroHuman.name)
print(villanBoss.name)
