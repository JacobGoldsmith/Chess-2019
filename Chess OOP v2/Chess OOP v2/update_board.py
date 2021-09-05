def update_board(pieces_on_the_board, board):
    
    
    board= [['_' for i in range(8)] for j in range(8)]
    for i in pieces_on_the_board:
        if i.location[-1] != 'off the board':
            board[i.location[-1][0]][i.location[-1][1]] = i.name
    return board