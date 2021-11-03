import json

class Move:
    def __init__(self, name ,type, powerPoint, category):
        self.name = name
        self.type = type
        self.powerPoint = powerPoint
        self.category = category

    def toString(self):
        return str(self.name) + " " + str(self.type) + " " + str(self.powerPoint) + " " + str(self.category)
    #def jsonToMoves(self):
       # movesList = []

        #with open('json/moves.json') as moves:
         #   moveObj = json.loads(moves)
          #  movesList.append(Move(moveObj["ename"], moveObj["type"], moveObj["pp"], moveObj["category"]))

        #return movesList