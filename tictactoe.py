def display_board(board):
    print("\n" * 100)
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("----------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("----------")
    print(board[1] + " | " + board[2] + " | " + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


def player_input():
    '''
    OUTPUT  = (Player 1 marker, Player 2 Marker)
    '''
    marker = " "

    # KEEP ASKING PLAYER 1 to choose X or O
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1, Choose X or O: ").upper()

    # ASSIGN PLAYER 2, the opposite marker

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


player1_marker, player2_marker = player_input()


def place_marker(board, marker, position):
    board[position] = marker

display_board(test_board)


def win_check(board, mark):
    # WIN TIC TAC TOE?
    return (
        # ALL ROWS , and check to see if they all share the same marker?
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # ALL CLOUMNS,check to see if marker matches
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # 2 diagonals, check to see match
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


display_board(test_board)
win_check(test_board, "X")

import random

def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for char in range(1, 10):
        if space_check(board, char):
            return False
    # BOARD IS FULL, WE RETURN TRUE
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position:(1-9) "))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# WHILE LOOP TO KEEP RUNNING THE GAME
print("Welcome to Tic TAC TOE")

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST , CHOOSE MARKERS X or O)
    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n? ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False
    ## GAME PLAY

    while game_on:
        ### PLAYER ONE TURN
        if turn == "Player 1":

            # Show the board
            display_board(the_board)
            # They can choose a position
            position = player_choice(the_board)
            # Place the marker to that position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 Has Won!!")
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 2"
            # No tie and no win? Then next player's turn


        ### PLAYER TWO TURN
        else:
            # Show the board
            display_board(the_board)
            # They can choose a position
            position = player_choice(the_board)
            # Place the marker to that position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 Has Won!!")
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()
