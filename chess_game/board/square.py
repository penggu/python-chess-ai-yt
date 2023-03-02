class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.piece = None

    def has_piece(self):
        return self.piece is not None

    def set_piece(self, piece):
        self.piece = piece

    def clear_piece(self):
        self.piece = None
