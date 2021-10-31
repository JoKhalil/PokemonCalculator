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

        return str(self.name) + " " + str(self.level) + " " + str(self.moves) + " " + str(self.attack) + " " \
               + str(self.defense) + " " + str(self.spAttack) + " " + str(self.spDefense) + " " + str(self.type)