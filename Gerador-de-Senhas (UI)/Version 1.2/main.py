from functions import *

# interface Gráfica

interface = [

    [Gui.Text('Selecione as opções desejadas', font=16, key='start', justification='c')],

    [Gui.Text('Tipo de senha', font=16, size=15, key='pass_text'),
     Gui.Combo(['De A à Z', 'Numérico', 'Alfanumérico'], font=16, size=13, key='tipo', default_value='-- Selecionar')],

    [Gui.Text('Tamanho da senha', font=16, size=15),
     Gui.Combo(list(range(8, 31)), font=16, key='size', default_value=12)],

    [Gui.Button('Gerar Senha', font=16, size=(25, 2)), Gui.Button('Sair', font=16, size=(8, 2))],

    [Gui.Text(size=35, font=20, key='vazio', justification='c')],

    [Gui.Input(size=45, key='campo', justification='c')],
    [Gui.Button('\t\t Salvar Senha\t\t       ')]
]

janela = Gui.Window('Password Generator', interface, enable_close_attempted_event=True)

success = False
while True:

    # Primeira etapa de verificação de eventos

    evento, valores = janela.read()
    if evento in (Gui.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Sair') and Gui.popup_yes_no('Realmente deseja sair?') == 'Yes':
        break
    elif evento == 'Gerar Senha':

        # Segunda etapa de verificação de eventos para evitar possíveis erros

        valores['size'] = int(valores['size'])
        if valores['size'] <= 0 or valores['size'] is False:
            janela['vazio'].update('Valores negativos não são aceitos')
        elif valores['tipo'] == '-- Selecionar':
            janela['vazio'].update('Escolha uma das opções disponíveis')
        elif valores['tipo'] != 'De A à Z' and valores['tipo'] != 'Numérico' and valores['tipo'] != 'Alfanumérico':
            janela['vazio'].update('Apenas as opções disponíveis serão aceitas.')
        else:

            # Caso tudo esteja certo, finalmente vai para a última etapa de criação da senha

            if valores['tipo'] == 'De A à Z':
                generator = main_function(1, valores['size'])
                janela['vazio'].update('Senha gerada com sucesso!')
                janela['campo'].update(f'{generator}')
                success = True
            elif valores['tipo'] == 'Numérico':
                generator = main_function(2, valores['size'])
                janela['vazio'].update('Senha gerada com sucesso!')
                janela['campo'].update(f'{generator}')
                success = True
            elif valores['tipo'] == 'Alfanumérico':
                generator = main_function(3, valores['size'])
                janela['vazio'].update('Senha gerada com sucesso!')
                janela['campo'].update(f'{generator}')
                success = True
    # Após a senha ser gerada, o usuário pode escolher se salva em um arquivo de texto

    elif evento == '\t\t Salvar Senha\t\t       ':
        if not success:
            janela['vazio'].update('Você ainda não gerou nenhuma senha')
        else:
            success = True
            password = generator
            new_window(password)

janela.close()
