import Piece
import Side
class Bishop(Piece):
    moves = []
    def __init__(self, side:Side):
        self.side = side
        for i in range(1,8):
            self.moves.append([i,i])
            self.moves.append([-i,-i])
            self.moves.append([i,-i])
            self.moves.append([-i,i])
    def getMoves(self):
        return self.moves

