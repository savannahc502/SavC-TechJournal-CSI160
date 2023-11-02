"""Tic-Tac-Toe Game! Needs two players, as it requires an input from PLAYER_X and PLAYER_Y

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 8/9 Lab: Tic-Tac-Toe
Due Date: 10/20/23

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import time

# Constants in are named in all caps (PEP8 Standard)
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
TIE_GAME = 'tie'
BOARD_SIZE = 3

current_player = PLAYER_X  # Player X goes first

# Builds an EMPTY board
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]


def print_board():
    # Clear the screen
    # replit.clear()

    """Prints the board to the console"""
    print('    0   1   2')
    print('  -------------')
    for i, row in enumerate(board):
        print(i, end="")
        for square in row:
            print(' | ' + square, end="")
        print(' |')
        print('  -------------')


def is_empty(row, col):
    """Returns True/False if a square is EMPTY

    params row, col: (int) The row and Column to Check
    return: (boolean) If the row is EMPTY
    """
    # TODO Part #1 complete is_empty()
    if board[row][col] == EMPTY:  # Checks to see if each index in the nested list is EMPTY
        # If so, it's true and the player can move.
        return True
    else:
        return False  # Else, if the index has a value, the player cannot make a move.


def move(player, row, col):
    """Makes a game move

    If a move is legal, moves the player to the row and col
    and returns True. If a move is illegal, no move is made
    and returns False. Hint: Should make use of is_empty()

    param player: Either PLAYER_X or PLAYER_O
    param row, col: (int) The row and Column to move to
    return: (boolean) Success of the move
    
    Assumptions: 
    Player enters a valid integer digit in the While True statement at the bottom of the code
    """
    # TODO Part #2 complete move()
    if row > 2 or row < 0:  
        # Makes sure that input from the player is within an acceptable range
        return False
    if col > 2 or row < 0:  
        # Makes sure that input from the player is within an acceptable range
        return False
    # if not row.isdigit() or not col.isdigit():  
    # https://www.scaler.com/topics/isdigit-java/
        # return False
        # I was attempting to create a check for valid digit input, but that threw off the rest of the code.
        # For simplicity, the function assumes a digit input. 
    elif is_empty(row, col) == False:
        return False  # Uses the is_empty function to check if the move is illegal
    else:
        board[row][col] = player
        return True  # Uses the is_empty function to check if the move is legal


def determine_winner():
    """Determine if there is a winner

    return: Returns None if there is no winner.
            Returns PLAYER_O or PLAYER_X if one of them won.
            Returns 'tie' if noone wins
    """
    # TODO Part #3 complete determine_winner()
    # The code below follows a similar pattern: it checks for possible win combinations 
    # and makes sure the interpreter does not include a row of 'EMPTY' as a win. 
    
    # Step 1: Check the horizontals looking for a winner.
    #         If so return winner.
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 'EMPTY':
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != 'EMPTY':
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != 'EMPTY':
        return board[2][0]
    # Step 2: Check the verticals looking for a winner
    #         If so return winner.
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != 'EMPTY':
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != 'EMPTY':
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != 'EMPTY':
        return board[0][2]
    # Step 3: Check the diagonals looking for a winner
    #         If so return winner.
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 'EMPTY' \
            or board[0][2] == board[1][1] == board[2][0] and board[0][2] != 'EMPTY':
        return board[1][1]
    # How to write a condition in multiple lines:
    # https://note.nkmk.me/en/python-if-elif-else/
    
    # Step 4: Check to see if there are empty squares.
    #         If there are empty squares, return None because
    #         noone has won the game yet
    #         If there are no empty squares return TIE_GAME
    #         because we didn't find a winner and all moves are made
    for row in board:
        if EMPTY in row:
            return None
    return TIE_GAME

while True:
    print()
    print_board()
    print()
    print('It is', current_player, 'turn')
    row = int(input('What is the row (0-2)? '))
    col = int(input('What is the col (0-2)? '))

    # Make sure the move is legal, if so make the move
    if is_empty(row, col):
        move(current_player, row, col)
    else:
        print('That is not a legal move!')
        time.sleep(2)
        continue

    # Check if there is a winner
    winner = determine_winner()
    if winner in (PLAYER_O, PLAYER_X):
        print_board()
        print('Congratulations', winner, '!!! You won!')
        print('But you are all winners')
        break

    if winner == TIE_GAME:
        print_board()
        print("It's a tie!!!")
        break

        # Let the other player have a turn
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O
