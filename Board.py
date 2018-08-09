import time


# This class holds the matrix which displays all objects of the game
# It also holds the score and time of the game
class Board:
    startTime = round(time.time())
    board = [[' ' for j in range(0, 68)] for i in range(0, 34)]
    score = 0
    lives = 2
    resetFlag = 0

    @staticmethod
    def printBoard():
        print()
        print()
        print()
        print("\t\t\t    BOMBERMAN")

        for i in range(0, 34):
            for j in range(0, 68):
                print(Board.board[i][j], end='')
            print()
        print("   Time: ", end='')
        print(180-(round(time.time())-Board.startTime), end='')
        print("\t\t   Score: ", end='')
        print(Board.score, end='')
        print("\t\tLives Left: ", end='')
        print(Board.lives)
        return Board.board

    @staticmethod
    def getTime():
        return 180-(round(time.time())-Board.startTime)
