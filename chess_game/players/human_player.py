from game.move import Move

class HumanPlayer:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        while True:
            try:
                # Prompt the user to enter a move
                move_str = input(f"Enter {self.color} player move (e.g. e2 e4): ")
                # Parse the move string and create a Move object
                initial_pos, final_pos = move_str.split()
                initial_row, initial_col = ord(initial_pos[1]) - ord('1'), ord(initial_pos[0]) - ord('a')
                final_row, final_col = ord(final_pos[1]) - ord('1'), ord(final_pos[0]) - ord('a')
                move = Move((initial_row, initial_col), (final_row, final_col))
                # Check if the move is valid
                if board.is_valid_move(move, self.color):
                    return move
                else:
                    print("Invalid move, please try again.")
            except ValueError:
                print("Invalid input, please enter two space-separated positions.")
