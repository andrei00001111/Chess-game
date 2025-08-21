import Board
import Piece
class Square:
    def __init__(self, board:Board, letter: int, number:int, color:str):
        self.board = board
        self.letter = letter
        self.number = number
        self.heldPiece = 0
        if color == 'White' or color == 'Black':
            self.color = color
        else: raise Exception("Color should be 'White' or 'Black', but got {color}")
    
    def holdPiece(self, piece:Piece):
        self.heldPiece = piece
    def makeSquare(self, board:Board, letter:str, number:int, color:str):
        pass


