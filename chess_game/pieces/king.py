from .piece import Piece

class King(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.has_moved = False

    def get_moves(self, board):
        # add code to get the possible moves for the king
        moves = []

        # check the eight adjacent squares
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                row = self.pos[0] + dx
                col = self.pos[1] + dy
                if 0 <= row < 8 and 0 <= col < 8:
                    piece = board.get_piece((row, col))
                    if piece is None or piece.color != self.color:
                        moves.append((row, col))

        # add code to handle castling

        return moves
