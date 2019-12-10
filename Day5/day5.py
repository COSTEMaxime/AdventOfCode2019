def main():
    with open('input5.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]

    pc = 0
    while (opcode := opcodes[pc]) != 99:
        # split, then look at the last digit
        if opcode % 100 == 1:
            # add
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            index = getIndexPositionMode(opcodes, pc, 3)
            opcodes[index] = operand1 + operand2
            # print('opcodes[{}] = {} + {}'.format(index, operand1, operand2))
            pc += 4
        elif opcode % 100 == 2:
            # mul
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            getIndexPositionMode(opcodes, pc, 3)
            opcodes[index] = operand1 * operand2
            # print('opcodes[{}] = {} * {}'.format(index, operand1, operand2))
            pc += 4
        elif opcode == 3:
            # in
            opcodes[opcodes[pc + 1]] = int(input('Input : '))
            pc += 2
        elif opcode % 10 == 4:
            # out
            print(getOperand(opcodes, pc, 1))
            pc += 2
        elif opcode % 100 == 5:
            # jmp nz
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            if operand1 != 0:
                pc = operand2
                # print('Jmp to {}'.format(operand2))
            else:
                pc += 3
        elif opcode % 100 == 6:
            # jmp z
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            if operand1 == 0:
                pc = operand2
                # print('Jmp to {}'.format(operand2))
            else:
                pc += 3
        elif opcode % 100 == 7:
            # jmp less than
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            if operand1 < operand2:
                opcodes[getIndexPositionMode(opcodes, pc, 3)] = 1
            else:
                opcodes[getIndexPositionMode(opcodes, pc, 3)] = 0
            pc += 4
        elif opcode % 100 == 8:
            # jmp eq
            operand1 = getOperand(opcodes, pc, 1)
            operand2 = getOperand(opcodes, pc, 2)
            if operand1 == operand2:
                opcodes[getIndexPositionMode(opcodes, pc, 3)] = 1
            else:
                opcodes[getIndexPositionMode(opcodes, pc, 3)] = 0
            pc += 4
        else:
            print('Unsupported opcode : {} at index {}'.format(opcode, pc))
            print(opcodes)
            break


def getOperand(opcodes, pc, offset):
    return opcodes[getIndexPositionMode(opcodes, pc, offset)]


def getIndexPositionMode(opcodes, pc, offset):
    if opcodes[pc] // 10**(offset + 1) % 10 == 0:
        return opcodes[pc + offset]
    else:
        return pc + offset


if _name_ == '_main_':
    main()