import numpy as np
from .art import logo
import os


def full_board() -> np.ndarray:
    six_by_six_array = np.full((6, 6), fill_value="   ", dtype="<U3")
    six_by_six_array[0, 1::2] = [" 0", "1", "2"]
    six_by_six_array[1::2, 0] = [" 0 ", " 1 ", " 2 "]
    six_by_six_array[1::, 2:5:2] = "|"
    six_by_six_array[2:5:2, 1::2] = "---"

    return six_by_six_array


def create_board() -> np.ndarray:
    return np.full((3, 3), fill_value="   ", dtype="<U3")


def print_board(current_board: np.ndarray, warning: str, player: str, text: str):
    os.system("clear")
    print(logo)
    print("Welcome! Select a position on the board (e.g. '01', '12').\n")
    tic_tac_toe_board = full_board()
    tic_tac_toe_board[1::2, 1::2] = current_board
    for row in tic_tac_toe_board:
        print(*row)
    print("\n")
    if warning != None:
        print(warning)
    if text != None:
        print(text)
