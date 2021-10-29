import PySimpleGUI as sg

from Pokemon import Pokemon

layout = [[sg.Text("test")],[sg.Input()], [sg.Input()], [sg.Input()], [sg.Input()], [sg.Button("Info")], [sg.Listbox()]]

pokemon = Pokemon(1, [layout.__getitem__(1), layout.__getitem__(2), layout.__getitem__(3), layout.__getitem__(4)], 1, 1, 1, 1, "Fire")

window = sg.Window('testTitle', layout)

event, values = window.read()

if(event == 'Info'):
    for move in pokemon.moves:
        print(move.name)


window.close()