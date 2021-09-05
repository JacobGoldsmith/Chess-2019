from in_check import in_check
from undo_move import undo_move
from checkmate import checkmate 
from next_turn import next_turn
from pin_functions import if_created_or_left_pin_save_squares, in_line_with_opp_king\
, associated_line_with_king, enters_pin, leaves_pin
import sys
from is_on_board import is_on_board


class piece():

    def __init__(self, color, x, y):
        self.color=color
        self.location = []
        self.future_legal_moves = []
        self.possible_destinations = []
        self.location.append([x, y])
        self.name = '0'
        self.is_in_pin = False
    def update_possible_destinations(self, board_obj, pieces_on_the_board):
        print("this is update_possible_destinations method from father piece class")
    
    def update_for_pin(self, board_obj, pieces_on_the_board):
        print("the piece", self.name, "needs to be updated for it is in a PIN")
        new_pos = []
        my_king = pieces_on_the_board[0] if self.color=='white' else pieces_on_the_board[1]
        advances = in_line_with_opp_king(self.location[-1], my_king)
        # IF POS MOVE IS A MULTIPLE OF ADVANCE
        for move in self.possible_destinations:
            if in_line_with_opp_king(move, my_king) == advances:
                new_pos.append(move)
        self.possible_destinations = new_pos
    
    def make_move(self, k, l, boardobject, pieces_on_the_board, list_of_pieces_moved, turn):
        if self.location[-1]== 'off the board':
            return False
        moved_and_taken_piece_index = []
        new_set = set()
        result = True
        new_square = boardobject.squares[k][l]
        old_square = boardobject.squares[self.location[-1][0]][self.location[-1][1]]
        if (self in new_square.legal_moves) == False:
            print(self.name, "is trying to go to", k, l, "22 piecesclass")
            return False
        moved_and_taken_piece_index.append(self)
        if new_square.piece:
            new_square.piece.location.append('off the board')
            new_set.add(new_square.piece)
            moved_and_taken_piece_index.append(new_square.piece)
        for piece in new_square.future_legal_moves | new_square.legal_moves | old_square.future_legal_moves | old_square.legal_moves:
            new_set.add(piece)
        new_square.piece = old_square.piece
        old_square.piece = None

        self.location.append([k, l])

        #PROMOTING PAWN     ----- NEEDS ATTENTION!------ DON'T RETURN TO MAIN FOR PROMOTION
        if self.name.lower() == 'p':
            if k == 7 or k == 0: 
                self.location.pop()
                self.location.append('off the board')
                result = 'promotion'
        for squ in boardobject.Wpinned_squares:
            print(squ.location, "is a white pinned square")
        for squ in boardobject.Bpinned_squares:
            print (squ.location, "is a black pinned square")
            
        #IF QUEEN BISHOP OR ROOK CREATES OR LEAVES PIN:
        if self.name.lower() in ('b', 'r', 'q'):
            prev_pinned_piece, pinned_piece = if_created_or_left_pin_save_squares(self, boardobject)
            print(prev_pinned_piece, pinned_piece)
            if pinned_piece:
                pinned_piece.update_possible_destinations(boardobject, pieces_on_the_board)
                pinned_piece.update_for_pin(boardobject, pieces_on_the_board)
                pinned_piece.is_in_pin = True
            if prev_pinned_piece:
                prev_pinned_piece.is_in_pin = False
                prev_pinned_piece.update_possible_destinations(boardobject, pieces_on_the_board)
            if pinned_piece in new_set:
                new_set.remove(pinned_piece)

        #IF ANY PIECE ENTERS OR LEAVES EXISTING PIN:
        abandoned_piece = leaves_pin(self, boardobject)
        alleviated_piece = enters_pin(self, boardobject)
        print(abandoned_piece, alleviated_piece)
        if abandoned_piece:
            abandoned_piece.update_possible_destinations(boardobject, pieces_on_the_board)
            abandoned_piece.update_for_pin(boardobject, pieces_on_the_board)
            abandoned_piece.is_in_pin = True
        if alleviated_piece and alleviated_piece != self:
            alleviated_piece.update_possible_destinations(boardobject, pieces_on_the_board)
            alleviated_piece.is_in_pin = False
        elif alleviated_piece:
            alleviated_piece.update_possible_destinations(boardobject, pieces_on_the_board)
            alleviated_piece.update_for_pin(boardobject, pieces_on_the_board)
            alleviated_piece.is_in_pin = True
        if abandoned_piece in new_set:
            new_set.remove(abandoned_piece)
        if alleviated_piece in new_set:
            new_set.remove(alleviated_piece)


        #CASTLING
        castling = False
        if self.name.lower() == 'k':
            if self.name == 'k':
                if l-self.location[-2][1] == -2:   #CASTLING LEFT
                    cas_rook = pieces_on_the_board[6]
                    x, y = 0, 3
                    new_square = boardobject.squares[0][3]
                    old_square = boardobject.squares[0][0]
                    castling = True
                if l-self.location[-2][1] == 2: #CASTLING RIGHT
                    cas_rook = pieces_on_the_board[7]
                    x, y = 0, 5
                    new_square = boardobject.squares[0][5]
                    old_square = boardobject.squares[0][7]
                    castling = True
            if self.name == 'K':
                if l-self.location[-2][1] == -2: #CASTLING LEFT
                    cas_rook = pieces_on_the_board[4]
                    x, y = 7, 3
                    new_square = boardobject.squares[7][3]
                    old_square = boardobject.squares[7][0]
                    castling = True
                if l-self.location[-2][1] == 2: #CASTLING RIGHT
                    cas_rook = pieces_on_the_board[5]
                    x, y = 7, 5
                    new_square = boardobject.squares[7][5]
                    old_square = boardobject.squares[7][7]
                    castling = True
            if castling:
                cas_rook.location.append([x, y])
                new_square.piece = old_square.piece
                old_square.piece = None
                moved_and_taken_piece_index.append(cas_rook)
                new_set.add(cas_rook)

            result = True
        
        list_of_pieces_moved.append(moved_and_taken_piece_index)

        #UPDATING PIECES AFFECTED AND SEEING IF KING WAS AFFECTED
        wkingupdate, bkingupdate = False, False
        for piece in new_set:
            bkingupdate = True if piece.name == 'k' else bkingupdate
            wkingupdate = True if piece.name == 'K' else wkingupdate
            if piece.update_possible_destinations(boardobject, pieces_on_the_board) :
                # see if any update affected the opposing kings surrounding squares
                bkingupdate = True if piece.color == 'white' else bkingupdate
                wkingupdate = True if piece.color == 'black' else wkingupdate
        #update opposing king if neccesary
        if wkingupdate:
            pieces_on_the_board[0].update_possible_destinations(boardobject, pieces_on_the_board)
        if bkingupdate:
            pieces_on_the_board[1].update_possible_destinations(boardobject, pieces_on_the_board)
        return result


