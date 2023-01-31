from random import sample
from string import ascii_letters, digits, punctuation


def line(size=15):
    """
    Linha Personalizada
    :param size: altera o tamanho da mesma
    :return: retorna a linha personalizada no tamanho informado (ou não)
    """
    return '-=' * size


def text(param):
    """
    Texto formatado para exibição mais bonita
    :param param: senha gerada
    :return: retorna a senha formatada com um cabeçalho
    """
    print(line())
    print(f'Senha gerada: {param}')
    print(line())


def head(t_str):
    """
    Cabeçalho Personalizado
    :param t_str: texto a ser formatado
    :return: retorna o cabeçalho personalizado com o texto informado
    """
    print(line())
    print(f'{t_str}'.center(30))
    print(line())


def menu(lista):
    """
    Menu Principal
    :param lista: lista com as opções passadas no código principal
    :return: devolve o menu formatado e com a opção escolhida
    """
    head('Menu principal'.upper())
    counter = 1
    for item in lista:
        print(f'{counter} - {item}')
        counter += 1
    print()
    escolha = leitor_de_inteiro('Escolha uma opção: ')
    return escolha


def leitor_de_inteiro(num):
    """
    Função que lê qualquer caractere e retorna somente números inteiros
    :param num: caractere introduzido pelo usuário
    :return: devolve um número inteiro apenas
    """
    while True:
        try:
            number = int(input(num))
        except (TypeError, ValueError):
            print('Apenas números inteiros são válidos')
            continue
        except KeyboardInterrupt:
            print('\nO usuário cancelou a entrada')
            return 0
        else:
            return int(number)


def password_generator(tipo_de_dado=1, size=12):
    """Esta função gera uma senha com caracteres aleatórios
    :param tipo_de_dado: Passa a escolhe do usuário dos dados
    :param size: Define o tamanho da senha, caso não informado será 0
    :return: Retorna a palavra-passe aleatória
    """
    # Armazena letras maiúsculas e minúsculas
    letras = ascii_letters
    # Armazena números de 0 a 9
    numeros = digits
    # Armazena simbolos
    simbolos = punctuation
    # Lista com a junção de letras e números
    caracteres = list()
    if tipo_de_dado == 1:
        caracteres = letras
    elif tipo_de_dado == 2:
        caracteres = numeros
    elif tipo_de_dado == 3:
        caracteres = letras + numeros + simbolos
    # Lista vazia que vai receber a senha gerada
    password = ""

    for counter in range(size):
        password += sample(caracteres, 1)[0]

    return password
