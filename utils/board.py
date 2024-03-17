import numpy as np


arr_6x6 = np.full((6, 6), fill_value="   ", dtype="<U3")
arr_6x6[0, 1::2] = [" 0", "1", "2"]
arr_6x6[1::2, 0] = [" 0 ", " 1 ", " 2 "]
arr_6x6[1::, 2:5:2] = "|"
arr_6x6[2:5:2, 1::2] = "---"


def create_board() -> np.ndarray:
    return np.full((3, 3), fill_value="   ", dtype="<U3")


def print_board(current_board: np.ndarray):
    arr_6x6[1::2, 1::2] = current_board
    tic_tac_toe_board = arr_6x6
    for row in tic_tac_toe_board:
        print(*row)
