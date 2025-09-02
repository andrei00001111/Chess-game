import Board
import Side
import Square
import Player
from Pieces import Pawn
from Pieces import Queen
from Pieces import King
from Pieces import Rook
from Pieces import Knight
from Pieces import Bishop
class ChessGame:
    def __init__(self):
        self.gameBoard = Board()
        self.whitePoints = 0
        self.blackPoints = 0
        self.moves = []
        
    def analyzeMove(self, move:str, side:Side):
        
        # Get Castles, capture
        if(move.find('O-O-O')):
            self.makeLongCastles(side)
        elif (move.find('O-O')):
            self.makeShortCastles(side)
        elif (move.find('x')):
            capture = True
        
        inputData = [0,0]
        outputData = [0,0]
        # pawn move
        if (move[0].islower):
            if(capture):
                outputData = self.moveToPos(move)
                inputData = outputData
                inputData[1] = inputData[1] - 1
                inputData[0] = ord(move[0])
            else:
                outputData = self.moveToPos(move[-2:])
                inputData = outputData
                inputData = outputData[1] - 1
        # Else normal move 
        else:
            outputMove = self.moveToPos(move)
    def makeInitPosition(self):
        for i in range(0,8):
            whitePawn = Pawn('White')
            blackPawn = Pawn('Black')
            self.gameBoard.putPieceInSquare(whitePawn, 1, i)
            self.gameBoard.putPieceInSquare(blackPawn, 6, i)
        
        whiteQueen = Queen('White')
        blackQueen = Queen('Black')
        self.gameBoard.putPieceInSquare(whiteQueen, 0, 3)
        self.gameBoard.putPieceInSquare(blackQueen, 7, 3)
        
        whiteKing = King('White')
        blackKing = King('Black')
        self.gameBoard.putPieceInSquare(whiteKing, 0, 4)
        self.gameBoard.putPieceInSquare(blackKing, 7, 4)

        for i in range (2):
            whiteKnight = Knight('White')
            blackKnight = Knight('Black')
            
            whiteRook = Rook('White')
            blackRook = Rook('Black')

            whiteBishop = Bishop('White')
            blackBishop = Bishop('Black')

            if i == 0:
                self.gameBoard.putPieceInSquare(whiteRook, 0, 0)
                self.gameBoard.putPieceInSquare(blackRook, 7, 0)

                self.gameBoard.putPieceInSquare(whiteKnight, 0, 1)
                self.gameBoard.putPieceInSquare(blackKnight, 7, 1)

                self.gameBoard.putPieceInSquare(whiteBishop, 0, 2)
                self.gameBoard.putPieceInSquare(blackBishop, 7, 2)

            elif i == 1:
                self.gameBoard.putPieceInSquare(whiteRook, 0, 7)
                self.gameBoard.putPieceInSquare(blackRook, 7, 7)

                self.gameBoard.putPieceInSquare(whiteKnight, 0, 6)
                self.gameBoard.putPieceInSquare(blackKnight, 7, 6)

                self.gameBoard.putPieceInSquare(whiteBishop, 0, 5)
                self.gameBoard.putPieceInSquare(blackBishop, 7, 5)



    def getInitSquare(self,move):
        pass

    def inputGameFromFile(self, gamePath):
        pass
    
    def saveGameToFile(self):
        pass
    
    def restartGame (self):
        pass
    
    def moveToPos(self, data:str):
        if (data.find('+')):
            data = data[-2:]
            data = data[0:2]
        else: data = data[-2:]
        data1 = data[0:1]
        data2 = data[1:2]

        letter = ord(data1) - ord('a')
        return [letter, int(data2)]