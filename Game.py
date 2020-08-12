
from Board import *
from Player import *
from Machine import *


class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.machine = Machine()

    def initGame(self):
        self.player.setName()
        self.player.getName()
        self.board.initBoard()

        randomChoice = self.board.coinFlip()
        self.player.setSide(randomChoice)
        print("Player is with ", randomChoice)
        self.machine.setSide(getOpSide(randomChoice))

    def startGame(self):
        # if player is x then move
        if self.player.getSide() == 'X':
            spot = self.player.getNextMove(self.board.getGameBoard())
            print('Player chose', end='\n\n')
            self.board.applyMove(spot, self.player.getSide())
            self.board.gameBoard_status()
            print()

        while True:
            # machine moves
            spot = (self.machine.minimax(self.board.getGameBoard(), 0, self.machine.getSide())[0],
                    self.machine.minimax(self.board.getGameBoard(), 0, self.machine.getSide())[1])
            print('Machine chose', end='\n\n')
            self.board.applyMove(spot, self.machine.getSide())
            self.board.gameBoard_status()
            print()

            # test for end then break
            info = self.board.isOver()
            if info[0]:
                print(f'{info[1]} wins !')
                break

            # player moves
            spot = self.player.getNextMove(self.board.getGameBoard())
            print('Player chose', end='\n\n')
            self.board.applyMove(spot, self.player.getSide())
            self.board.gameBoard_status()
            print()

            # test for end then break
            info = self.board.isOver()
            if info[0]:
                print(f'{info[1]} wins !')
                break