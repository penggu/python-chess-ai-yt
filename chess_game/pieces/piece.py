class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.has_moved = False

    def get_moves(self, board):
        # add code to get the possible moves for the piece
        return []

class Pawn(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.has_moved = False
        self.en_passant_target = False

    def get_moves(self, board):
        # add code to get the possible moves for the pawn
        return []

class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)

    def get_moves(self, board):
        # add code to get the possible moves for the knight
        return []

class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)

    def get_moves(self, board):
        # add code to get the possible moves for the bishop
        return []

class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.has_moved = False

    def get_moves(self, board):
        # add code to get the possible moves for the rook
        return []

class Queen(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)

    def get_moves(self, board):
        # add code to get the possible moves for the queen
        return []

class King(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.has_moved = False

    def get_moves(self, board):
        # add code to get the possible moves for the king
        return []
