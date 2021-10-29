import PySimpleGUI as sg
import json
from Move import Move
from Pokemon import Pokemon

def jsonToMoves():
    movesList = []

    ##with open('json/moves.json') as moves:
      ##  moveObj = json.dumps(str(moves))
        ##movesList.append(Move(moveObj.index("e"), moveObj.index("t"), moveObj.index("p"), moveObj.index("c")))
    for moves in open('json/moves.json'):
        moveObj = json.dumps(str(moves))
        movesList.append(Move(moveObj.index("e"), moveObj.index("t"), moveObj.index("p"), moveObj.index("c")))
    return movesList



layout = [[sg.Text("test")], [sg.DropDown([str(jsonToMoves()[0])])], [sg.Button("Info")]]

#pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('testTitle', layout)

event, values = window.read()

if(event == 'Info'):
    print(str(jsonToMoves()[0]))


window.close()