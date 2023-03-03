import PySimpleGUI as psg


class App:
    def __init__(self):
        psg.theme('Material2')
        title = [
            [psg.Text('Sistema de Cadastro de Produtos', font=30)]
        ]
        col1 = [
            [psg.Text('Nome do Produto:', pad=(10, 10), font=20, size=20)],
            [psg.Text('Preço:', pad=(10, 10), font=20)],
            [psg.Text('Quantidade:', pad=(10, 10), font=20)],
            [psg.Text('Categoria:', pad=(10, 10), font=20)],
            [psg.Text('Descrição:', pad=(10, 10), font=20)],
        ]

        col2 = [
            [psg.Input(size=15, pad=(10, 10), font=20)],
            [psg.Input(size=15, pad=(10, 10), font=20)],
            [psg.Input(size=15, pad=(10, 10), font=20)],
            [psg.Input(size=15, pad=(10, 10), font=20)],
            [psg.Input(size=15, pad=(10, 10), font=20)],

        ]

        layout = [
            [psg.Column(title, justification='c')],
            [psg.Frame('Produtos', background_color='white', title_color='black',
                    layout=[
                        [psg.Column(col1), psg.Column(col2)],
                        [psg.Column([[psg.Submit('Cadastrar', font=30, pad=(50, 10))]], justification='c')]
                    ])],
        ]

        self.window = psg.Window('Sistema de Cadastro', element_justification='c', background_color='white').layout(layout)

        while True:
            eventos, valores = self.window.read()

            if eventos == psg.WINDOW_CLOSED:
                break
        self.window.close()


App()
