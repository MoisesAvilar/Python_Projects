import PySimpleGUI as gui
import datetime
import sqlite3


def menu():
    return [
        ['Arquivo', 'Nada'],
        ['Ajuda', ['Sobre']]]


def tabela_produtos(nome, descricao, quantidade, tamanho):
    con = sqlite3.connect('produtos.db')
    con.execute('''CREATE TABLE IF NOT EXISTS Produtos
                (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                Produto TEXT NOT NULL, 
                Descrição TEXT NOT NULL, 
                Quantidade INTEGER NOT NULL, 
                Tamanho TEXT NOT NULL)''')
    con.execute('''INSERT INTO Produtos (Produto, Descrição, Quantidade, Tamanho)
                                VALUES (?, ?, ?, ?)''', (nome, descricao, quantidade, tamanho))
    con.commit()
    con.close()


def carregar_vendas(produto, detalhes, codigo, quantidade, preco, vendedor, cliente, total, data):
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
    con.execute('''INSERT INTO Vendas 
                (Produto, Descrição, Código, Quantidade, Preço, Vendedor, Cliente, Total, Data) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (produto, detalhes, codigo, quantidade, preco, vendedor, cliente, total, data))
    con.commit()
    con.close()


def carregar_produtos(produto, quantidade):
    con = sqlite3.connect('produtos.db')
    cursor = con.cursor()
    cursor.execute('''SELECT Quantidade FROM Produtos WHERE Produto = ?''', (produto,))
    valor = cursor.fetchone()
    valor = valor[0]
    restante = valor - quantidade
    cursor.execute('''UPDATE Produtos SET Quantidade = ? WHERE Produto = ?''', (restante, produto,))
    con.commit()
    con.close()


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


class CadastrarVenda:
    def __init__(self):
        global index
        dados = carregar_dados()
        nome = [tupla[0] for tupla in dados]
        descricao = [tupla[1] for tupla in dados]
        volume = [tupla[2] for tupla in dados]
        referencia = [tupla[3] for tupla in dados]

        layout = [
            [gui.Text('Registro de Venda de Produtos', font=('Helvetica', 20), size=40, justification='c')],
            [gui.Frame('Dados do Produto',
                layout=[
                    [gui.Menu(menu())],
                    [gui.Button(
                        image_filename=r'C:\Users\moise\Documents\Python_Projects'
                        r'\Gerenciador-de-Vendas\images\2990061.png',
                        image_size=(60, 60), key='img')],
                    [gui.Text('Nome do produto', size=20),
                        gui.Combo(nome, size=20, key='nome', enable_events=True, readonly=True,
                        background_color='lightgray', text_color='darkblue')],
                    [gui.Text('Quantidade', size=20),
                        gui.Input(size=5, key='quantidade', background_color='lightgray', text_color='darkblue'),
                        gui.Text(key='disponivel')],
                    [gui.Text('Código/Referência', size=20), gui.Text(size=20, key='codigo')],
                    [gui.Text('Descrição', size=20), gui.Text(size=20, key='descricao')],
                    [gui.Text('Valor R$', size=20),
                        gui.Input(size=20, key='valor', background_color='lightgray', text_color='darkblue')],
                    [gui.Text(size=10), gui.Button('Adicionar produto', size=20), gui.Text(size=10)],
                    [gui.Text()],
                    [gui.Text('*Opcional')],
                    [gui.Text('Nome do cliente', size=20),
                        gui.Input(size=20, key='cliente', background_color='lightgray', text_color='darkblue')],
                    [gui.Text('Nome do vendedor', size=20),
                        gui.Input(size=20, key='vendedor', background_color='lightgray', text_color='darkblue')],
                    [gui.Text()],
                    [gui.Text(size=10), gui.Button('Registrar', size=20), gui.Text(size=10)],
                    [gui.Text()],
                    ]
                )
            ]
        ]

        self.window = gui.Window('Sistema de Registro de Vendas', layout,
                                element_justification='c', font=('Helvetica', 16))

        while True:
            events, values = self.window.read()
            if events == gui.WINDOW_CLOSED:
                break
            elif events == 'nome':
                produto_selecionado = values['nome']
                index = nome.index(produto_selecionado)
                self.window['descricao'].update(descricao[index])
                self.window['disponivel'].update(f'Em estoque: {volume[index]}')
                self.window['codigo'].update(referencia[index])
                atualizar_estoque(produto_selecionado, self.window)
            elif not values['nome']:
                gui.popup('Preencha os campos obrigatórios')
                continue
            elif not values['quantidade'].isnumeric():
                gui.popup('Apenas números inteiros', no_titlebar=True)
                continue
            elif not values['valor'].replace('.', '', 1).isnumeric():
                gui.popup('Digite o preço correto')
                continue
            elif int(values['quantidade']) > volume[index]:
                gui.popup('Quantidade não disponivel')
                continue
            elif events == 'Adicionar produto':
                produto = values['nome']
                detalhes = self.window['descricao'].get().encode('utf-8')
                codigo = self.window['codigo'].get().encode('utf-8')
                quantidade = int(values['quantidade'])
                preco = float(values['valor'])
                vendedor = values['vendedor'].title()
                cliente = values['cliente'].title()
                total = preco * quantidade
                data = datetime.date.today()

                carregar_vendas(produto, detalhes, codigo, quantidade, preco, vendedor, cliente, total, data)
                gui.popup('Venda registrada com sucesso!')

                self.window.Element('nome').update('')
                self.window.Element('descricao').update('')
                self.window.Element('codigo').update('')
                self.window.Element('quantidade').update('')
                self.window.Element('disponivel').update('')
                self.window.Element('valor').update('')
                self.window.Element('vendedor').update('')
                self.window.Element('cliente').update('')

            elif events == 'Registrar':
                produto = values['nome']
                detalhes = self.window['descricao'].get().encode('utf-8')
                codigo = self.window['codigo'].get().encode('utf-8')
                quantidade = int(values['quantidade'])
                preco = float(values['valor'])
                vendedor = values['vendedor'].title()
                cliente = values['cliente'].title()
                total = preco * quantidade
                data = datetime.date.today()

                carregar_vendas(produto, detalhes, codigo, quantidade, preco, vendedor, cliente, total, data)

                gui.popup('Venda registrada com sucesso!')

                carregar_produtos(produto, quantidade)

        self.window.close()


class CadastrarProduto:
    def __init__(self):
        layout = [
            [gui.Text('Nome do Produto', size=20), gui.Input(key='nome', size=20)],
            [gui.Text('Descrição do Produto', size=20), gui.Input(key='descricao', size=20)],
            [gui.Text('Quantidade', size=20), gui.Input(key='quantidade', size=20)],
            [gui.Text('Tamanho', size=20), gui.Input(key='tamanho', size=20)],
            [gui.Text(size=10), gui.Button('Confirmar', size=20), gui.Text(size=10)],
        ]

        self.window = gui.Window('Cadastrar Produtos', layout)

        while True:
            event, value = self.window.read()

            if event == gui.WINDOW_CLOSED or event == gui.WIN_X_EVENT:
                CadastrarVenda()
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

                tabela_produtos(nome, descricao, quantidade, tamanho)

                self.window.Element('nome').update('')
                self.window.Element('descricao').update('')
                self.window.Element('quantidade').update('')
                self.window.Element('tamanho').update('')
                self.window['nome'].set_focus()
                gui.popup('Produto cadastrado com sucesso!')

        self.window.close()
