import re
from itertools import combinations
from math import gcd


def main():
    moons = []
    with open('input12.txt') as file:
        for line in file.readlines():
            tokens = re.findall("[-+]?[0-9]+", line.strip())

            moons.append({
                'posx': int(tokens[0]),
                'posy': int(tokens[1]),
                'posz': int(tokens[2]),
                'velx': 0,
                'vely': 0,
                'velz': 0
            })

    steps = 1000
    print('Part 1 : {}'.format(part1(moons, steps)))
    print('Part 2 : {}'.format(part2(moons, steps)))


def part1(moons, steps):
    for step in range(steps):
        for pair in combinations(range(len(moons)), 2):
            moon0 = moons[pair[0]]
            moon1 = moons[pair[1]]
            for axis in ['x', 'y', 'z']:
                if moon0['pos' + axis] < moon1['pos' + axis]:
                    moon0['vel' + axis] += 1
                    moon1['vel' + axis] -= 1
                elif moon0['pos' + axis] > moon1['pos' + axis]:
                    moon0['vel' + axis] -= 1
                    moon1['vel' + axis] += 1

        for moon in moons:
            for axis in ['x', 'y', 'z']:
                moon['pos' + axis] += moon['vel' + axis]

    totalEnergy = 0
    for moon in moons:
        pot = abs(moon['posx']) + abs(moon['posy']) + abs(moon['posz'])
        kin = abs(moon['velx']) + abs(moon['vely']) + abs(moon['velz'])
        totalEnergy += pot * kin

    return totalEnergy


def part2(moons, steps):
    periods = []
    for axis in ['x', 'y', 'z']:
        test = False
        count = 0
        while not test:
            for pair in combinations(range(len(moons)), 2):
                moon0 = moons[pair[0]]
                moon1 = moons[pair[1]]
                diff = 1 if moon0['pos' + axis] < moon1['pos' + axis] else -1 if moon0['pos' + axis] > moon1['pos' + axis] else 0
                moon0['vel' + axis] += diff
                moon1['vel' + axis] -= diff

            test = True
            for index in range(len(moons)):
                moons[index]['pos' + axis] += moons[index]['vel' + axis]
                if moons[index]['vel' + axis] != 0 or moons[index]['pos' + axis] != moons[index]['pos' + axis]:
                    test = False
            count += 1
        print('Period axis {} : {}'.format(axis, (count + steps) * 2))
        periods.append((count + steps) * 2)

    result = 1
    for period in periods:
        result = lcm(period, result)

    return result


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    main()
