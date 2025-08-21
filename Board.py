import pygame
import Square
class Board:
    boardMap = []
    def createBoard(self, length = 8, width = 8):
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

    def getBoardState(self):
        return self.boardMap

    def showBoard(self):
        pass
                

