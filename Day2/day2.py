def part1():
    with open('input2.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]

    opcodes[1] = 12
    opcodes[2] = 2

    index = 0
    while (opcode := opcodes[index]) != 99:
        if opcode == 1:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] + opcodes[opcodes[index + 2]]
            index += 4
        if opcode == 2:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] * opcodes[opcodes[index + 2]]
            index += 4

    print('Part 1 : {}'.format(opcodes[0]))


def part2():
    with open('input2.txt') as file:
        opcodesBase = [int(value) for value in file.readlines()[0].split(',')]

    for noun in range(100):
        for verb in range(100):
            opcodes = opcodesBase.copy()

            opcodes[1] = noun
            opcodes[2] = verb

            index = 0
            while (opcode := opcodes[index]) != 99:
                if opcode == 1:
                    opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] + opcodes[opcodes[index + 2]]
                    index += 4
                elif opcode == 2:
                    opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] * opcodes[opcodes[index + 2]]
                    index += 4
                else:
                    break

            if opcodes[0] == 19690720:
                print('Part 2 : {}'.format(100 * noun + verb))
                return



if __name__ == "__main__":
    part1()
    part2()
