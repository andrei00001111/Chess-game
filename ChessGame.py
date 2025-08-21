import Board
import Side
import Player
class ChessGame:
    def __init__(self):
        self.gameBoard = Board()
        self.whitePoints = 0
        self.blackPoints = 0
        self.moves = []
        
    def makeMove(self, move, side:Side):
        isCastles = self.isMoveCastles(move)
        player = self.getPlayerFromMove(move)
        if(isCastles):
            self.gameBoard.makeCastle(move, side)
            return
        pieceType = self.getTypeFromMove(move)
        isCapture = self.isMoveCapture(move)
        inputSquare = self.getInputFromMove(move)
        outputSquare = self.getOutputFromMove(move)

        if isCapture:
            
            player.addPoints()
        
        self.gameBoard.putPieceInSquare(pieceType, outputSquare)
        self.gameBoard.putPieceInSquare()
        self.moves.append(move)

    def getPieceTypeFromMove(self,move):
        pass

    def inputGameFromFile(self, gamePath):
        pass
    
    def saveGameToFile(self):
        pass
    
    def restartGame (self):
        pass