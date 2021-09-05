def in_check(boardobject, pieces_on_the_board):
    result = 'not in check'
    a, b = pieces_on_the_board[0].location[-1][0], pieces_on_the_board[0].location[-1][1] #white king
    c, d = pieces_on_the_board[1].location[-1][0], pieces_on_the_board[1].location[-1][1] #black king
    for piece in boardobject.squares[a][b].legal_moves:
        if piece.color == 'black':
            if result == 'black':
                result = 'both'
            else:
                result = 'white'
            break
    for piece in boardobject.squares[c][d].legal_moves:
        if piece.color == 'white':
            if result == 'white':
                result = 'both'
            else:
                result = 'black'
            break
    return result