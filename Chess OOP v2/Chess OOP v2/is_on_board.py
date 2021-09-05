def is_on_board(x):
    if x[0] > 7 or \
    x[0] < 0 or \
    x[1] > 7 or \
    x[1] < 0:
        return False
    return True