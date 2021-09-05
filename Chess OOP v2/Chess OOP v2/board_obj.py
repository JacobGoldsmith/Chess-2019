from square import square
from pieces_classes import piece
from queen import queen
from rook import rook
from bishop import bishop
from knight import knight
class board_obj():
    def __init__(self, pieces_on_the_board):
        self.squares = [[square(j, i) for i in range(8)] for j in range(8)]
        self.pieces_list = pieces_on_the_board
        self.Bpinned_squares = set()
        self.Wpinned_squares = set()
        self.Bking_surrounding = set()
        self.Wking_surrounding = set()


        for pi in pieces_on_the_board:
            self.squares[pi.location[-1][0]][pi.location[-1][1]] = pi

