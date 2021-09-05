def next_turn(turn):
    if turn.lower()== 'black':
        return 'white'
    if turn.lower()== 'white':
        return 'black'