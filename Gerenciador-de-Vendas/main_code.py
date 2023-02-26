from functions import *


class Start:
    def __init__(self):
        layout = [
            [gui.Button('Escuro')],
            [gui.Button('Cadastrar Produto'), gui.Button('Cadastrar Venda')]
        ]

        self.window = gui.Window('Tela Inicial', layout)

        while True:
            event, value = self.window.read()
            if event == gui.WINDOW_CLOSED:
                break
            elif event == 'Cadastrar Venda':
                CadastrarVenda()
            elif event == 'Cadastrar Produto':
                CadastrarProduto()
            elif event == 'Escuro':
                gui.theme('DarkBlack1')
                self.window.close()
                Start()
        self.window.close()


Start()
