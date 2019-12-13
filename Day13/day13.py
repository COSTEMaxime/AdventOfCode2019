import sys
sys.path.append('../Day9')

from time import sleep
from day9 import Program


class Game(Program):
    def __init__(self, opcodes):
        super().__init__(opcodes)
        self.outputBuffer = []
        self.gameBoard = GameBoard()
        self.score = 0

    def getInput(self):
        sleep(.02)
        self.gameBoard.printInConsole()
        if self.gameBoard.xball > self.gameBoard.xpaddle:
            return 1
        elif self.gameBoard.xball < self.gameBoard.xpaddle:
            return -1
        else:
            return 0

    def output(self, value):
        self.outputBuffer.append(value)
        if len(self.outputBuffer) % 3 == 0:
            x = self.outputBuffer[0]
            y = self.outputBuffer[1]
            value = self.outputBuffer[2]

            if x == -1 and y == 0:
                self.score = value
            else:
                char = ' ' if value == 0 else '|' if value == 1 else u'\u2591' if value == 2 else '-' if value == 3 else 'o'
                self.gameBoard.setTile(x, y, char)
            self.outputBuffer = []


class GameBoard:
    def __init__(self):
        # tile = {x, y, type}
        self.board = [[]]

        self.xball = 0
        self.xpaddle = 0

    def setTile(self, x, y, type_):
        if x >= len(self.board[0]):
            for line in self.board:
                line.extend([' '] * (x - len(self.board[0]) + 1))

        if y >= len(self.board):
            for index in range(len(self.board), y + 1):
                self.board.append([' '] * len(self.board[0]))

        if type_ == 'o':
            self.xball = x

        if type_ == '-':
            self.xpaddle = x

        self.board[y][x] = type_

    def getTilesCountByType(self, type_):
        count = 0
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == type_:
                    count += 1
        return count

    def printInConsole(self):
        text = ''
        for line in self.board:
            text += ''.join(line) + '\n'

        print(text, end='\r')


def main():
    with open('input13.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]

    gamePart1 = Game(opcodes)
    gamePart1.compute()

    gamePart2 = Game(opcodes)
    gamePart2.opcodes[0] = 2
    gamePart2.compute()
    print('Part 1 : {}'.format(gamePart1.gameBoard.getTilesCountByType(u'\u2591')))
    print('Part 2 : {}'.format(gamePart2.score))


if __name__ == '__main__':
    main()
