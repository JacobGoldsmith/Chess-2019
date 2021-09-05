from pieces_classes import piece
from recursive_ai import recursive_ai
import copy
def aimove(boardobject, pieces_on_the_board, list_of_pieces_moved, color):
    depth_count = 1
    max_eval_and_index = recursive_ai(boardobject, pieces_on_the_board, list_of_pieces_moved, color, depth_count)
    res = False
    print(max_eval_and_index)
    x, y = max_eval_and_index[1]
    k, l = pieces_on_the_board[x].possible_destinations[y]
    res= pieces_on_the_board[x].make_move(k, l, boardobject, pieces_on_the_board, list_of_pieces_moved, color)
    return res