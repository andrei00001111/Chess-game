import Board
import Side
class PieceInterface:
    
    def Piece(self, letter: int, number:int, color:str, ):
        pass
    def showMoves(self):
        pass
    def getPosition(self):
        pass
    def getMoves(self):
        pass
    def move(self, board: Board, letter: str, number:int):
        pass
    