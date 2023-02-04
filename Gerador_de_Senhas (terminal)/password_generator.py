from pass_generator_functions import *

while True:
    opcao = menu(['Letras (Aa, Bb...)', 'Números', 'Letras, números e símbolos', 'Sair'])
    if opcao == 1:
        senha = password_generator(1)
        text(senha)
    elif opcao == 2:
        senha = password_generator(2)
        text(senha)
    elif opcao == 3:
        senha = password_generator(3)
        text(senha)
    elif opcao == 4:
        break
    else:
        print('Opção inválida')
