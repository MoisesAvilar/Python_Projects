import PySimpleGUI as Gui
from pass_generator_gui import main_function

# interface Gráfica
interface = [
    [Gui.Text('Selecione as opções desejadas', font=16)],  # Nome do aplicativo
    [Gui.Text('Tipo de senha', font=16, size=15),
     Gui.Combo(['De A à Z', 'Numérico', 'Alfanumérico'], font=16, size=15, key='tipo', default_value='De A à Z')],
    [Gui.Text('Tamanho da senha', font=16, size=15), Gui.Combo(list(range(1, 31)), font=16, key='size', default_value=12)],
    [Gui.Button('Gerar Senha', font=16, size=(25, 2)), Gui.Button('Sair', font=16, size=(8, 2))],
    [Gui.Input(size=45, key='campo', justification='c')]
]

janela = Gui.Window('Password Generator', interface)

while True:
    evento, valores = janela.read()
    if evento == Gui.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Gerar Senha':
        valores['size'] = int(valores['size'])
        print('o')
        if valores['tipo'] == 'De A à Z':
            generator = main_function(1, valores['size'])
            janela['campo'].update(f'{generator}')
            print(generator)
        elif valores['tipo'] == 'Numérico':
            generator = main_function(2, valores['size'])
            janela['campo'].update(f'{generator}')
            print(generator)
        elif valores['tipo'] == 'Alfanumérico':
            generator = main_function(3, valores['size'])
            janela['campo'].update(f'{generator}')
            print(generator)

janela.close()
