from math import gcd


def main():
    with open('input10.txt') as file:
        grid = [[char for char in line.strip()] for line in file.readlines()]

    results = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                results.append([(x, y), detect(grid, x, y)])

    print(max(results, key=lambda x: x[1]))


def detect(grid, asteroidX, asteroidY):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                if x == asteroidX and y == asteroidY:
                    continue

                canSee = True
                distX = x - asteroidX
                distY = y - asteroidY
                test = gcd(distX, distY)
                if abs(test) != 1:
                    for toto in range(abs(test)):
                        if asteroidY + (distY // test * toto) == asteroidY and asteroidX + (distX // test * toto) == asteroidX:
                            continue
                        if grid[asteroidY + (distY // test * toto)][asteroidX + (distX // test * toto)] == '#':
                            canSee = False
                if canSee:
                    count += 1

    return count


if _name_ == '_main_':
    main()