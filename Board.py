import random


class Board:
    def __init__(self):
        self.game_board = []
        self.initBoard()

    def initBoard(self):
        self.game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def coinFlip(self):
        return random.choice(['X', '0'])

    def gameBoard_status(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                print(self.game_board[i][j], end=' ')
            print()

    def getGameBoard(self):
        return self.game_board

    def applyMove(self, spot, side):
        self.game_board[spot[0]][spot[1]] = side

    def checkLine(self, line):
        if self.game_board[line][0] == 'X' and self.game_board[line][1] == 'X' and self.game_board[line][2] == 'X':
            return True, 'X'

        if self.game_board[line][0] == '0' and self.game_board[line][1] == '0' and self.game_board[line][2] == '0':
            return True, '0'

        return False, None

    def checkLines(self):
        for i in range(len(self.game_board)):
            info = self.checkLine(i)
            if info[0]:
                return info
        return False, None

    def checkColumn(self, column):
        if self.game_board[0][column] == 'X' and self.game_board[1][column] == 'X' and self.game_board[2][
            column] == 'X':
            return (True, 'X')

        if self.game_board[0][column] == '0' and self.game_board[1][column] == '0' and self.game_board[2][
            column] == '0':
            return (True, '0')

        return False, None

    def checkColumns(self):
        for i in range(len(self.game_board)):
            info = self.checkColumn(i)
            if info[0]:
                return info
        return False, None

    def checkDiagonals(self):
        # main
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == 'X' and self.game_board[0][0] != '-':
            return True, 'X'
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == '0' and self.game_board[0][
            0] != '-':
            return True, '0'
        # second
        if self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2] == 'X' and self.game_board[0][
            2] != '-':
            return True, 'X'
        if self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2] == '0' and self.game_board[0][
            2] != '-':
            return True, '0'
        return False, None

    def checkDraw(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if self.game_board[i][j] == '-':
                    return (False, None)
        return (True, None)

    def isOver(self):
        info = self.checkLines()
        if info[0]:
            return info

        info = self.checkColumns()
        if info[0]:
            return info

        info = self.checkDiagonals()
        if info[0]:
            return info

        info = self.checkDraw()
        if info[0]:
            return info

        return info
