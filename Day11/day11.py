import sys
sys.path.append('../Day9')

from day9 import Program


class Robot(Program):
    def __init__(self, opcodes):
        super().__init__(opcodes)
        self.x = 0
        self.y = 0
        self.direction = 0
        self.outputCount = 0

        self.board = Board()

    def getInput(self):
        return self.board.getColor(self.x, self.y)

    def output(self, value):
        if self.outputCount % 2:
            # up = 0, right = 1, ...
            self.direction += 1 if value else -1
            self.direction %= 4

            if self.direction == 0:
                self.y -= 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y += 1
            elif self.direction == 3:
                self.x -= 1
        else:
            self.board.paint(self.x, self.y, value)

        self.outputCount += 1


class Board:
    def __init__(self):
        # tile = {x, y, color}
        self.tiles = []

    def getTile(self, x, y):
        for tile in self.tiles:
            if tile['x'] == x and tile['y'] == y:
                return tile

        tile = {
            'x': x,
            'y': y,
            'color': 0
        }

        self.tiles.append(tile)
        return tile

    def getColor(self, x, y):
        return self.getTile(x, y)['color']

    def paint(self, x, y, color):
        # Return True if a new tile is created
        self.getTile(x, y)['color'] = color

    def outputInConsole(self):
        width = max(self.tiles, key=lambda x: x['x'])['x'] - min(self.tiles, key=lambda x: x['x'])['x'] + 1
        height = max(self.tiles, key=lambda x: x['y'])['y'] - min(self.tiles, key=lambda x: x['y'])['y'] + 1

        for y in range(height):
            for x in range(width):
                print(' ' if self.getColor(x, y) else u'\u2591', end='')
            print()


def main():
    with open('input11.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]
    robotPart1 = Robot(opcodes)
    robotPart1.compute()
    print('Part 1 : {}'.format(len(robotPart1.board.tiles)))

    robotPart2 = Robot(opcodes)
    robotPart2.board.paint(0, 0, 1)
    robotPart2.compute()
    robotPart2.board.outputInConsole()


if __name__ == "__main__":
    main()
