def value_of_piece(name):
    name = name.lower()
    if name == 'p':
        return 1
    if name == 'r':
        return 5
    if name == 'n':
        return 3
    if name == 'b':
        return 3
    if name == 'q':
        return 9
    return 0
        