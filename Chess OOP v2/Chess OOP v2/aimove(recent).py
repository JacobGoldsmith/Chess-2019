def aimove(pieces_on_the_board, list_of_pieces_moved, color):
    import random
    from in_check import in_check
    from undo_move import undo_move
    from checkmate import checkmate
    from next_turn import next_turn
    from queen import queen
    from rook import rook
    from bishop import bishop
    from knight import knight
    from is_stalemate import is_stalemate
    import sys
    ilegal = True
    depth_count = 0
    piece_histogram = []
    coordinates_histogram = []
    if is_stalemate(pieces_on_the_board, list_of_pieces_moved, color):
        return 'stalemate'
    random_choice = True
    while ilegal:
        #FIND A MOVE
        while random_choice:
            piece = random.choice(pieces_on_the_board)
            if len(piece.possible_destinations) == 0:
                continue
            if piece.color !=color:
                continue
            coordinates = random.choice(piece.possible_destinations)
            

        #MAKE THE MOVE
        result = piece.make_move(coordinates[0], coordinates[1], pieces_on_the_board, list_of_pieces_moved)
        for piece1 in pieces_on_the_board:    #update all possible destinations
            piece1.possible_destinations.clear()
            if piece1.location[-1] != 'off the board':
                piece1.update_possible_destinations(pieces_on_the_board)
        #CHECK LEGALITY OF MOVE
        incheck_result = in_check(pieces_on_the_board)
        print(incheck_result, "23 aimove")
        if incheck_result == color or incheck_result == 'both':
            ilegal = True
            print(color, " computer you can't go there 26 aimove")
            if result == True:
                undo_move(pieces_on_the_board, list_of_pieces_moved)
            return False
        else:
            print("i'm not in check, 31 aimove")
            ilegal = False
            result = True
        if incheck_result == next_turn(color):
            if checkmate(pieces_on_the_board, list_of_pieces_moved, next_turn(color))==True:
                print("CHECKMATE HAHAHA 35 aimove")
                result = 'checkmate'
            else:
                print(next_turn(color), "you are in check!, 38 aimove")
        #PROMOTED PAWN
        if result == 'promotion':
            promotion_options = ['q', 'r', 'n', 'b']
            choice = random.choice(promotion_options)
            if choice == 'q': 
                promoted = queen(color, coordinates[0], coordinates[1])
            if choice == 'r': 
                promoted = rook(color, coordinates[0], coordinates[1])
            if choice == 'n': 
                promoted = knight(color, coordinates[0], coordinates[1])
            if choice == 'b': 
                promoted = bishop(color, coordinates[0], coordinates[1])
            pieces_on_the_board.append(promoted)
            pieces_on_the_board[-1].location.insert(0, 'off the board')
            list_of_pieces_moved[-1].append(pieces_on_the_board.index(pieces_on_the_board[-1]))
            result = True


    return result