# Marino Tselani   May 2022.

board = [' ', ' ', ' ',   # The dementions of the tictactoe board, filled without any player moves.
         ' ', ' ', ' ',
         ' ', ' ', ' ']

players = {'X': 'player 1', 'O': 'player 2'} # p1 has X , p2 has O , put into a dictionary.

# The winning combinations .
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

current_player = 'X'    # p1 always starts 1st
game_over = False       # flag init

while not game_over: #
    # printing the board inside the while loop as the game has not ended
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

    # get the next move of the current plaer.
    while not False:
        move = int(input(f'{players[current_player]}, enter your move (0-8): '))
        if move>8 or move<0:
            print('I said numbers between 0 and 8')
        else:
            break

    # we update the board with the move of the current player
    if board[move] == ' ':
        board[move] = current_player
    else:
        print('This position is already occupied.')
        continue

    #we  ccheck if the game has ended.
    for combination in winning_combinations:
        if board[combination[0]] == current_player and board[combination[1]] == current_player and board[combination[2]] == current_player:
            print(f'{players[current_player]} wins!')
            game_over = True
            break
    else:                       # the else part is asigned , when the 2 players have filled the board without achieving any of the winning combinations
        if ' ' not in board:
            print('Marino wins, because neither of you did')
            game_over = True

    # the part of the code where we switch the players' turn
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'