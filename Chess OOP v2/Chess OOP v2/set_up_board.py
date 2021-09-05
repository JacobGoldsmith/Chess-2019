from pieces_classes import piece
from rook import rook
from knight import knight
from bishop import bishop
from pawn import pawn
from king import king
from queen import queen
from board_obj import board_obj
def set_up(board_obj, pieces_on_the_board):
    pieces_on_the_board.append(king('white', 7, 4)) #0
    pieces_on_the_board.append(king('black', 0, 4)) #1
    pieces_on_the_board.append(queen('white', 7, 3)) #2
    pieces_on_the_board.append(queen('black', 0, 3)) #3
    pieces_on_the_board.append(rook('white', 7, 0)) #4 
    pieces_on_the_board.append(rook('white', 7, 7)) #5 
    pieces_on_the_board.append(rook('black', 0, 0)) #6 
    pieces_on_the_board.append(rook('black', 0, 7)) #7
    pieces_on_the_board.append(knight('white', 7, 1))
    pieces_on_the_board.append(knight('white', 7, 6))
    pieces_on_the_board.append(knight('black', 0, 1))
    pieces_on_the_board.append(knight('black', 0, 6))
    pieces_on_the_board.append(bishop('white', 7, 2))
    pieces_on_the_board.append(bishop('white', 7, 5))
    pieces_on_the_board.append(bishop('black', 0, 2))
    pieces_on_the_board.append(bishop('black', 0, 5))
    for i in range(8):
        pieces_on_the_board.append(pawn('white', 6, i))
    for i in range(8):
        pieces_on_the_board.append(pawn('black', 1, i))
    for piece in pieces_on_the_board:
        board_obj.squares[piece.location[-1][0]][piece.location[-1][1]].piece = piece 
    for piece in pieces_on_the_board:   # updating pieces possible destinations
        piece.update_possible_destinations(board_obj, pieces_on_the_board)