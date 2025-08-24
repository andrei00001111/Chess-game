import Piece
import Side
class King(Piece):
    moves = []
    canCastle  = True
    def __init__(self, side:Side):
        self.moves = [[-1,-1], [-1,0], [-1, 1], [0,-1], [0,1], [1, -1], [1,0], [1,1]]
        self.canCastle = True
    def getCanCastle(self):
        return self.canCastle
    def reverseCastle(self):
        self.canCastle = not self.canCastle
    def getMoves(self):
        if self.canCastle:
            auxMoves = self.moves
            auxMoves.append([0,2], [0,-2])
            return auxMoves
        else: return self.moves
