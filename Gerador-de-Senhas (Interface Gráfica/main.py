import PySimpleGUI as gui
from pass_generator_gui import main_function

interface = [
            [gui.Titlebar('Password Generator w/UI')],
            [gui.Text('Escolha o  tipo de senha:'), gui.Input(size=4, key='tipo')],
            [gui.Text('Escolha o tamanho da senha:'), gui.Input(size=4, key='tamanho')],
            [gui.Text('Cria sua senha'), gui.Button('Criar')],
            [gui.Input(key='campo')]
]

janela = gui.Window('Testando', interface)

while True:
    event, values = janela.read()
    if event == gui.WIN_CLOSED:
        break
    elif event == 'Criar':
        values['tipo'] = int(values['tipo'])
        values['tamanho'] = int(values['tamanho'])

        if values['tipo'] == 1:
            a = main_function(1, values['tamanho'])
            janela['campo'].update(f'{a}')
            print(main_function(1, values['tamanho']))

        elif values['tipo'] == 2:
            a = main_function(2, values['tamanho'])
            janela['campo'].update(f'{a}')
            print(main_function(2, values['tamanho']))

        elif values['tipo'] == 3:
            a = main_function(3, values['tamanho'])
            janela['campo'].update(f'{a}')

        elif values['tipo'] < 1 or values['tipo'] > 2:
            janela['campo'].update('O tipo de senha não está certo.')

janela.close()
