from Block import Block
from Board import Board
from Enemy import Enemy
from Player import Player


# This class comes to use after the bomb has been set
class Explosion(Block):

    def __init__(self):
        bl = [['\033[1;33me\033[0m' for j in range(0, 4)] for i in range(0, 2)]
        super().__init__(bl)

    def explode(self, n, m):
        if Board.board[n][m] != 'X':
            # Explosion has no effect on wall
            if Board.board[n][m] == '\033[1;34m/\033[0m':
                # Explosion on brick destroys brick and scores 20 points
                Board.score = Board.score + 20
            for i in Enemy.instances:
                # Explosion on enemy kills enemy and scores 100 points
                if i.getPos() == [n, m]:
                    Board.score = Board.score + 100
                    Enemy.killEnemy(n, m)
            if Player.instance.getPos() == [n, m]:
                # Explosion on player kills player
                if Board.lives == 0:
                    Board.lives = Board.lives - 1
                    print("\t\tGame Over")
                    Player.killPlayer()
                else:
                    Board.lives = Board.lives - 1
                    Board.resetFlag = 1
            super().putBlock(Board.board, n, m)
        return

    def afterExplosion(self, n, m):
        if Board.board[n][m] != 'X':
            # Everything except walls is destroyed
            super().remBlock(Board.board, n, m)
        return
