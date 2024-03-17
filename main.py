from utils import board, players


play = True
this_board = board.create_board()
player = players.choose_first_player()


while play:
    board.print_board(current_board=this_board)
    move = input(f"Player ({player}) position: ")
    try:
        move = [int(n) for n in move]
        i = move[0]
        j = move[1]
        if this_board[i, j] == "":
            this_board[i, j] = player
            player = players.switch_player(current_player=player)
        else:
            print("Position already filled. Try again.")
    except IndexError:
        print("Position out of board. Try again.")
    except ValueError:
        print("Invalid position. Try again.")

    if board.check_win(current_board=this_board):
        print(f"Player ({player}) wins.")
        play = False
    elif not board.check_tie(current_board=this_board):
        print("It's a tie.")
        play = False

# if __name__ == "__main__":
#     tic_tac_toe()
