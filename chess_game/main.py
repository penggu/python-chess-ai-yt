from board.board import Board
from pieces.piece import Piece
from players.human_player import HumanPlayer

def main():
    # create the chess board and the players
    board = Board()
    white_player = HumanPlayer("white")
    black_player = HumanPlayer("black")

    # set up the game loop
    current_player = white_player
    while not board.is_game_over():
        # ask the current player for their move
        move = current_player.get_move(board)

        # make the move on the board
        piece = board.get_piece(move.initial_pos)
        board.move_piece(piece, move.final_pos)

        # update the current player
        current_player = black_player if current_player == white_player else white_player

    # print the winner of the game
    winner = board.get_winner()
    if winner is None:
        print("The game ended in a draw.")
    else:
        print(f"The winner is {winner}.")

if __name__ == "__main__":
    main()
