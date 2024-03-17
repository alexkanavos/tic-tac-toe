from utils import board, players, checks
import os


def tic_tac_toe():

    this_board = board.create_board()
    player = players.choose_first_player()
    board.print_board(current_board=this_board)
    play = True

    while play:

        move = input(f"Player ({player}) position: ")
        os.system("clear")
        try:
            move = [int(n) for n in move]
            i = move[0]
            j = move[1]
            if this_board[i, j] == "   ":
                this_board[i, j] = f" {player} "
            else:
                print("Position already filled. Try again.")
        except IndexError:
            print("Position out of board. Try again.")
        except ValueError:
            print("Invalid position. Try again.")

        board.print_board(current_board=this_board)

        if checks.check_win(current_board=this_board):
            print(f"Player ({player}) wins.")
            play = False
        elif not checks.check_tie(current_board=this_board):
            print("It's a tie.")
            play = False

        player = players.switch_player(current_player=player)
