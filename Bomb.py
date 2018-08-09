from threading import Timer
from Block import Block
from Board import Board
from Explosion import Explosion


class Bomb(Block):

    def __init__(self):
        self.pos = []
        self.set = 0
        self.timer = 3
        bl = [["\033[1;35m0\033[0m" for j in range(0, 4)] for i in range(0, 2)]
        super().__init__(bl)

    def setBomb(self, board, pos):
        if self.set == 1:
            return board
        self.set = 1
        self.pos = pos
        n = pos[0]
        m = pos[1]
        super().putBlock(board, n, m)
        # Bomb is set to explode after the timer runs out
        t = Timer(2, self.explodeBomb, [Board.lives])
        t.start()
        return board

    def afterExpl(self):    # clears up the exploded blocks
        n = self.pos[0]
        m = self.pos[1]
        expl = Explosion()
        expl.afterExplosion(n, m)
        expl.afterExplosion(n-2, m)
        expl.afterExplosion(n+2, m)
        expl.afterExplosion(n, m+4)
        expl.afterExplosion(n, m-4)
        self.set = 0
        return

    def explodeBomb(self, life):
        n = self.pos[0]
        m = self.pos[1]
        if life != Board.lives:
            return
        expl = Explosion()
        expl.explode(n, m)
        expl.explode(n-2, m)
        expl.explode(n+2, m)
        expl.explode(n, m+4)
        expl.explode(n, m-4)
        if Board.lives >= 0:
            # The explosion is shown for 1 second
            t = Timer(1, self.afterExpl)
            t.start()
        return
