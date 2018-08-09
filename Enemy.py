from Person import Person
import random
from Board import Board


class Enemy(Person):
    instances = []
    # current instances of every enemy are stored here
    allDir = ["right", "left", "up", "down"]
    # Possible directions the enemy may move

    def __init__(self, board, pos):
        self.dir = Enemy.allDir[random.randint(0, 3)]
        # A random direction is chosen initially
        bl = [["\033[1;31mE\033[0m" for j in range(0, 4)] for i in range(0, 2)]
        super().__init__(bl, pos)
        Enemy.instances.append(self)
        n = pos[0]
        m = pos[1]
        super().putBlock(board, n, m)

    def checkBlockEmpty(self, board, n, m):
        for i in range(0, 2):
            for j in range(0, 4):
                if (board[n+i][m+j] == '\033[1;33me\033[0m' or
                        board[n+i][m+j] == "\033[1;35m0\033[0m"):
                    return False
        return super().checkBlockEmpty(board, n, m)

    def moveRandom(self, board):
        # This function defines the random movement of the enemy
        Pos = self.getPos()
        n = Pos[0]
        m = Pos[1]
        N = n
        M = m
        k = 0
        while True:
            if (self.dir == "left"):
                N = n
                M = m-4
            elif (self.dir == "right"):
                N = n
                M = m+4
            elif (self.dir == "up"):
                N = n-2
                M = m
            elif (self.dir == "down"):
                N = n+2
                M = m
            if self.checkBlockEmpty(board, N, M) is True:
                # If enemy's current direction is feasible,Enemy will move
                self.pos = [N, M]
                board = super().remBlock(board, n, m)
                board = super().putBlock(board, N, M)
                return board
            # If enemy is trapped,  then enemy stays where it is
            elif (self.checkBlockEmpty(board, n, m-4) is False and
                    self.checkBlockEmpty(board, n, m+4) is False and
                    self.checkBlockEmpty(board, n+2, m) is False and
                    self.checkBlockEmpty(board, n-2, m) is False):
                return board
            # Enemy choses a random direction when can't move
            else:
                self.dir = Enemy.allDir[k]
                k = (k + 1) % 4
        return board

    @staticmethod
    def killEnemy(n, m):
        pos = [n, m]
        for i in Enemy.instances:
            if i.getPos() == pos:
                Enemy.instances.remove(i)
        return
