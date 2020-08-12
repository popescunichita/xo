from helpers import *


class Player:
    def setSide(self, side):
        self.side = side

    def getName(self):
        return print(f'Your name is: {self.name}')

    def getSpot(self):
        while True:

            spot = input("Player, enter the spot: ")

            if not spot.isnumeric():
                print("Wrong input. Enter a number: ")
                continue

            spot = int(spot)

            if spot < 1 or spot > 9:
                print("Invalid input. Enter again: ")
                continue

            else:
                return spot

    def getNextMove(self, game_board):
        while True:
            spot = self.getSpot()
            pair = spots_map[spot]
            if game_board[pair[0]][pair[1]] == '-':
                return pair
            print("Place already filled!")

    def setName(self):
        self.name = input('Enter your name: ')

    def getSide(self):
        return self.side
