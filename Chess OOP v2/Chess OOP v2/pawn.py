from pieces_classes import piece
from is_on_board import is_on_board
class pawn(piece):
    def __init__(self, color, x, y):
        piece.__init__(self, color, x, y)
#    white_name = "\u2659"
#    black_name = "\u265F"
        if color == 'black':
            self.name = 'p'
        if color == 'white':
            self.name = 'P'
    def update_possible_destinations(self, board_obj, pieces_on_the_board):
        print("updating", self.name)
        updateking = False
        oppKingSquares = board_obj.Wking_surrounding if self.color == 'black' else board_obj.Bking_surrounding
        for x, y in self.possible_destinations+ self.future_legal_moves:
            if board_obj.squares[x][y] in oppKingSquares:
                    updateking = True
            board_obj.squares[x][y].legal_moves.discard(self)
            board_obj.squares[x][y].future_legal_moves.discard(self)
        self.possible_destinations.clear()
        self.future_legal_moves.clear()
        if self.location[-1] == 'off the board':
            return
        x = self.location[-1][0]
        y = self.location[-1][1]
        if self.color.lower() == 'black':
            if board_obj.squares[x + 1][y].piece == None: #if no one is in front of this pawn
                self.possible_destinations.append([x + 1, y])   #Black pawn wants to go up one
                board_obj.squares[x + 1][y].legal_moves.add(self)
                if x == 1 and board_obj.squares[x + 2][y].piece == None:
                    self.possible_destinations.append([x + 2, y])   #Black pawn wants to go up two
                    board_obj.squares[x + 2][y].legal_moves.add(self)
                elif x==1:
                    self.future_legal_moves.append([x + 2, y])
                    board_obj.squares[x + 2][y].future_legal_moves.add(self)
            else:
                self.future_legal_moves.append([x + 1, y])
                board_obj.squares[x + 1][y].future_legal_moves.add(self)
            
            #Black pawn wants to take a piece to its right
            if is_on_board([x + 1, y +1]):
                updateking = True if board_obj.squares[x+1][y+1] in oppKingSquares else updateking
                board_obj.squares[x + 1][y +1].future_legal_moves.add(self)
                taking_piece = board_obj.squares[x + 1][y +1].piece
                if taking_piece != None and taking_piece.color != self.color:
                    self.possible_destinations.append([x + 1, y +1]) 
                    board_obj.squares[x + 1][y +1].legal_moves.add(self)
                else:
                    self.future_legal_moves.append([x + 1, y + 1])
                    board_obj.squares[x + 1][y + 1].future_legal_moves.add(self)


            #Black pawn wants to take a piece to its left
            if is_on_board([x + 1, y -1]):
                updateking = True if board_obj.squares[x+1][y-1] in oppKingSquares else updateking
                board_obj.squares[x + 1][y -1].future_legal_moves.add(self)
                taking_piece = board_obj.squares[x + 1][y -1].piece
                if taking_piece != None and taking_piece.color != self.color:
                    self.possible_destinations.append([x + 1, y -1]) 
                    board_obj.squares[x + 1][y -1].legal_moves.add(self)
                else:
                    self.future_legal_moves.append([x + 1, y - 1])
                    board_obj.squares[x + 1][y - 1].future_legal_moves.add(self)

        if self.color.lower() == 'white':
            if board_obj.squares[x - 1][y].piece == None: #if no one is in front of this pawn
                self.possible_destinations.append([x - 1, y])   #white pawn wants to go up one
                board_obj.squares[x - 1][y].legal_moves.add(self)
                if x == 6 and board_obj.squares[x - 2][y].piece == None:
                    self.possible_destinations.append([x - 2, y])   #white pawn wants to go up two
                    board_obj.squares[x - 2][y].legal_moves.add(self)
                elif x == 6:
                    self.future_legal_moves.append([x - 2, y])
                    board_obj.squares[x - 2][y].future_legal_moves.add(self)
            else:
                self.future_legal_moves.append([x - 1, y])
                board_obj.squares[x - 1][y].future_legal_moves.add(self)
            
            #white pawn wants to take a piece to its right
            if is_on_board([x - 1, y +1]):
                updateking = True if board_obj.squares[x-1][y+1] in oppKingSquares else updateking
                board_obj.squares[x - 1][y +1].future_legal_moves.add(self)
                taking_piece = board_obj.squares[x - 1][y +1].piece
                if taking_piece != None and taking_piece.color != self.color:
                    self.possible_destinations.append([x - 1, y +1]) 
                    board_obj.squares[x - 1][y +1].legal_moves.add(self)
                else:
                    self.future_legal_moves.append([x - 1, y + 1])
                    board_obj.squares[x - 1][y + 1].future_legal_moves.add(self)

            #white pawn wants to take a piece to its left
            if is_on_board([x - 1, y -1]):
                updateking = True if board_obj.squares[x-1][y-1] in oppKingSquares else updateking
                board_obj.squares[x - 1][y -1].future_legal_moves.add(self)
                taking_piece = board_obj.squares[x - 1][y -1].piece
                if taking_piece != None and taking_piece.color != self.color:
                    self.possible_destinations.append([x - 1, y -1]) 
                    board_obj.squares[x - 1][y -1].legal_moves.add(self)
                else:
                    self.future_legal_moves.append([x - 1, y - 1])
                    board_obj.squares[x - 1][y - 1].future_legal_moves.add(self)
        return updateking