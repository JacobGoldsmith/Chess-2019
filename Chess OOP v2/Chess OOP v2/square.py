class square():
    def __init__(self, x, y):
        self.legal_moves = set()
        self.future_legal_moves = set()
        self.location = [x, y]
        self.piece = None
    

