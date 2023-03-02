import pygame
import sys
from board.board import Board
from pieces.piece import Piece
from players.human_player import HumanPlayer

# constants
WIDTH = 640
HEIGHT = 480
FPS = 30

# set up the game window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# load the images
board_image = pygame.image.load("board.png")
pieces_image = pygame.image.load("pieces.png")

# create the chess board and the players
board = Board()
white_player = HumanPlayer("white")
black_player = HumanPlayer("black")

# set up the game loop
clock = pygame.time.Clock()
current_player = white_player
while not board.is_game_over():
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ask the current player for their move
    move = current_player.get_move(board)

    # make the move on the board
    piece = board.get_piece(move.initial_pos)
    board.move_piece(piece, move.final_pos)

    # update the current player
    current_player = black_player if current_player == white_player else white_player

    # draw the game objects
    screen.blit(board_image, (0, 0))
    for row in range(8):
        for col in range(8):
            piece = board.get_piece((row, col))
            if piece is not None:
                piece_image = pieces_image.subsurface(piece.image_rect)
                screen.blit(piece_image, (col*64, row*64))

    # update the screen
    pygame.display.flip()

    # control the framerate
    clock.tick(FPS)

# print the winner of the game
winner = board.get_winner()
if winner is None:
    print("The game ended in a draw.")
else:
    print(f"The winner is {winner}.")
