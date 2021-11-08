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

def jsonToWeathers():
    weathersList = []

    with open('json/weathers.json') as weathers:

        weatherDict = json.load(weathers)
        for i in weatherDict:
            weathersList.append(i['weather'])
    
    return weathersList

layoutMain = [[sg.Text("Welcome to the Pokelutor.\nPlease choose a pokemon \nand it's specification", size=(25, 3))],
              [sg.Combo(jsonToPokemons(), key="pokemonCombo", size=(25))], [sg.Text("Level")], [sg.InputText(key='level', size=(5, 3))],
              [sg.Text("Attack")], [sg.InputText(key='attack', size=(5, 3))], [sg.Text("Defense")], [sg.InputText(key='defense', size=(5, 3))],
              [sg.Text("Sp Attack")], [sg.InputText(key='spAttack', size=(5, 3))], [sg.Text("Sp Defense")],
              [sg.InputText(key='spDefense', size=(5, 3))], [sg.Button("Create")]]

layoutMove = [[sg.Text("test")], [sg.Combo(jsonToMoves(), key='moveCombo1', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo2', size=(25))],
              [sg.Combo(jsonToMoves(), key='moveCombo3', size=(25))], [sg.Combo(jsonToMoves(), key='moveCombo4', size=(25))], [sg.Button("Info")]]

#layoutInfo = [[sg.Text(key="pokemonInfo")]]
# pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('Pokelutor', layoutMain)

event, values = window.read()

if(event == 'Create'):
    valuesPokemon = values['pokemonCombo']
    level = values['level']
    statAttack = values['attack']
    statDefense = values['defense']
    statSpAttack = values['spAttack']
    statSpDefense = values['spDefense']


    window.close()

    window = sg.Window(values['pokemonCombo'], layoutMove)

    event, values = window.read()



if (event == 'Info'):
    # print(valuesPokemon[0] + ":")
    # key is to call a specific component directly
    # print(values['moveCombo1'][0])
    # print(values['moveCombo2'][0])
    # print(values['moveCombo3'][0])
    # print(values['moveCombo4'][0])

    pokemonMoveList = []
    firstMove = Move(values['moveCombo1'][0], values['moveCombo1'][1], values['moveCombo1'][2], values['moveCombo1'][3])
    secondMove = Move(values['moveCombo2'][0], values['moveCombo2'][1], values['moveCombo2'][2], values['moveCombo2'][3])
    thirdMove = Move(values['moveCombo3'][0], values['moveCombo3'][1], values['moveCombo3'][2], values['moveCombo3'][3])
    fourthMove = Move(values['moveCombo4'][0], values['moveCombo4'][1], values['moveCombo4'][2], values['moveCombo4'][3])

    pokemonMoveList.append(firstMove.name)
    pokemonMoveList.append(secondMove.name)
    pokemonMoveList.append(thirdMove.name)
    pokemonMoveList.append(fourthMove.name)

    pokemon = Pokemon(valuesPokemon[0], level, pokemonMoveList, statAttack, statDefense, statSpAttack, statSpDefense, valuesPokemon[1])

    # window = sg.Window("Info", layoutInfo)
    #
    # values['pokemonInfo'] = pokemon.toString()
    #
    # event, values = window.read()

    print(pokemon.toString())

    window.close()
