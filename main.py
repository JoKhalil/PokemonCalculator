import PySimpleGUI as sg
import json
from Move import Move
from Pokemon import Pokemon


def jsonToMoves():
    movesList = []

    with open('json/moves.json') as moves:
        # for moveObj in moves:
        # moveObj = moves.read()
        moveDict = json.load(moves)
        for i in moveDict:
            movesList.append(i)

    return movesList


layout = [[sg.Text("test")], [sg.Combo(jsonToMoves(), key='moveCombo')], [sg.Button("Info")]]

# pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('Pokelutor', layout)

event, values = window.read()

if (event == 'Info'):
    #key is to call a specific component directly
    print(values['moveCombo']['ename'])

window.close()
