from pieces_classes import piece
from is_on_board import is_on_board
class bishop(piece):
    def __init__(self, color, x, y):
        piece.__init__(self, color, x, y)
        if color == 'black':
            self.name = 'b'
        if color == 'white':
            self.name = 'B'
    def set_up_piece(self, x, y):
        self.location.append([x, y])

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
        directions = [[-1, -1],[-1, 1],[1, -1],[1, 1]]
        for i, j in directions:
            x = self.location[-1][0] + i
            y = self.location[-1][1] + j
            while is_on_board([x, y]):
                if board_obj.squares[x][y] in oppKingSquares:
                        updateking = True
                self.possible_destinations.append([x, y])
                board_obj.squares[x][y].legal_moves.add(self)
                if board_obj.squares[x][y].piece != None:
                    board_obj.squares[x][y].future_legal_moves.add(self)
                    self.future_legal_moves.append([x, y])
                    if board_obj.squares[x][y].piece.color == self.color:
                        self.possible_destinations.pop()
                        board_obj.squares[x][y].legal_moves.discard(self)
                    break
                x += i
                y +=j
        return updateking