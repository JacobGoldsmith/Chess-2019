def print_board(board_obj):
    number=8
    print (number, end='')
    number-=1
    print('|', end='')
    for i in range(8):
        
        for j in range(8):
            if board_obj.squares[i][j].piece:
                print (board_obj.squares[i][j].piece.name,'|', end='')
            else:
                print ('_ |', end='')
        print ('')
        if number != 0:
            print (number, end='')
            number -=1
            print('|', end='')
    letter=97
    while letter < 105:
        print(' ',chr(letter), end='')
        letter+=1
    print('')