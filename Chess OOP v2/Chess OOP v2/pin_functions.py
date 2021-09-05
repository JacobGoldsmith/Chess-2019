from is_on_board import is_on_board
def enters_pin(piece, boardobject):
    #CHECK EVERY MOVED PIECE IF ALLIVIATES SOMEONE ELSE IN A PIN OR PUTS HIMSELF IN A PIN
    if boardobject.squares[piece.location[-1][0]][piece.location[-1][1]] not in\
    boardobject.Bpinned_squares | boardobject.Wpinned_squares:
        return False
    x, y = piece.location[-1]
    pi = None
    king = boardobject.pieces_list[1] if boardobject.squares[x][y] in boardobject.Bpinned_squares\
    else boardobject.pieces_list[0]
    advances = in_line_with_opp_king([x, y], king)
    for direction in [-1, 1]:
        i, j = x+advances[0]*direction, y+advances[1]*direction
        while [i, j]!=king.location[-1]:
            print(i, j, "from new func ENTERS")
            square = boardobject.squares[i][j]
            if square.piece and square.piece.color!=king.color and\
            associated_line_with_king(advances, square.piece.name.lower()):
                break
            if pi and square.piece:
                pi = False
                break
            elif square.piece and pi==None:
                pi = square.piece
            i, j = i+advances[0]*direction, j+advances[1]*direction
    return pi if pi != None else piece

def leaves_pin(piece, boardobject):
    #CHECK EVERY MOVED PIECE IF ABANDONED SOMEONE ELSE IN A PIN
    if boardobject.squares[piece.location[-2][0]][piece.location[-2][1]] not in\
    boardobject.Bpinned_squares | boardobject.Wpinned_squares:
        return False
    x, y = piece.location[-2]
    pi = None
    king = boardobject.pieces_list[1] if boardobject.squares[x][y] in boardobject.Bpinned_squares\
    else boardobject.pieces_list[0]
    advances = in_line_with_opp_king([x, y], king)
    for direction in [-1, 1]:
        i, j = x+advances[0]*direction, y+advances[1]*direction
        while [i, j]!=king.location[-1]:
            print(i, j, "from new func LEAVES")
            square = boardobject.squares[i][j]
            if square.piece and square.piece.color!=king.color and\
            associated_line_with_king(advances, square.piece.name.lower()):
                break
            if pi and square.piece:
                pi = False
                break
            elif square.piece and pi==None:
                pi = square.piece
            i, j = i+advances[0]*direction, j+advances[1]*direction
    return pi


def if_created_or_left_pin_save_squares(piece, boardobject):
    print("checking pins, created")
    oppking = boardobject.pieces_list[0] if piece.color == 'black' else boardobject.pieces_list[1]
    liadvances=[in_line_with_opp_king(piece.location[-2], oppking), in_line_with_opp_king(piece.location[-1], oppking)]
    for advances in range(2):
        liadvances[advances] = associated_line_with_king(liadvances[advances], piece.name.lower())
    if liadvances == [None, None]:
        return liadvances
    opp_pinned_squares = boardobject.Wpinned_squares if piece.color == 'black' else boardobject.Bpinned_squares
    pinned_pieces = [None, None]
    list_of_locations = [piece.location[-2], piece.location[-1]]
    for cnt in range(2):
        list_of_locations[cnt]= None if isinstance(list_of_locations[cnt], str) else list_of_locations[cnt]
    for xy, advances, idx in zip(list_of_locations, liadvances, range(2)):
        if xy == None:
            pinned_pieces[idx]=None
            continue
        else:
            x, y = xy
        if not advances:
            pinned_pieces[idx]=None
            continue
        i, j = x + advances[0], y + advances[1]
        while [i, j]!=oppking.location[-1]:
            square = boardobject.squares[i][j]
            if idx == 1:
                print("i am adding square", square.location, "to the list")
                opp_pinned_squares.add(square)
            else:
                opp_pinned_squares.remove(square)
            if pinned_pieces[idx] and square.piece:
                pinned_pieces[idx] = False
            elif square.piece and pinned_pieces[idx]!=False:
                pinned_pieces[idx]= square.piece
            i, j = i + advances[0], j + advances[1]
        if pinned_pieces[idx] and pinned_pieces[idx].color == piece.color:
            pinned_pieces[idx]=None
    return pinned_pieces

def in_line_with_opp_king(p, oppking):
    k_x, k_y = oppking.location[-1] 
    p_x, p_y = p
    if p_y==k_y:
        return [1, 0] if p_x<k_x else [-1, 0]
    if p_x==k_x:
        return [0, 1] if p_y<k_y else [0, -1]
    if (p_x-k_x)/(p_y-k_y)==1:
        return [1, 1] if (p_x-k_x)<0 else [-1, -1]
    if (p_x-k_x)/(p_y-k_y)==-1:
        return [1, -1] if (p_x-k_x)<0 else [-1, 1]
    return None
    
def associated_line_with_king(advances, name):
    if advances in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        if name in ('r', 'q'):
            return advances
    if advances in ([1, 1], [-1, 1], [-1, -1], [1, -1]):
        if name in ('b', 'q'):
            return advances
    return None