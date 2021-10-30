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
            movesList.append([i['ename'], i['type'], i['power'], i['category']])

    return movesList


layoutMove = [[sg.Text("test")], [sg.Combo(jsonToMoves(), key='moveCombo1', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo2', size=(25))],
              [sg.Combo(jsonToMoves(), key='moveCombo3', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo4', size=(25))], [sg.Button("Info")]]

layoutMain = [[sg.Text("Welcome to the Pokelutor. Please choose a pokemon and it's specification")],
              [sg.Combo(["Bulbasaur", "Squirtle", "Charmander"], key="pokemonCombo")],[sg.Button("Create")]]#if pokemon.json is added dont forget to remove the brackets when calling the function

# pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('Pokelutor', layoutMain)

event, values = window.read()

if(event == 'Create'):
    valuesPokemon = values['pokemonCombo']
    window.close()

    window = sg.Window(values['pokemonCombo'], layoutMove)

    event, values = window.read()



if (event == 'Info'):
    print(valuesPokemon + ":")
    #key is to call a specific component directly
    print(values['moveCombo1'][0])
    print(values['moveCombo2'][0])
    print(values['moveCombo3'][0])
    print(values['moveCombo4'][0])

    pokemonMoveList = []

    pokemonMoveList.append(values['moveCombo1'][0])
    pokemonMoveList.append(values['moveCombo2'][0])
    pokemonMoveList.append(values['moveCombo3'][0])
    pokemonMoveList.append(values['moveCombo4'][0])

    pokemon = Pokemon(12, pokemonMoveList, 15, 20, 16, 21, "Fire")

    print(pokemon.toString())

wind2222eee                             ow.close()
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee//eeeeeeeeeeeeeeeeeeeeee/E??eee                 e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ee