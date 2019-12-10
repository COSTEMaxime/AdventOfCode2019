def parse(line):
    parsedInput = [[0, 0]]
    index = 0

    for token in line.split(','):
        direction = token[0]

        previousPath = parsedInput[index]
        parsedToken = previousPath.copy()
        if direction == 'U':
            parsedToken[0] += int(token[1:])
        elif direction == 'D':
            parsedToken[0] -= int(token[1:])
        elif direction == 'R':
            parsedToken[1] += int(token[1:])
        elif direction == 'L':
            parsedToken[1] -= int(token[1:])
        parsedInput.append(parsedToken)
        index += 1
    return parsedInput


def main():
    # Path represents the coordinates of each turn of the wire
    # path1 = R8,U5,L5,D3 = [[0, 0], [0, 8], [5, 8], [5, 3], [2, 3]]
    # path2 = U7,R6,D4,L4 = [[0, 0], [7, 0], [7, 6], [3, 6], [3, 2]]

    # I tried to solve the first part without using a 2 dimentional array to represent the data. (It's messy don't judge me)

    with open('input3.txt') as file:
        lines = file.readlines()

    wirePath1 = parse(lines[0])
    wirePath2 = parse(lines[1])
    part1 = []
    part2 = []

    prevCoordPath2 = [0, 0]
    path2Dist = 0

    for currentIndexPath2 in range(1, len(wirePath2)):
        currentCoordPath2 = wirePath2[currentIndexPath2]
        path2Dist += abs(currentCoordPath2[0] - prevCoordPath2[0]) + abs(currentCoordPath2[1] - prevCoordPath2[1])

        prevCoordPath1 = [0, 0]
        path1Dist = 0
        if wirePath2[currentIndexPath2][0] == prevCoordPath2[0]:
            # same y coordinate (horizontal line)
            for currentIndexPath1 in range(1, len(wirePath1)):
                currentCoordPath1 = wirePath1[currentIndexPath1]
                path1Dist += abs(currentCoordPath1[0] - prevCoordPath1[0]) + abs(currentCoordPath1[1] - prevCoordPath1[1])
                # if path1 x is within path2 x and previous path2 x
                # and if path2 y is within path1 y and previous path1 y
                if ((prevCoordPath2[1] < currentCoordPath1[1] < currentCoordPath2[1] or prevCoordPath2[1] > currentCoordPath1[1] > currentCoordPath2[1]) and
                   (prevCoordPath1[0] < currentCoordPath2[0] < currentCoordPath1[0] or prevCoordPath1[0] > currentCoordPath2[0] > currentCoordPath1[0])):
                    part1.append(abs(currentCoordPath2[0]) + abs(currentCoordPath1[1]))

                    diff = abs(currentCoordPath2[1] - currentCoordPath1[1]) + abs(currentCoordPath2[0] - currentCoordPath1[0])
                    part2.append(path1Dist + path2Dist - diff)
                prevCoordPath1 = wirePath1[currentIndexPath1]
        else:
            # same x coordinate (vertical line)
            for currentIndexPath1 in range(1, len(wirePath1)):
                currentCoordPath1 = wirePath1[currentIndexPath1]
                path1Dist += abs(currentCoordPath1[0] - prevCoordPath1[0]) + abs(currentCoordPath1[1] - prevCoordPath1[1])
                # same as above but but with x and y szapped
                if ((prevCoordPath2[0] < currentCoordPath1[0] < currentCoordPath2[0] or prevCoordPath2[0] > currentCoordPath1[0] > currentCoordPath2[0]) and
                   (prevCoordPath1[1] < currentCoordPath2[1] < currentCoordPath1[1] or prevCoordPath1[1] > currentCoordPath2[1] > currentCoordPath1[1])):
                    part1.append(abs(currentCoordPath1[0]) + abs(currentCoordPath2[1]))

                    diff = abs(currentCoordPath2[1] - currentCoordPath1[1]) + abs(currentCoordPath2[0] - currentCoordPath1[0])
                    part2.append(path1Dist + path2Dist - diff)
                prevCoordPath1 = wirePath1[currentIndexPath1]

        prevCoordPath2 = wirePath2[currentIndexPath2]

    print('Part 1 : {}'.format(min(part1)))
    print('Part 2 : {}'.format(min(part2)))


if _name_ == '_main_':
    main()