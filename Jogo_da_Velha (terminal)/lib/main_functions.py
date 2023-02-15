from random import randint


def line(size=21):
    return '-=' * size


def head(txt):
    print(line())
    print(f'{txt:^42}'.upper())
    print(line())


def welcome_player():
    head('tic-tac-toe')
    print('Welcome to the Tic-Tac-Toe game'.center(42))
    print('Can you defeat the Elton Musgo AI???'.center(42))
    print('Please choose one option below'.center(42))
    print(line())


def name(name_player):
    name_player = input(name_player)
    return name_player


def main_menu():
    head('Main menu')


def tic_tac_toe(matrix):
    head('tic-tac-toe')
    counter = 1
    for num in matrix:
        if counter == 2 or counter == 5 or counter == 8:
            print(f'| {num}', end=' | ')
        elif counter == 3 or counter == 6 or counter == 9:
            print(f'{num}')
            print(f"\t\t\t\t{('_ ' * 5)}")
        else:
            print(f'\t\t\t\t{num:}', end=' ')
        counter += 1


def player():
    while True:
        try:
            inputed_option = str(input('Choose only X or O: ')).upper().strip()
        except KeyboardInterrupt:
            print('User has stopped program')
        else:
            if inputed_option not in 'XO':
                print('Incorrect option')
            elif inputed_option in ' ':
                print('Do not try cheat the system')
            else:
                return inputed_option


def verify(chose):
    if chose == 'X':
        bot = 'O'
    else:
        bot = 'X'
    return bot


def read_integer(number):
    ok = False
    while not ok:
        try:
            n = int(input(number))
        except (ValueError, TypeError):
            print('Only integers are allowed')
        except KeyboardInterrupt:
            print('User has stopped')
        else:
            if n < 1 or n > 9:
                print('Number needs to be bigger than 1 and less than 9')
            else:
                ok = True
                return n


def player_round(matrix, chosen, name_player):
    head('player round')
    ok = False
    while not ok:
        position = read_integer(f'{name_player}, where will you play? ')
        for number in matrix:
            if position == number:
                matrix[position - 1] = chosen
                ok = True
        if ok:
            pass
        else:
            print('Try again with another number')


def bot_round(matrix, bot):
    head('bot round')
    ok = False
    while not ok:
        bot_number = randint(1, 9)
        for number in matrix:
            if bot_number == number:
                matrix[bot_number - 1] = bot
                ok = True
        if ok:
            pass
        else:
            pass
    print(f'Bot choose: {bot_number}')


def player_wins(matrix, chosen):
    # Verifying lines:
    if matrix[0] == chosen and matrix[1] == chosen and matrix[2] == chosen:
        return True
    elif matrix[3] == chosen and matrix[4] == chosen and matrix[5] == chosen:
        return True
    elif matrix[6] == chosen and matrix[7] == chosen and matrix[8] == chosen:
        return True

    # Verifying columns:
    elif matrix[0] == chosen and matrix[3] == chosen and matrix[6] == chosen:
        return True
    elif matrix[1] == chosen and matrix[4] == chosen and matrix[7] == chosen:
        return True
    elif matrix[2] == chosen and matrix[5] == chosen and matrix[8] == chosen:
        return True

    # Verifying diagonals
    elif matrix[0] == chosen and matrix[4] == chosen and matrix[8] == chosen:
        return True
    elif matrix[6] == chosen and matrix[4] == chosen and matrix[2] == chosen:
        return True
    return False


def bot_wins(matrix, bot):
    # Verifying lines:
    if matrix[0] == bot and matrix[1] == bot and matrix[2] == bot:
        return True
    elif matrix[3] == bot and matrix[4] == bot and matrix[5] == bot:
        return True
    elif matrix[6] == bot and matrix[7] == bot and matrix[8] == bot:
        return True

    # Verifying columns:
    elif matrix[0] == bot and matrix[3] == bot and matrix[6] == bot:
        return True
    elif matrix[1] == bot and matrix[4] == bot and matrix[7] == bot:
        return True
    elif matrix[2] == bot and matrix[5] == bot and matrix[8] == bot:
        return True

    # Verifying diagonals
    elif matrix[0] == bot and matrix[4] == bot and matrix[8] == bot:
        return True
    elif matrix[6] == bot and matrix[4] == bot and matrix[2] == bot:
        return True
    return False
