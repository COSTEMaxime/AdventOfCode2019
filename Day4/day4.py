def main():
    countPart1 = 0
    countPart2 = 0

    for password in range(353096, 843212):
        parsedPassword = [int(x) for x in str(password)]
        if validatePart1(parsedPassword):
            countPart1 += 1
        if validatePart2(parsedPassword):
            countPart2 += 1

    print('Part 1 : {}'.format(countPart1))
    print('Part 2 : {}'.format(countPart2))


def validatePart1(password):
    double = False
    prev = 0
    for x in password:
        if x < prev:
            return False
        if x == prev:
            double = True

        prev = x

    return double


def validatePart2(password):
    prev = 0
    for x in password:
        if x < prev:
            return False
        prev = x

    index = 0
    while index < len(password) - 1:
        count = 0
        while index < len(password) - 1 and password[index] == password[index + 1]:
            count += 1
            index += 1
        if count == 1:
            return True

        index += 1

    return False


if __name__ == '__main__':
    main()
