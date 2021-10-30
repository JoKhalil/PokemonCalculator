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
            #['ename to only display ename']
            movesList.append([i['ename'], i['type'], i['pp'], i['category']])

    return movesList


layout = [[sg.Text("test")], [sg.Combo(jsonToMoves(), key='moveCombo1')], [sg.Combo(jsonToMoves(), key='moveCombo2')]
        , [sg.Combo(jsonToMoves(), key='moveCombo3')], [sg.Combo(jsonToMoves(), key='moveCombo4')], [sg.Button("Info")]]

# pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('Pokelutor', layout)

event, values = window.read()

if (event == 'Info'):
    #key is to call a specific component directly
    print(values['moveCombo1'])
    print(values['moveCombo2'])
    print(values['moveCombo3'])
    print(values['moveCombo4'])

window.close()
