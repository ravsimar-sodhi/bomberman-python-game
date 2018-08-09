import sys
from Person import Person
from Enemy import Enemy
from Board import Board


class Player(Person):
    instance = ""

    def __init__(self):
        # The player block is set
        bl = [["\033[1;32mB\033[0m" for j in range(0, 4)]for i in (0, 2)]
        super().__init__(bl, [2, 4])
        Player.instance = self

    def move(self, board, dir):
        if dir != "stay":
            board = super().move(board, dir)
        # If the player has overlapped with an enemy, you lose the current game
        for i in Enemy.instances:
            if i.getPos() == self.getPos():
                if Board.lives == 0:
                    Board.lives = Board.lives - 1
                    print("\n\t\t    Game Over")
                    Player.killPlayer()
                else:
                    Board.lives = Board.lives - 1
                    Board.resetFlag = 1
        return board

    # To kill the player at the end of the game when all lives are lost
    @staticmethod
    def killPlayer():
        Player.instance = ""
        sys.exit(1)
