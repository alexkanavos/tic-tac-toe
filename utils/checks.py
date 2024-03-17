import numpy as np


def check_win(current_board: np.ndarray) -> bool:

    equality_list = []

    diag_1 = np.diagonal(current_board)
    diag_2 = np.diagonal(np.fliplr(current_board))

    diag_1_exists = all(item == diag_1[0] and item != "   " for item in diag_1)
    equality_list.append(diag_1_exists)

    diag_2_exists = all(item == diag_2[0] and item != "   " for item in diag_2)
    equality_list.append(diag_2_exists)

    for row in current_board:
        row_exists = all(item == row[0] and item != "   " for item in row)
        equality_list.append(row_exists)

    for col in current_board.T:
        col_exists = all(item == col[0] and item != "   " for item in col)
        equality_list.append(col_exists)

    return any(equality_list)


def check_tie(current_board: np.ndarray) -> bool:
    return np.any(current_board == "   ")
