import PySimpleGUI as gui
import datetime
import sqlite3


def carregar_dados():
    con = sqlite3.connect('produtos.db')
    cursor = con.cursor()
    cursor.execute('''SELECT Produto, Descrição, Quantidade, Tamanho from Produtos''')
    dados = cursor.fetchall()
    nome = []
    descricao = []
    quantidade = []
    tamanho = []

    for item in dados:
        nome.append(item[0])
        descricao.append(item[1])
        quantidade.append(item[2])
        tamanho.append(item[3])
    con.close()
    return nome, descricao, quantidade, tamanho

def cadastrar_venda():
    dados = carregar_dados()

    layout = [
        [gui.Text()],
        [gui.Text('Nome do produto', font=20, size=18), gui.Combo(dados[0], size=20, key='nome', enable_events=True, readonly=True)],
        [gui.Text('Quantidade', size=20), gui.Input(size=5, key='quantidade'), gui.Text(key='disponivel')],
        [gui.Text()],
        [gui.Text('Código', size=20), gui.Text(size=20, key='codigo')],
        [gui.Text('Descrição', size=20), gui.Text(size=20, key='descricao')],
        [gui.Text('Valor R$', size=20), gui.Input(size=20, key='valor')],
        [gui.Text()],
        [gui.Text('*Opcional')],
        [gui.Text('Nome do cliente', size=20), gui.Input(size=20, key='cliente')],
        [gui.Text('Nome do vendedor', size=20), gui.Input(size=20, key='vendedor')],
        [gui.Text()],
        [gui.Text(size=10), gui.Button('Cadastrar', size=20), gui.Text(size=10)]
    ]

    window = gui.Window('Sistema de Cadastro de Vendas', layout)

    while True:
        events, values = window.read()
        if events == gui.WINDOW_CLOSED:
            break
        elif events == 'nome':
            produto_selecionado = values['nome']
            index = dados[0].index(produto_selecionado)
            window['descricao'].update(dados[1][index])
            window['disponivel'].update(f'Em estoque: {dados[2][index]}')
            window['codigo'].update(dados[3][index])
        elif not values['nome']:
            gui.popup('Preencha os campos obrigatórios')
            continue
        elif not values['quantidade'].isnumeric():
            gui.popup('Apenas números inteiros', no_titlebar=True)
            continue
        elif not values['valor'].replace('.', '', 1).isnumeric():
            gui.popup('Digite o preço correto')
        elif events == 'Cadastrar':

            produto = values['nome'].title()
            cliente = values['cliente'].title()
            vendedor = values['vendedor'].title()
            preco = float(values['valor'])
            quantidade = int(values['quantidade'])
            print(index, quantidade, dados[1][index])
            if quantidade > dados[1][index]:
                gui.popup('Quantidade não disponivel')
                continue
            codigo = values['codigo']
            descricao = values['descricao'].title()
            total = preco * quantidade
            data = datetime.date.today()
            gui.popup('Venda cadastrada com sucesso!')

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
                Produto TEXT NOT NULL, Descrição TEXT NOT NULL, 
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
