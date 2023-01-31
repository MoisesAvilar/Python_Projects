from lib.main_functions import *

# Main code
welcome_player()  # Welcome screen
name_player = name('Your name: ').title().strip()  # Get player's name
chosen = player()   # Let the player decice which one to play
print(f'{name_player} has chose: {chosen}')  # Shows name and choice in an f_string
bot = verify(chosen)    # If player choose one option, bot got another
print(f'Bot got: {bot}')    # Shows bot's choice
matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # List with 9 numbers

# Main Looping
while True:
    tic_tac_toe(matrix)  # Function to shows a 3x3 matrix
    player_round(matrix, chosen, name_player)  # Call another function to get number and add to matrix
    if player_wins(matrix, chosen):
        tic_tac_toe(matrix)
        head(f'{name_player} Wins')
        break
    bot_round(matrix, bot)  # Do the same thing that function above, except get number
    if bot_wins(matrix, bot):
        tic_tac_toe(matrix)
        print(line())
        print(f'YOU LOSE'.center(42))
        print(line())
        break
