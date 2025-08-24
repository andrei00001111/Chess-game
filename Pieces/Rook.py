import Piece
import Side
class Rook(Piece):
    moves = []
    def __init__(self, side:Side):
        self.side = side
        for i in range(1,8):
            self.moves.append([0,-i])
            self.moves.append([0,i])
            self.moves.append([-i,0])
            self.moves.append([i,0])
            