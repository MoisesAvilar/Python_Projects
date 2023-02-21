from functions import *

layout = [
    [gui.Menu(menu())],
    [gui.Button('Cadastrar Produto'), gui.Button('Cadastrar Venda')]
]

window = gui.Window('Tele Inicial', layout)

while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    elif event == 'Cadastrar Venda':
        cadastrar_venda()
    elif event == 'Cadastrar Produto':
        cadastrar_produto()
    window.close()
