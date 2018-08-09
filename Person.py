from Block import Block


# This is the parent class of Player and Enemy
class Person(Block):

    def __init__(self, bl, pos):
        super().__init__(bl)
        self.pos = pos

    def getPos(self):
        # To get the current position of an instance of Player
        return self.pos

    def move(self, board, dir):
        n = self.pos[0]
        m = self.pos[1]
        if (dir == "left"):
            N = n
            M = m-4
        elif (dir == "right"):
            N = n
            M = m+4
        elif (dir == "up"):
            N = n-2
            M = m
        elif (dir == "down"):
            N = n+2
            M = m
        if (super().checkBlockEmpty(board, N, M) and
                board[N][M] != "\033[1;35m0\033[0m"):
            self.pos = [N, M]
        if (board[n][m] == '\033[1;32mB\033[0m' or
                board[n][m] == '\033[1;31mE\033[0m'):
            board = super().remBlock(board, n, m)
            board = super().putBlock(board, N, M)
        return board

    @staticmethod
    def kill(n, m):
        pos = [n, m]
        for i in self.instances:
            if i.getPos() == pos:
                self.instances.remove(i)
        return
