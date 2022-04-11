class Team:
    def __init__(self, pokemons):
        self.pokemons = pokemons


    def toString(self):

        counter = 0
        for i in self.pokemons:
            if counter == 0:
                return "The team consists of: " + str(i.name)
            else:
                return str(i.name)