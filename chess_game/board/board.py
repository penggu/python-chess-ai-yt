from .pieces.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self):
        # create an 8x8 grid of squares
        self.squares = [[None for _ in range(8)] for _ in range(8)]

        # set up the starting position of the pieces
        self.squares[0][0] = Rook("black")
        self.squares[0][1] = Knight("black")
        self.squares[0][2] = Bishop("black")
        self.squares[0][3] = Queen("black")
        self.squares[0][4] = King("black")
        self.squares[0][5] = Bishop("black")
        self.squares[0][6] = Knight("black")
        self.squares[0][7] = Rook("black")
        for col in range(8):
            self.squares[1][col] = Pawn("black")

        self.squares[7][0] = Rook("white")
        self.squares[7][1] = Knight("white")
        self.squares[7][2] = Bishop("white")
        self.squares[7][3] = Queen("white")
        self.squares[7][4] = King("white")
        self.squares[7][5] = Bishop("white")
        self.squares[7][6] = Knight("white")
        self.squares[7][7] = Rook("white")
        for col in range(8):
            self.squares[6][col] = Pawn("white")

        # keep track of the current player
        self.current_player = "white"

        # keep track of the last move made
        self.last_move = None

        # keep track of the number of moves made since the last capture or pawn move
        self.halfmove_clock = 0

        # keep track of the fullmove number
        self.fullmove_number = 1

    def get_piece(self, pos):
        return self.squares[pos[0]][pos[1]]

    def move_piece(self, piece, pos):
        self.squares[piece.pos[0]][piece.pos[1]] = None
        self.squares[pos[0]][pos[1]] = piece
        piece.pos = pos

    def is_game_over(self):
        # add code to check for game over conditions
        return False

    def get_winner(self):
        # add code to determine the winner
        return None
