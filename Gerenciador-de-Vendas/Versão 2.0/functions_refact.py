import sqlite3
import PySimpleGUI as psg
from visualizar_vendas import Apps


def load():
    con = sqlite3.connect('produtos.db')
    curso = con.cursor()
    curso.execute('PRAGMA table_info(Produtos);')
    lista = [titulo[1] for titulo in curso.fetchall()]
    con.close()
    return lista


def elementos():
    con = sqlite3.connect('produtos.db')
    curso = con.cursor()
    curso.execute('''SELECT ID, Produto, Descrição, Quantidade, Tamanho
                    FROM Produtos''')
    lista = [dados for dados in curso.fetchall()]
    con.close()
    conteudo = []

    for item in lista:
        valores = (item[0], item[1], item[2], item[3])
        conteudo.append(valores)

    return conteudo


class App:

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
            [psg.InputText(size=55, pad=(20, 5))],
            [psg.Text('Quantidade: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5))],
            [psg.Text('Categoria: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5))],
            [psg.Text('Descrição: *', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=55, pad=(20, 5))],
            [psg.Button('Cadastrar', pad=(30, 30)),
                psg.Button('Limpar Campos', pad=(30, 30))],
        ]

        right_column = [
            [psg.Text('Opcional', font='Helvetica 20 italic', background_color='white', text_color='black')],
            [psg.Text('Nome do Cliente:', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=60, pad=(20, 5))],
            [psg.Text('Nome do Vendedor:', background_color='white', text_color='black', pad=(30, 5))],
            [psg.InputText(size=60, pad=(20, 5))],
            [psg.Text('Esolher Foto:', background_color='white', text_color='black', pad=(30, 5))],
            [psg.FileBrowse('Selecionar', pad=(15, 5), button_color=('black', 'white'))],
        ]

        output = [
                [psg.Table(values=elementos(), headings=load(), max_col_width=20,
                        justification='center', pad=(10, 10), expand_x=True,
                        background_color='white', text_color='black')]
                    ]

        layout = [
            title,
            [psg.HSeparator()],
            [psg.Column(left_column, justification='left', background_color='white'), psg.VerticalSeparator(),
                psg.Column(right_column, justification='right', background_color='white')],
            [psg.HSeparator()],
            [output]
        ]

        window = psg.Window('oi', layout, use_custom_titlebar=True, background_color='white',
                            font='Helvetica 14 italic', finalize=True, resizable=True,
                            location=(0, 0), grab_anywhere=True, button_color=('black', 'white'),
                            size=(1370, 700))

        while True:
            event, value = window.read()
            if event == psg.WINDOW_CLOSED:
                break
            elif event == 'Visualizar Vendas':
                Apps()
        window.close()


App()
