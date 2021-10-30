class Pokemon:
    def __init__(self, level, moves, attack, defense, spAttack, spDefense, type):
        self.level = level
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.spAttack = spAttack
        self.spDefense = spDefense
        self.type = type

    def toString(self):

        return self.level + " " + self.moves + " " + self.attack + " " + self.defense + " " + self.spAttack + " " + self.spDefense + " " + self.type