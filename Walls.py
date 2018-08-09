from Block import Block


class Walls(Block):
    def __init__(self):
        bl = [['X' for j in range(0, 4)] for i in range(0, 2)]
        super().__init__(bl)

    def buildWalls(self, board):
        # Sets the walls on the boundary of the board and alternate blocks
        j = 0
        while j < 68:
            super().putBlock(board, 0, j)
            super().putBlock(board, 32, j)
            j = j + 4
        i = 2
        while i < 32:
            super().putBlock(board, i, 0)
            super().putBlock(board, i, 64)
            i = i + 2
        i = 4
        while i < 30:
            j = 8
            while j < 60:
                super().putBlock(board, i, j)
                j = j + 8
            i = i + 4
        return board
