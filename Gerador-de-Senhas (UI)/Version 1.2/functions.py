import PySimpleGUI as Gui
from string import ascii_letters, digits
from random import sample


def main_function(caracter, lenght):
    """
    Função responsável para gerar uma senha aleatória através de dados inseridos pelo usuário.
    :param caracter: Recebe o tipo de dado (string) que a senha terá.
    :param lenght: Tamanho da senha em valores inteiros.
    :return: retorna a senha gerada à interface para o usuário.
    """

    lst = []
    if caracter == 1:
        lst = ascii_letters
    elif caracter == 2:
        lst = digits
    elif caracter == 3:
        lst = ascii_letters + digits

    password = ''

    for simbol in range(lenght):
        password += sample(lst, 1)[0]

    return password


def save_password(password, conta):
    with open('arquivo.txt', 'a+') as file:
        file.write(f"Conta/Usuario: {conta} \nSenha: {password}\n")


def new_window(password):
    layout = [
        [Gui.Text('Nome do site ou usuário', size=20), Gui.Input(size=10, key='conta')],
        [Gui.Text(size=30, key='dialog', justification='c', font=20)],
        [Gui.Text(size=10), Gui.Button('Salvar', size=10, font=20), Gui.Text(size=10)]
    ]

    window = Gui.Window('Salvar Senha', layout, modal=True)

    while True:
        event, values = window.read()
        if event == Gui.WINDOW_CLOSED:
            break
        elif event == 'Salvar':
            conta = values['conta']
            save_password(password, conta)
            window['dialog'].update('Senha salva com sucesso')

    window.close()
