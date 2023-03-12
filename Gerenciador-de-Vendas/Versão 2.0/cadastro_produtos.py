import PySimpleGUI as psg
import sqlite3


def cadastrar_produto(nome, quantidade, categoria, descricao):

    try:
        con = sqlite3.connect('produtos.db')
        curso = con.cursor()
        curso.execute('''CREATE TABLE IF NOT EXISTS Produtos
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Produto TEXT NOT NULL,
                            Quantidade INTEGER NOT NULL,
                            Categoria TEXT NOT NULL,
                            Descrição TEXT NOT NULL)''')

        curso.execute('''INSERT INTO Produtos
                        (Produto, Quantidade, Categoria, Descricao)
                            VALUES (?, ?, ?, ?)''', (nome, quantidade, categoria, descricao))
        con.commit()
        con.close()
    except:
        psg.popup('Aconteceu um erro :(', background_color='white', text_color='black',
                    button_color=('black', 'white'))
    else:
        if not nome:
            psg.popup('Insira o nome do produto', background_color='white', text_color='black',
                    button_color=('black', 'white'))
        elif not quantidade:
            psg.popup('Insira quantidade', background_color='white', text_color='black',
                    button_color=('black', 'white'))
        elif not quantidade.isnumeric():
            psg.popup('Apenas números inteiros', background_color='white', text_color='black',
                    button_color=('black', 'white'))
        elif not categoria:
            psg.popup('Insira a categoria', background_color='white', text_color='black',
                    button_color=('black', 'white'))
        elif not descricao:
            psg.popup('Insira a descrição', background_color='white', text_color='black',
                    button_color=('black', 'white'))
        else:
            psg.popup('Produto Cadastrado', background_color='white', text_color='black',
                        button_color=('black', 'white'))


class Produtos:

    def __init__(self):
        azul = '#4A3CAE'
        roxo = '#550681'
        amarelo = '#C1C100'
        laranja = '#C19800'

        title = [psg.Text('Sistema de Vendas', font=('Helvetica 30 bold'), size=70,
                        text_color='white', background_color=azul, pad=(0, 0), justification='c')]

        title_cadatro = [psg.Text('Cadastrar Produtos', font=('Any 20 bold'), size=40, pad=(0, 0),
                                background_color='white',
                                text_color='gray', justification='c')]

        left_column = [
            title_cadatro,
            [psg.Text('Nome do Produto: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5), key='produto')],
            [psg.Text('Quantidade: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5), key='quantidade')],
            [psg.Text('Categoria: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5), key='categoria')],
            [psg.Text('Descrição: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5), key='descricao')],
            [psg.Button('Cadastrar', pad=(50, 30)),
                psg.Button('Limpar Campos', pad=(30, 30)),
                psg.Button('Escolher Foto', pad=(30, 30))]
        ]

        layout = [
            title,
            [psg.HSeparator()],
            [psg.Column(left_column, justification='center', background_color='white')],
        ]

        window = psg.Window('Cadastrar Produtos', layout, use_custom_titlebar=True, background_color='white',
                            font='Helvetica 14 italic', finalize=True, resizable=True,
                            location=(300, 100), grab_anywhere=True, button_color=('black', 'white'),
                            size=(800, 550), )

        while True:

            event, value = window.read()
            if event == psg.WINDOW_CLOSED:
                break

            elif event == 'Cadastrar':
                nome = value['produto']
                quantidade = value['quantidade']
                categoria = value['categoria']
                descricao = value['descricao']

                cadastrar_produto(nome, quantidade, categoria, descricao)

            elif event == 'Limpar Campos':
                window.Element('produto').update('')
                window.Element('quantidade').update('')
                window.Element('categoria').update('')
                window.Element('descricao').update('')
                window['produto'].set_focus()

        window.close()


Produtos()
