import pygame
import Square
import Piece
class Board:
    boardMap = []
    def __init__(self, length = 8, width = 8):
        self.length = length
        self.wdith = width
        for i in range(length):
            widthMap = []
            for j in range(width):
                if (i + j) % 2  == 0:
                    color = 'Black'
                else: color = 'White'
                square = Square(board = self, letter = j, number = i, color = color)
                widthMap.append(square)
            self.boardMap.append(widthMap)

    def getPieceFromSquare(self, length, width):
        return self.boardMap[length][width].getPiece()
    

    def putPieceInSquare(self, piece:Piece, length, width):
        self.boardMap[length][width].putPiece(piece)

    def getBoardState(self):
        return self.boardMap

    # TODO: Show the board with pygame
    def showBoard(self):
        pass
                

