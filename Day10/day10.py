from math import gcd, atan2, degrees
from functools import cmp_to_key


def main():
    with open('input10.txt') as file:
        grid = [[char for char in line.strip()] for line in file.readlines()]

    resultPart1 = part1(grid)
    print('Part 1 : {}'.format(resultPart1))
    print('Part 2 : {}'.format(part2(grid, resultPart1[0][0], resultPart1[0][1])))


def part1(grid):
    results = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                results.append([(x, y), detect(grid, x, y)])

    return max(results, key=lambda x: x[1])


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
                gcd_ = gcd(distX, distY)
                if abs(gcd_) != 1:
                    for factor in range(abs(gcd_)):
                        if asteroidY + (distY // gcd_ * factor) == asteroidY and asteroidX + (distX // gcd_ * factor) == asteroidX:
                            continue
                        if grid[asteroidY + (distY // gcd_ * factor)][asteroidX + (distX // gcd_ * factor)] == '#':
                            canSee = False
                if canSee:
                    count += 1

    return count


def part2(grid, stationX, stationY):
    angles = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                if x == stationX and y == stationY:
                    pass
                angle = (90.0 + degrees(atan2(y - stationY, x - stationX))) % 360
                dist = abs(y - stationY + x - stationX)
                angles.append([(x, y), angle, dist])

    sortedAngles = sorted(angles, key=cmp_to_key(sort_))

    index = 0
    count = 0
    currentAngle = -1
    result = None
    while len(sortedAngles):
        index_ = index % len(sortedAngles)

        if sortedAngles[index_][1] != currentAngle:
            asteroid = sortedAngles.pop(index_)
            print('{} to be vaporized : {} - {}'.format(count, asteroid[0][0], asteroid[0][1]))
            if count == 200:
                result = asteroid[0][0] * 100 + asteroid[0][1]
            currentAngle = asteroid[1]
            count += 1
        else:
            index += 1
            if len(sortedAngles) and index_ == 0:
                currentAngle = -1

    return result


def sort_(a, b):
    if a[1] == b[1]:
        if a[2] > b[2]:
            return 1
        else:
            return -1
    elif a[1] > b[1]:
        return 1
    else:
        return -1


if __name__ == '__main__':
    main()
