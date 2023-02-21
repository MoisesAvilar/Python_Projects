import PySimpleGUI as gui
import datetime
import sqlite3


def menu():
    return [
        ['Arquivo', 'Nada'],
        ['Ajuda', ['Sobre']]]


def atualizar_estoque(produto, window):
    con = sqlite3.connect('produtos.db')
    cursor = con.cursor()
    cursor.execute('SELECT Quantidade FROM Produtos WHERE Produto = ?', (produto,))
    result = cursor.fetchone()
    if result:
        disponivel = result[0]
        window['disponivel'].update(f'Em estoque: {disponivel}')
    con.close()


def carregar_dados():
    con = sqlite3.connect('produtos.db')
    cursor = con.cursor()
    cursor.execute('''SELECT Produto, Descrição, Quantidade, Tamanho from Produtos''')
    dados = cursor.fetchall()
    return dados


def cadastrar_venda():
    dados = carregar_dados()
    nome = [tupla[0] for tupla in dados]
    descricao = [tupla[1] for tupla in dados]
    volume = [tupla[2] for tupla in dados]
    referencia = [tupla[3] for tupla in dados]

    layout = [
        [gui.Text()],
        [gui.Text('Nome do produto', font=20, size=18),
         gui.Combo(nome, size=20, key='nome', enable_events=True, readonly=True)],
        [gui.Text('Quantidade', size=20), gui.Input(size=5, key='quantidade'),
         gui.Text(key='disponivel')],
        [gui.Text('Código/Referência', size=20), gui.Text(size=20, key='codigo')],
        [gui.Text('Descrição', size=20), gui.Text(size=20, key='descricao')],
        [gui.Text('Valor R$', size=20), gui.Input(size=20, key='valor')],
        [gui.Text()],
        [gui.Text('*Opcional')],
        [gui.Text('Nome do cliente', size=20), gui.Input(size=20, key='cliente')],
        [gui.Text('Nome do vendedor', size=20), gui.Input(size=20, key='vendedor')],
        [gui.Text()],
        [gui.Text(size=10), gui.Button('Registrar', size=20), gui.Text(size=10)]
    ]

    window = gui.Window('Sistema de Registro de Vendas', layout)

    while True:
        events, values = window.read()
        if events == gui.WINDOW_CLOSED:
            break
        elif events == 'nome':
            produto_selecionado = values['nome']
            index = nome.index(produto_selecionado)
            window['descricao'].update(descricao[index])
            window['disponivel'].update(f'Em estoque: {volume[index]}')
            window['codigo'].update(referencia[index])
            atualizar_estoque(produto_selecionado, window)
        elif not values['nome']:
            gui.popup('Preencha os campos obrigatórios')
            continue
        elif not values['quantidade'].isnumeric():
            gui.popup('Apenas números inteiros', no_titlebar=True)
            continue
        elif not values['valor'].replace('.', '', 1).isnumeric():
            gui.popup('Digite o preço correto')
            continue
        elif events == 'Registrar':
            con = sqlite3.connect('vendas.db')
            con.execute('''CREATE TABLE IF NOT EXISTS Vendas
                            (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Produto TEXT NOT NULL,
                            Descrição TEXT NOT NULL,
                            Código TEXT NOT NULL,
                            Quantidade INTEGER NOT NULL,
                            Preço REAL NOT NULL,
                            Vendedor TEXT,
                            Cliente TEXT,
                            Total REAL NOT NULL,
                            Data TEXT NOT NULL)''')

            produto = values['nome']
            detalhes = window['descricao'].get().encode('utf-8')
            codigo = window['codigo'].get().encode('utf-8')
            quantidade = int(values['quantidade'])
            preco = float(values['valor'])
            vendedor = values['vendedor'].title()
            cliente = values['cliente'].title()
            total = preco * quantidade
            data = datetime.date.today()

            con.execute('''INSERT INTO Vendas 
                        (Produto, Descrição, Código, Quantidade, Preço, Vendedor, Cliente, Total, Data) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (produto, detalhes, codigo, quantidade, preco, vendedor, cliente, total, data))
            con.commit()
            con.close()
            gui.popup('Venda registrada com sucesso!')
            con_produtos = sqlite3.connect('produtos.db')
            cursor_produtos = con_produtos.cursor()
            cursor_produtos.execute('''SELECT Quantidade FROM Produtos WHERE Produto = ?''', (produto,))
            valor = cursor_produtos.fetchone()
            deposito = valor[0]
            restante = deposito - quantidade
            cursor_produtos.execute('''UPDATE Produtos SET Quantidade = ? WHERE Produto = ?''', (restante, produto,))
            con_produtos.commit()
            con_produtos.close()
            window.Element('nome').update('')
            window.Element('descricao').update('')
            window.Element('codigo').update('')
            window.Element('quantidade').update('')
            window.Element('disponivel').update('')
            window.Element('valor').update('')
            window.Element('vendedor').update('')
            window.Element('cliente').update('')
    window.close()


def cadastrar_produto():
    con = sqlite3.connect('produtos.db')
    layout = [
        [gui.Text('Nome do Produto', size=20), gui.Input(key='nome', size=20)],
        [gui.Text('Descrição do Produto', size=20), gui.Input(key='descricao', size=20)],
        [gui.Text('Quantidade', size=20), gui.Input(key='quantidade', size=20)],
        [gui.Text('Tamanho', size=20), gui.Input(key='tamanho', size=20)],
        [gui.Text(size=10), gui.Button('Confirmar', size=20), gui.Text(size=10)],
    ]

    window = gui.Window('Cadastrar Produtos', layout)

    con.execute('''CREATE TABLE IF NOT EXISTS Produtos
                (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                Produto TEXT NOT NULL, 
                Descrição TEXT NOT NULL, 
                Quantidade INTEGER NOT NULL, 
                Tamanho TEXT NOT NULL)''')
    while True:
        try:
            event, value = window.read()
        except:
            cadastrar_venda()
            break
        if event == gui.WINDOW_CLOSED or event == gui.WIN_X_EVENT:
            cadastrar_venda()
            break
        elif not all(value.values()):
            gui.popup('Preencha todos os campos')
            continue
        elif not value['quantidade'].isnumeric():
            gui.popup('Apenas números inteiros')
            continue
        elif event == 'Confirmar':
            nome = value['nome'].strip().title()
            descricao = value['descricao'].strip().title()
            quantidade = value['quantidade'].strip()
            tamanho = value['tamanho'].strip()
            con.execute('''INSERT INTO Produtos (Produto, Descrição, Quantidade, Tamanho)
                            VALUES (?, ?, ?, ?)''', (nome, descricao, quantidade, tamanho))
            con.commit()
            window.Element('nome').update('')
            window.Element('descricao').update('')
            window.Element('quantidade').update('')
            window.Element('tamanho').update('')
            window['nome'].set_focus()
            gui.popup('Produto cadastrado com sucesso!')

    con.close()
    window.close()









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
