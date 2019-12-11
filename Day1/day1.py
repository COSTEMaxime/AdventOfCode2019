from math import floor


def main():
    with open('input1.txt') as file:
        lines = file.readlines()
        print('Part 1 : {}'.format(sum([part1(int(line.strip())) for line in lines])))
        print('Part 2 : {}'.format(sum([part2(int(line.strip())) for line in lines])))


def part1(mass):
    return floor(mass / 3) - 2


def part2(mass):
    fuel = 0
    while (mass := floor(mass / 3) - 2) > 0:
        fuel += mass
    return fuel


if __name__ == "__main__":
    main()
