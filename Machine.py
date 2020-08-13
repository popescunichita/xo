from helpers import *
from Board import *


class Machine():

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

    def minimax(self, board, depth, side):

        info = board.isOver()
        if info[0]:
            # is a draw
            if info[1] == None:
                return (-1, -1, 0)
            # won game
            if info[1] == side:
                return (-1, -1, 1)
            else:
                # lost game
                return (-1, -1, -1)

        bestValue = -1
        row = -1
        col = -1

        # Traverse all cells, evaluate minimax function for all empty cells.And return the cell with optimal value.
        for i in range(len(board.game_board)):
            for j in range(len(board.game_board)):
                # Check if the cell is empty
                if board.game_board[i][j] == '-':
                    # Make the move
                    board.game_board[i][j] = side

                    # Compute evaluation function for this move
                    fromRec = self.minimax(board, depth + 1, getOpSide(side))

                    scoreFromRec = -fromRec[2]
                    # If the value of the current move is better than best value update best
                    if scoreFromRec >= bestValue:
                        row = i
                        col = j
                        bestValue = scoreFromRec

                    # Undo the move
                    board.game_board[i][j] = '-'

        return (row, col, bestValue)

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side
