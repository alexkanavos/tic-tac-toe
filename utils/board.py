import numpy as np


arr_6x6 = np.empty((6, 6), dtype="<U3")
arr_6x6[0, 1::2] = np.arange(3)
arr_6x6[1::2, 0] = np.arange(3)
arr_6x6[1::, 2:5:2] = "|"
arr_6x6[2:5, 1::2] = "---"
arr = np.full((6, 6), " ")


def create_board() -> np.ndarray:
    return np.empty((3, 3), dtype="<U3")


def print_board(current_board: np.ndarray):
    for row in current_board:
        print(*row)


def check_win(current_board: np.ndarray) -> bool:

    equality_list = []

    diag_1 = np.diagonal(current_board)
    diag_2 = np.diagonal(np.fliplr(current_board))

    diag_1_exists = all(item == diag_1[0] and item != "" for item in diag_1)
    equality_list.append(diag_1_exists)

    diag_2_exists = all(item == diag_2[0] and item != "" for item in diag_2)
    equality_list.append(diag_2_exists)

    for row in current_board:
        row_exists = all(item == row[0] and item != "" for item in row)
        equality_list.append(row_exists)

    for col in current_board.T:
        col_exists = all(item == col[0] and item != "" for item in row)
        equality_list.append(col_exists)

    return any(equality_list)


def check_tie(current_board: np.ndarray) -> bool:
    return np.any(current_board == "")
