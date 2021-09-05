from in_check import in_check
from undo_move import undo_move
import time
def checkmate(boardobject, pieces_on_the_board, list_of_pieces_moved, color):
    '''
    for piece in pieces_on_the_board:
        if piece.color == color:
            for coordinates in piece.possible_destinations:
                moveresult = piece.make_move(coordinates[0], coordinates[1], pieces_on_the_board, list_of_pieces_moved)
                if moveresult == False:
                    continue
                for piece1 in pieces_on_the_board:    #update all other colors possible destinations
                    if piece1.location[-1] != 'off the board' and piece1 != color:
                        piece1.possible_destinations.clear()
                        piece1.update_possible_destinations(pieces_on_the_board)
                incheckresult = in_check(pieces_on_the_board) 
                if incheckresult != color and incheckresult != 'both':
                    print("not checkmate 18 checkmate")
                    undo_move(pieces_on_the_board, list_of_pieces_moved)
                    return False
                undo_move(pieces_on_the_board, list_of_pieces_moved)
    '''
    return False