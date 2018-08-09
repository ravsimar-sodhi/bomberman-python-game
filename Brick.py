import random
from Block import Block


class Brick(Block):

    def __init__(self):
        bl = [["\033[1;34m/\033[0m" for j in range(0, 4)]for i in (0, 2)]
        super().__init__(bl)
    
    def checkBlockEmpty(self, board, n, m):
        for i in range(0, 2):
            for j in range(0, 4):
                if board[n+i][m+j] == "\033[1;32mB\033[0m":
                    return False 
        return super().checkBlockEmpty(board, n, m)
    
    def placeRandom(self, board, n):
        row = []
        col = []
        for t in range(0, n):
            row.append(random.randint(1, 15)*2)
            col.append(random.randint(1, 15)*4)
        for i in range(0, n):
            if self.checkBlockEmpty(board, row[i], col[i]):
                board = super().putBlock(board, row[i], col[i])
        return board
