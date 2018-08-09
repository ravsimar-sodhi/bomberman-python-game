import time
import os
import random
from threading import Timer
from Walls import Walls
from Brick import Brick
from Board import Board
from Player import Player
from Bomb import Bomb
from Enemy import Enemy
from getchunix import *
from Block import Block


b = Block(0)


# This function helps in random placement of enemys
def placeRandom():
    col = (random.randint(1, 15) * 4)
    row = (random.randint(1, 15) * 2)
    while b.checkBlockEmpty(Board.board, row, col) is False:
        random.seed(time.time())
        row = (random.randint(1, 15) * 2)
        col = (random.randint(1, 15) * 4)
    return [row, col]


# This function moves Enemy after one second
def moveEnemy(x=0):
    t = Timer(1, moveEnemy)
    if len(Enemy.instances) == 0 or x == 1 or Board.lives < 0:
        # If no enemy exists, or the game is over, This thread is cancelled
        t.cancel()
    t.start()
    for i in Enemy.instances:
        Board.board = i.moveRandom(Board.board)
    return


# This functions builds the board again in case life is lost
def setBoard():
    walls = Walls()
    bricks = Brick()
    player = Player()
    bmb = Bomb()
    Enemy.instances = []    # Previous game's Enemies are destroyed
    Board.board = [[' ' for j in range(0, 68)] for i in range(0, 34)]
    Board.board = walls.buildWalls(Board.board)
    Board.board = player.putBlock(Board.board, 2, 4)
    Board.board = bricks.placeRandom(Board.board, 15)
    # New Enemies are created here
    enemy1 = Enemy(Board.board, placeRandom())
    enemy2 = Enemy(Board.board, placeRandom())
    enemy3 = Enemy(Board.board, placeRandom())
    return [player, bmb]

f = 0


class Game:
    Board.resetFlag = 1
    while True:
        if Board.lives < 0:
            Enemy.instances = []
            break
        if Board.resetFlag == 1:    # If board needs to be reset
            state = setBoard()
            player = state[0]
            bmb = state[1]
            if f == 0:
                moveEnemy()
                # moveEnemy is called only on the first setting of the board
                f = 1
            Board.resetFlag = 0
            Board.startTime = round(time.time())
            # The time of the game is reset
        ch = getInput()
        if ch == 'd':
            Board.board = player.move(Board.board, "right")
        elif ch == 'a':
            Board.board = player.move(Board.board, "left")
        elif ch == 's':
            Board.board = player.move(Board.board, "down")
        elif ch == 'w':
            Board.board = player.move(Board.board, "up")
        elif ch == 'b':
            pos = player.getPos()
            Board.board = bmb.setBomb(Board.board, pos)
        elif ch == 'q':
            os._exit(1)
        else:
            Board.board = player.move(Board.board, "stay")
        if Board.getTime() <= 0:    # If the time runs out in the game
            if Board.lives == 0:
                    Board.lives = Board.lives - 1
                    os._exit(1)
            else:
                Board.lives = Board.lives - 1
                Board.resetFlag = 1
        # The game is displayed by printing the board from the Board class
        Board.printBoard()

# An instance of the game in created
game = Game()
