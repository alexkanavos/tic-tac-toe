import numpy as np
import random

SYMBOLS = ["X", "O"]
board_array = np.full((3, 3), fill_value="_", dtype="<U3")

play = True
symbol = random.choice(SYMBOLS)

while play:
    print(board_array)
    move = input(f"Player ({symbol}) position: ")
    try:
        move = [int(n) for n in move]
        i = move[0]
        j = move[1]
        if board_array[i, j] == "_":
            board_array[i, j] = symbol
        else:
            print("Position already filled. Try again.")
    except IndexError:
        print("Position out of board. Try again.")
    except ValueError:
        print("Invalid position. Try again.")
