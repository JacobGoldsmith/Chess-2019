from pieces_classes import piece
from is_on_board import is_on_board
class king(piece):
    def __init__(self, color, x, y):
        piece.__init__(self, color, x, y)
#    white_name = "\u2654"
#    black_name = "\u265A"
        if color == 'black':
            self.name = 'k'
        if color == 'white':
            self.name = 'K'
    def update_possible_destinations(self, board_obj, pieces_on_the_board):
        print("updating", self.name)
        mySurroundingSquares = board_obj.Bking_surrounding if self.color=='black' else board_obj.Wking_surrounding
        mySurroundingSquares.clear()
        for x, y in self.possible_destinations+ self.future_legal_moves:
            board_obj.squares[x][y].legal_moves.discard(self)
            board_obj.squares[x][y].future_legal_moves.discard(self)
        self.possible_destinations.clear()
        self.future_legal_moves.clear()
        if self.location[-1] == 'off the board':
            return
        directions = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,1], [-1,0], [-1,-1]]
        for i, j in directions:
            x, y = self.location[-1][0] + i, self.location[-1][1] + j
            #CHECK IF THE LOCATION IS ON BOARD
            if is_on_board([x, y])==False:
                continue
            square = board_obj.squares[x][y]
            mySurroundingSquares.add(square)
            #APPEND POTENTIAL POSSIBLE DESTINATIONS
            self.possible_destinations.append([x, y])
            square.legal_moves.add(self)
            #CHECK IF LOCATION IS OCCUPIED 
            if square.piece != None:
                self.future_legal_moves.append([x, y])
                square.future_legal_moves.add(self)
                if square.piece.color == self.color:
                    self.possible_destinations.pop()
                    square.legal_moves.discard(self)
                    continue
            #CHECK IF KING IS IN CHECK IF SO ELIMINATING THAT LEGAL MOVE
            imprint_list = square.legal_moves | square.future_legal_moves
            for threats in imprint_list:
                if threats.color != self.color:
                    self.possible_destinations.pop()
                    square.legal_moves.discard(self)
                    if threats.name.lower() in ('b', 'r', 'q'):
                        x, y = self.location[-1][0] - i, self.location[-1][1] - j
                        try:
                            self.possible_destinations.remove([x, y])
                            board_obj.squares[x][y].legal_moves.discard(self)
                        except:
                            pass
                            
                    

        #CASTLING
        castle_to_the_left = ([self.location[-1][0], self.location[-1][1] - 1], [self.location[-1][0], self.location[-1][1] - 2])
        castle_to_the_right = ([self.location[-1][0], self.location[-1][1] + 1], [self.location[-1][0], self.location[-1][1] + 2])
        if len(self.location) == 1:
            if self.color == 'black':
                rook_1 = pieces_on_the_board[6]
                rook_2 = pieces_on_the_board[7]
            if self.color == 'white':
                rook_1 = pieces_on_the_board[4]
                rook_2 = pieces_on_the_board[5]
            if len(rook_1.location) == 1:
                result = True
                for castles in castle_to_the_left:
                    if board_obj.squares[castles[0]][castles[1]].piece!= None:
                        result = False
                    imprint_list = board_obj.squares[castles[0]][castles[1]].legal_moves
                    if next((x for x in imprint_list if x.color!=self.color), None)!= None:
                        result = False
                if result:
                    self.possible_destinations.append(castle_to_the_left[1])
                    board_obj.squares[castle_to_the_left[1][0]][castle_to_the_left[1][1]].legal_moves.add(self)

            if len(rook_2.location) == 1:
                result = True
                for castles in castle_to_the_right:
                    if board_obj.squares[castles[0]][castles[1]].piece!= None:
                        result = False
                    imprint_list = board_obj.squares[castles[0]][castles[1]].legal_moves
                    if next((x for x in imprint_list if x.color!=self.color), None)!= None:
                        result = False
                if result:
                    self.possible_destinations.append(castle_to_the_right[1])
                    board_obj.squares[castle_to_the_right[1][0]][castle_to_the_right[1][1]].legal_moves.add(self)