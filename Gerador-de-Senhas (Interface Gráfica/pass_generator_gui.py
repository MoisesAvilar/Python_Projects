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


print(main_function(1, 10))
