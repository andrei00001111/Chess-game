class Side:
    def __init__(self, side):
        if side == 'Black':
            self.side = 1
        elif side == 'White':
            self.side = 0
        else: raise Exception(f"Sides can only be 'Black' or 'White', but {side} was given")
    def getSide(self):
        if self.side == 1:
            return 'Black'
        else:
            return 'White'