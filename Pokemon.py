class Pokemon:
    def __init__(self, name, level, moves, attack, defense, spAttack, spDefense, type):
        self.name = name
        self.level = level
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.spAttack = spAttack
        self.spDefense = spDefense
        self.type = type

    def toString(self):

        return str(self.type) + " " + str(self.name) + " " + str(self.level) + " " + str(self.moves) + " Attack: " + str(self.attack) + " Defense: " \
               + str(self.defense) + " Special Attack: " + str(self.spAttack) + " Special Defense: " + str(self.spDefense) \
