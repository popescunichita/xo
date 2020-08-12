from helpers import *
from Board import *


class Machine(Board):

    # def getSpot(self):
    #     while True:
    #
    #         spot = input("Machine, enter the spot: ")
    #
    #         if not spot.isnumeric():
    #             print("Wrong input. Enter a number: ")
    #             continue
    #
    #         spot = int(spot)
    #
    #         if spot not in range(1, 10):
    #             print("Invalid input. Enter again: ")
    #             continue
    #
    #         else:
    #             return spot
    #
    # def getNextMove(self, game_board):
    #
    #     while True:
    #         spot = self.getSpot()
    #         pair = spots_map[spot]
    #         if game_board[pair[0]][pair[1]] == '-':
    #             return pair
    #         print('Place already filled!')

    def evaluate(self, side):
        # check for not ended
        if self.checkDraw() == (False, None):
            return None
        # check for draw
        if self.checkDraw() == (True, None):
            return 0
        # check who wins
        if self.checkLines() == (True, side):
            return 1
        if self.checkColumns() == (True, side):
            return 1
        return -1

    def movesLeft(self, game_board):
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if game_board[i][j] == '-':
                    return False
        return True

    def minimax(self, game_board, depth, side):
        # check for draw and return (-1, -1, 0)
        if self.evaluate(side) == 0:
            return -1, -1, 0
        # check for ending and return (-1, -1, {max = 1,min = -1})
        if self.evaluate(side) == 1:
            return -1, -1, 1
        if self.evaluate(side) == -1:
            return -1, -1, -1
        if depth == 9 or self.movesLeft(game_board):
            return -1, -1, 0

        bestValue = -1
        row = -1
        col = -1

        # Traverse all cells, evaluate minimax function for all empty cells.And return the cell with optimal value.
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                # Check if the cell is empty
                if game_board[i][j] == '-':
                    # Make the move
                    game_board[i][j] = side

                    # Compute evaluation function for this move
                    fromRec = self.minimax(game_board, depth + 1, getOpSide(side))

                    scoreFromRec = -fromRec[2]
                    # If the value of the current move is better than best value update best
                    if scoreFromRec >= bestValue:
                        row = i
                        col = j
                        bestValue = scoreFromRec

                    # Undo the move
                    game_board[i][j] = '-'

        return (row, col, bestValue)

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side