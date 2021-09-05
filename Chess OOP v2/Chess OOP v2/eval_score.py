from checkmate import checkmate
from value_of_piece import value_of_piece
def eval_score(boardobject, pieces_on_the_board, list_of_pieces_moved, color):
    if checkmate(boardobject, pieces_on_the_board, list_of_pieces_moved, color):
        return (-1000 if color=='black' else 1000)
    if len(list_of_pieces_moved)<5:
        pass
    evaluation = 0
    for pi in pieces_on_the_board:
        if pi.location[-1]!='off the board':
            if pi.color == 'white':
                color_bias = 1
            if pi.color == 'black':
                color_bias = -1
            evaluation += color_bias*value_of_piece(pi.name)
            if is_in_ecnter(pi.location[-1][0], pi.location[-1][1]):
                evaluation +=color_bias*2

    return [evaluation]


def is_in_ecnter(x, y):
    if x>1 and x<6 and y>1 and x<6:
        return True
