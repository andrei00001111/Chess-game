import Piece
import Side
class Knight(Piece):
    moves = []
    def __init__(self, side:Side):
        self.side = side
        self.moves = [[2,1], [2,-1], [-2,1], [-2,-1], [-1,-2], [-1,2], [1,-2], [1,2]]
    def getMoves(self):
        return self.moves

