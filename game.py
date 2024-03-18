from utils import board, players, checks


def tic_tac_toe():

    play = True

    while play:

        this_board = board.create_board()
        current_player = players.choose_first_player()
        error = None
        text = None

        while True:

            board.print_board(
                current_board=this_board,
                warning=error,
                player=current_player,
                text=text,
            )
            move = input(f"Player ({current_player}) position: ")
            try:
                if len(move) != 2:
                    raise ValueError
                move = [int(n) for n in move]
                i = move[0]
                j = move[1]
                if this_board[i, j] == "   ":
                    this_board[i, j] = f" {current_player} "
                    if checks.check_win(current_board=this_board):
                        board.print_board(
                            current_board=this_board,
                            warning=error,
                            player=current_player,
                            text=f"Player ({current_player}) wins.",
                        )
                        break
                    elif not checks.check_tie(current_board=this_board):
                        board.print_board(
                            current_board=this_board,
                            warning=error,
                            player=current_player,
                            text="It's a tie.",
                        )
                        break

                    error = None
                    current_player = players.switch_player(player=current_player)
                else:
                    error = "Position already filled. Try again."
            except IndexError:
                error = "Position out of board. Try again."
            except ValueError:
                error = "Invalid position. Try again."

        if input("Do you want to play again? Type (y/n): ").lower() == "n":
            play = False
