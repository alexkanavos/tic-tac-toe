import numpy as np
from utils import choose_first_player, switch_player
import os


board = np.full((3, 3), fill_value="_", dtype="<U3")


play = True
print(board)

player = choose_first_player()

while play:
    move = input(f"Player ({player}) position: ")
    try:
        move = [int(n) for n in move]
        i = move[0]
        j = move[1]
        if board[i, j] == "_":
            board[i, j] = player
            player = switch_player(current_player=player)
        else:
            print("Position already filled. Try again.")
    except IndexError:
        print("Position out of board. Try again.")
    except ValueError:
        print("Invalid position. Try again.")
    print(board)
