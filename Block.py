# This class is the parent class of almost all objects
# Since every object is of 2x4 size


class Block:

    def __init__(self, bl):
        self.bl = bl

    # This saves us putting every object into the matrix manually
    def putBlock(self, board, n, m):
        for i in range(0, 2):
            for j in range(0, 4):
                board[n+i][m+j] = self.bl[i][j]
        return board

    # This resets a block e.g after an explosion ,  when a block moves
    def remBlock(self, board, n, m):
        for i in range(0, 2):
            for j in range(0, 4):
                board[n+i][m+j] = ' '
        return board

    # Checks if a block does not have walls or bricks
    # Child classes override this method according to their convenience
    def checkBlockEmpty(self, board, n, m):
        for i in range(0, 2):
            for j in range(0, 4):
                if(board[n+i][m+j] == 'X' or
                        board[n+i][m+j] == '\033[1;34m/\033[0m'):
                    return False
        return True
