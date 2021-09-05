import random
from in_check import in_check
from undo_move import undo_move
from checkmate import checkmate
from next_turn import next_turn
from queen import queen
from rook import rook
from bishop import bishop
from knight import knight
from is_stalemate import is_stalemate
from best_eval_score import best_eval_score
import sys
from next_turn import next_turn
from print_board import print_board
from update_board import update_board
from eval_score import eval_score
import copy
'''
Tasks: 
Optimize with every level evals.
Optimize the code for efficiency using squares
'''
def recursive_ai(boardobject, pieces_on_the_board, list_of_pieces_moved, color, depth_count):

    #DEPTH CONDITION
    if depth_count >3:
        #GIVE EVALUATION SCORE
        return eval_score(boardobject, pieces_on_the_board, list_of_pieces_moved, color)
    #MAKE MOVE, RECURSIVE RETURN MAX EVAL SCORE, UNDO MOVE
    # if depth_count != 1:
    histogram = []
    for piece in pieces_on_the_board:
        if piece.color!=color:
            histogram.append('not my color')
            continue
        if piece.location[-1]=='off the board':
            histogram.append('illegal')
            continue
        if len(piece.possible_destinations)!= 0:
            histogram.append([0 for i in piece.possible_destinations])

        else:
            histogram.append('illegal')
    #MAKE MOVE
    for x in range(len(histogram)):
        if isinstance(histogram[x], str):
            continue
        piece = pieces_on_the_board[x]
        for y in range(len(histogram[x])):
            if isinstance(histogram[x][y], str):
                continue
            if isinstance(piece.possible_destinations[y], list):
                k, l = piece.possible_destinations[y]
            else:
                continue
            move_result = piece.make_move(k, l, boardobject, pieces_on_the_board, list_of_pieces_moved, color)
            # print_board(boardobject)
            #PROMOTED PAWN
            if move_result == 'promotion':
                promotion_options = ['q', 'r', 'n', 'b']
                choice = random.choice(promotion_options)
                if choice == 'q': 
                    promoted = queen(color, k, l)
                if choice == 'r': 
                    promoted = rook(color, k, l)
                if choice == 'n': 
                    promoted = knight(color, k, l)
                if choice == 'b': 
                    promoted = bishop(color, k, l)
                pieces_on_the_board.append(promoted)
                pieces_on_the_board[-1].location.insert(0, 'off the board')
                list_of_pieces_moved[-1].append(pieces_on_the_board[-1])
                a, b = pieces_on_the_board[-1].location[-1][0], pieces_on_the_board[-1].location[-1][1]
                boardobject.squares[a][b].piece = pieces_on_the_board[-1]
                boardobject.squares[a][b].piece.update_possible_destinations(boardobject, pieces_on_the_board)
            color_bias = -1 
            if color == 'white':
                color_bias = 1
            if move_result == 'checkmate':
                histogram[x][y] = color_bias*1000
                depth_count = 4
                continue
            #RECURSIVE CALL
            histogram[x][y]+=recursive_ai(boardobject, pieces_on_the_board, list_of_pieces_moved, next_turn(color), depth_count+1)[0]
            #UNDO MOVE
            if move_result==True:
                undo_move(boardobject, pieces_on_the_board, list_of_pieces_moved)

    #RETURNING THE MAX EVAL SCORE
    return  best_eval_score(histogram, color)

    # I want this to return the max and an index



#        if is_stalemate(pieces_on_the_board, list_of_pieces_moved, color):
#            return 'stalemate'
