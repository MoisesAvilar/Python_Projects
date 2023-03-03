import PySimpleGUI as psg
import sqlite3


def load():
    con = sqlite3.connect('vendas.db')
    curso = con.cursor()
    curso.execute('PRAGMA table_info(Vendas);')
    lista = [titulo[1] for titulo in curso.fetchall()]
    con.close()
    return lista


def elementos():
    con = sqlite3.connect('vendas.db')
    curso = con.cursor()
    curso.execute('''SELECT ID, Produto, Descrição, Código, Quantidade, Preço, Vendedor, Cliente, Total, Data
                    FROM Vendas''')
    lista = [dados for dados in curso.fetchall()]
    con.close()
    conteudo = []

    for item in lista:
        valores = (item[0], item[1], item[2].decode(), item[3].decode(),
                item[4], item[5], item[6], item[7], item[8], item[9])
        conteudo.append(valores)

    return conteudo


class Apps:
    def __init__(self):
        title_bar = [
            [psg.Text('Vendas Cadastradas', font='Any 20')],
        ]

        output = [
            [psg.Frame('',
                layout=[
                    [psg.Table(values=elementos(), headings=load(), max_col_width=25, auto_size_columns=True,
                            justification='left', pad=(10, 30), background_color='white',
                            text_color='black', expand_x=True)]
                ], background_color='white')]
        ]

        layout = [
            [title_bar, output]
        ]
        self.window = psg.Window('Sistema de Cadastro', element_justification='c', location=(100, 100), background_color='white').layout(layout)

        while True:
            eventos, valores = self.window.read()

            if eventos == psg.WINDOW_CLOSED:
                break
        self.window.close()
