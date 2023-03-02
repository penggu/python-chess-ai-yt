import pygame
import sys
from board.board import Board
from pieces.piece import Piece
from players.human_player import HumanPlayer

# constants
WIDTH = 640
HEIGHT = 480
FPS = 30

class ChessGame:
    def __init__(self):
        # set up the game window
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")

        # load the images
        self.board_image = pygame.image.load("board.png")
        self.pieces_image = pygame.image.load("pieces.png")

        # create the chess board and the players
        self.board = Board()
        self.white_player = HumanPlayer("white")
        self.black_player = HumanPlayer("black")
        self.current_player = self.white_player

        # set up the game loop
        self.clock = pygame.time.Clock()

    def run(self):
        while not self.board.is_game_over():
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ask the current player for their move
            move = self.current_player.get_move(self.board)

            # make the move on the board
            piece = self.board.get_piece(move.initial_pos)
            self.board.move_piece(piece, move.final_pos)

            # update the current player
            self.current_player = self.black_player if self.current_player == self.white_player else self.white_player

            # draw the game objects
            self.screen.blit(self.board_image, (0, 0))
            for row in range(8):
                for col in range(8):
                    piece = self.board.get_piece((row, col))
                    if piece is not None:
                        piece_image = self.pieces_image.subsurface(piece.image_rect)
                        self.screen.blit(piece_image, (col*64, row*64))

            # update the screen
            pygame.display.flip()

            # control the framerate
            self.clock.tick(FPS)

        # print the winner of the game
        winner = self.board.get_winner()
        if winner is None:
            print("The game ended in a draw.")
        else:
            print(f"The winner is {winner}.")

if __name__ == "__main__":
    game = ChessGame()
    game.run()
