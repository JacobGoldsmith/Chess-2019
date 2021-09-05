def undo_move(boardobject, pieces_on_the_board, list_of_pieces_moved):
    if len(list_of_pieces_moved) == 0:
        return False
    new_set = set()
    for piece in list_of_pieces_moved[-1]:
        new_set.add(piece)
        for square in [piece.location[-1], piece.location[-2]]:
            if isinstance(square, list):
                for pi in boardobject.squares[square[0]][square[1]].future_legal_moves:
                    new_set.add(pi)
                for pi in boardobject.squares[square[0]][square[1]].legal_moves:
                    if pi in new_set:
                        continue
                    new_set.add(pi)
        if isinstance(piece.location[-1], str):
            piece.location.pop()
            boardobject.squares[piece.location[-1][0]][piece.location[-1][1]].piece = piece
        elif isinstance(piece.location[-1], list):
            if isinstance(piece.location[-2], list):
                boardobject.squares[piece.location[-1][0]][piece.location[-1][1]].piece = None
                piece.location.pop()
                boardobject.squares[piece.location[-1][0]][piece.location[-1][1]].piece = piece
            else:
                boardobject.squares[piece.location[-1][0]][piece.location[-1][1]].piece = None
                piece.location.pop()
                pieces_on_the_board.pop()
                del piece
    list_of_pieces_moved.pop()
    for piece in new_set:
        print(piece.name, piece.possible_destinations, "is being updated from undo")
        piece.update_possible_destinations(boardobject, pieces_on_the_board)
    return True