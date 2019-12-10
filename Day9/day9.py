class Program():
    def __init__(self, opcodes):
        self.opcodes = opcodes.copy()
        self.pc = 0
        self.base = 0

    def compute(self, inputs=None):
        while (opcode := self.opcodes[self.pc]) != 99:
            if opcode % 100 == 1:
                # add
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                self.memset(3, operand1 + operand2)
                # print('opcodes[{}] = {} + {}'.format(index, operand1, operand2))
                self.pc += 4
            elif opcode % 100 == 2:
                # mul
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                self.memset(3, operand1 * operand2)
                # print('opcodes[{}] = {} * {}'.format(index, operand1, operand2))
                self.pc += 4
            elif opcode % 100 == 3:
                # in
                self.memset(1, inputs.pop() if inputs else int(input('Enter value : ')))
                self.pc += 2
            elif opcode % 10 == 4:
                # out
                value = self.memget(1)
                self.pc += 2
                print('Output : {}'.format(value))
            elif opcode % 100 == 5:
                # jmp nz
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                if operand1 != 0:
                    self.pc = operand2
                    # print('Jmp to {}'.format(operand2))
                else:
                    self.pc += 3
            elif opcode % 100 == 6:
                # jmp z
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                if operand1 == 0:
                    self.pc = operand2
                    # print('Jmp to {}'.format(operand2))
                else:
                    self.pc += 3
            elif opcode % 100 == 7:
                # jmp less than
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                if operand1 < operand2:
                    self.memset(3, 1)
                else:
                    self.memset(3, 0)
                self.pc += 4
            elif opcode % 100 == 8:
                # jmp eq
                operand1 = self.memget(1)
                operand2 = self.memget(2)
                if operand1 == operand2:
                    self.memset(3, 1)
                else:
                    self.memset(3, 0)
                self.pc += 4
            elif opcode % 100 == 9:
                # base
                self.base += self.memget(1)
                self.pc += 2
                # print('Base {}'.format(self.base))
            else:
                print('Unsupported opcode : {} at index {}'.format(opcode, self.pc))
                print(self.opcodes)
                break

        print('Done')

    def memset(self, offset, value):
        positionMode = self.opcodes[self.pc] // 10**(offset + 1) % 10
        if positionMode == 0:
            index = self.opcodes[self.pc + offset]
        elif positionMode == 2:
            index = self.opcodes[self.pc + offset] + self.base

        try:
            self.opcodes[index] = value
        except IndexError:
            if index < 0:
                raise
            else:
                self.opcodes.extend([0] * (index - len(self.opcodes) + 1))
                return self.memset(offset, value)

    def memget(self, offset):
        positionMode = self.opcodes[self.pc] // 10**(offset + 1) % 10
        if positionMode == 0:
            index = self.opcodes[self.pc + offset]
        elif positionMode == 1:
            index = self.pc + offset
        elif positionMode == 2:
            index = self.base + self.opcodes[self.pc + offset]

        try:
            return self.opcodes[index]
        except IndexError:
            if index < 0:
                raise
            else:
                self.opcodes.extend([0] * (index - len(self.opcodes) + 1))
                return self.memget(offset)


def main():
    with open('input9.txt') as file:
        opcodes = [int(value) for value in file.readlines()[0].split(',')]
    program = Program(opcodes)
    program.compute()


if _name_ == '_main_':
    main()