import itertools
import random
from random import randint

board = []

for x in range(0, 3):
    board.append(["()"] * 3)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)

ship_positions = list(itertools.product(range(len(board)), range(len(board))))
print(f"{ship_positions=}")

ship_sunk = True
for turn in range(4):
    if ship_sunk:
        A_row, A_col = ship_positions.pop(random.randint(0, len(ship_positions) - 1))
        print(f"{A_row=}, {A_col=}")
        print(f"{ship_positions=}")
        ship_sunk = False

    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if (guess_row == A_row and guess_col == A_col):
        print("Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "(X)"
        print_board(board)
        ship_sunk = True

    else:
        if (guess_row not in range(3) or guess_col not in range(3)):
            print("Oops, that's not even in the ocean..")
        elif board[guess_row][guess_col] == '(0)':
            print("You guessed that one already")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col] = "(0)"
            print_board(board)
        if (turn == 3):
            print("Game Over")
