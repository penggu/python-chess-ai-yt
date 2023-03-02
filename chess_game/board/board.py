import sys
# sys.path.append("..")
from pieces.piece import Piece, Pawn, Knight, Bishop, Rook, Queen
from pieces.king import King

class Board:
    def __init__(self):
        # create an 8x8 grid of squares
        self.squares = [[None for _ in range(8)] for _ in range(8)]

        # set up the starting position of the pieces
        self.squares[0][0] = Rook("black", (0, 0))
        self.squares[0][1] = Knight("black", (0, 1))
        self.squares[0][2] = Bishop("black", (0, 2))
        self.squares[0][3] = Queen("black", (0, 3))
        self.squares[0][4] = King("black", (0, 4))
        self.squares[0][5] = Bishop("black", (0, 5))
        self.squares[0][6] = Knight("black", (0, 6))
        self.squares[0][7] = Rook("black", (0, 7))
        for col in range(8):
            self.squares[1][col] = Pawn("black", (1, col))

        self.squares[7][0] = Rook("white", (7, 0))
        self.squares[7][1] = Knight("white", (7, 1))
        self.squares[7][2] = Bishop("white", (7, 2))
        self.squares[7][3] = Queen("white", (7, 3))
        self.squares[7][4] = King("white", (7, 4))
        self.squares[7][5] = Bishop("white", (7, 5))
        self.squares[7][6] = Knight("white", (7, 6))
        self.squares[7][7] = Rook("white", (7, 7))
        for col in range(8):
            self.squares[6][col] = Pawn("white", (6, col))

        # keep track of the current player
        self.current_player = "white"

        # keep track of the last move made
        self.last_move = None

        # keep track of the number of moves made since the last capture or pawn move
        self.halfmove_clock = 0

        # keep track of the fullmove number
        self.fullmove_number = 1

    def set_piece(self, pos, piece):
        self.squares[pos[0]][pos[1]].set_piece(piece)

    def get_piece(self, pos):
        return self.squares[pos[0]][pos[1]]

    def move_piece(self, piece, pos):
        self.squares[piece.pos[0]][piece.pos[1]] = None
        self.squares[pos[0]][pos[1]] = piece
        piece.pos = pos

    def remove_piece(self, pos):
        self.squares[pos[0]][pos[1]] = None

    def is_valid_pos(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8
    
    def is_valid_move(self, piece, pos):
        # check if the position is valid
        if not self.is_valid_pos(pos):
            return False

        # check if the piece is of the correct color
        if piece.color != self.current_player:
            return False

        # check if the piece can move to the position
        if not piece.can_move(self, pos):
            return False

        # check if the move would put the player in check
        if self.is_in_check(piece.color, piece.pos, pos):
            return False

        return True

    def is_game_over(self):
        # add code to check for game over conditions
        return False

    def get_winner(self):
        # add code to determine the winner
        return None
