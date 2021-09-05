def find_piece(pieces_on_the_board, x, y):
    for piece in pieces_on_the_board:
        if piece.location[-1] == [x, y]:
            return piece