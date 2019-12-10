from itertools import permutations


class Program():
    def __init__(self, opcodes):
        self.opcodes = opcodes.copy()
        self.pc = 0

    def compute(self, inputs):
        while (opcode := self.opcodes[self.pc]) != 99:
            # split, then look at the last digit
            if opcode % 100 == 1:
                # add
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                index = getIndexPositionMode(self.opcodes, self.pc, 3)
                self.opcodes[index] = operand1 + operand2
                # print('opcodes[{}] = {} + {}'.format(index, operand1, operand2))
                self.pc += 4
            elif opcode % 100 == 2:
                # mul
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                index = getIndexPositionMode(self.opcodes, self.pc, 3)
                self.opcodes[index] = operand1 * operand2
                # print('opcodes[{}] = {} * {}'.format(index, operand1, operand2))
                self.pc += 4
            elif opcode == 3:
                # in
                self.opcodes[self.opcodes[self.pc + 1]] = inputs.pop()
                self.pc += 2
            elif opcode % 10 == 4:
                # out
                value = getOperand(self.opcodes, self.pc, 1)
                self.pc += 2
                return value
            elif opcode % 100 == 5:
                # jmp nz
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                if operand1 != 0:
                    self.pc = operand2
                    # print('Jmp to {}'.format(operand2))
                else:
                    self.pc += 3
            elif opcode % 100 == 6:
                # jmp z
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                if operand1 == 0:
                    self.pc = operand2
                    # print('Jmp to {}'.format(operand2))
                else:
                    self.pc += 3
            elif opcode % 100 == 7:
                # jmp less than
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                if operand1 < operand2:
                    self.opcodes[getIndexPositionMode(self.opcodes, self.pc, 3)] = 1
                else:
                    self.opcodes[getIndexPositionMode(self.opcodes, self.pc, 3)] = 0
                self.pc += 4
            elif opcode % 100 == 8:
                # jmp eq
                operand1 = getOperand(self.opcodes, self.pc, 1)
                operand2 = getOperand(self.opcodes, self.pc, 2)
                if operand1 == operand2:
                    self.opcodes[getIndexPositionMode(self.opcodes, self.pc, 3)] = 1
                else:
                    self.opcodes[getIndexPositionMode(self.opcodes, self.pc, 3)] = 0
                self.pc += 4
            else:
                print('Unsupported opcode : {} at index {}'.format(opcode, self.pc))
                print(self.opcodes)
                break

        return None


def main():
    with open('input7.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]

    # part1(opcodes)
    part2(opcodes)


def part1(opcodes):
    thrustLevels = []
    for p in permutations([0, 1, 2, 3, 4]):
        previousOutput = 0
        program = Program(opcodes)
        for x in p:
            previousOutput = program.compute([previousOutput, x])

        thrustLevels.append(previousOutput)
    print(max(thrustLevels))


def part2(opcodes):
    thrustLevels = []
    for p in permutations([5, 6, 7, 8, 9]):
        programs = [Program(opcodes) for x in p]

        previousOutput = 0
        for x in p:
            previousOutput = programs[x - 5].compute([previousOutput, x])

        index = 0
        lastValidOutput = None
        while previousOutput is not None:
            lastValidOutput = previousOutput
            previousOutput = programs[p[index % len(p)] % len(p)].compute([previousOutput])
            index += 1

        thrustLevels.append(lastValidOutput)
    print(max(thrustLevels))


def getOperand(opcodes, pc, offset):
    return opcodes[getIndexPositionMode(opcodes, pc, offset)]


def getIndexPositionMode(opcodes, pc, offset):
    if opcodes[pc] // 10**(offset + 1) % 10 == 0:
        return opcodes[pc + offset]
    else:
        return pc + offset


if _name_ == '_main_':
    main()