import Side
import Piece
class Pawn(Piece):
    moves = []
    def __init__(self, side:Side):
        self.side = side
        if self.side.getSide() == 'Black':
            self.moves = [[-1,0], [-1,-1], [-1,1]]
        else:
            self.moves = [[1,0], [1,-1], [1,1]]
        self.canMoveTwice = True

    def getMoves(self):
        if not self.canMoveTwice:
            return self.moves
        auxMoves = self.moves
        if (self.side.getSide == 'Black'):
            auxMoves.append([-2,0])
        else:
            auxMoves.append([2,0])
        return auxMoves
    
    def reverMoveTwice(self):
        self.canMoveTwice = not self.canMoveTwice