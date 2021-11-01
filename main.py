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

def jsonToPokemons():
    pokemonsList = []
    #encoding utf8 for chinese and japanese characters
    with open('json/pokemons.json', encoding="utf8") as pokemons:
        # for moveObj in moves:
        # moveObj = moves.read()

        pokemonDict = json.load(pokemons)
        for i in pokemonDict:
            #['ename to only display ename']
            pokemonsList.append([i['name']['english'], i['type']])

    return pokemonsList

layoutMain = [[sg.Text("Welcome to the Pokelutor.\nPlease choose a pokemon \nand it's specification", size=(25,3))],
              [sg.Combo(jsonToPokemons(), key="pokemonCombo")], [sg.Button("Create")]]

layoutMove = [[sg.Text("test")], [sg.Combo(jsonToMoves(), key='moveCombo1', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo2', size=(25))],
              [sg.Combo(jsonToMoves(), key='moveCombo3', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo4', size=(25))], [sg.Button("Info")]]

# pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('Pokelutor', layoutMain)

event, values = window.read()

if(event == 'Create'):
    valuesPokemon = values['pokemonCombo']
    window.close()

    window = sg.Window(values['pokemonCombo'], layoutMove)

    event, values = window.read()



if (event == 'Info'):
    print(valuesPokemon[0] + ":")
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

    pokemon = Pokemon(valuesPokemon[0], 12, pokemonMoveList, 15, 20, 16, 21, valuesPokemon[1])

    print(pokemon.toString())

    window.close()
