from itertools import product


def parse_data():
    with open('2019/02/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.split(",")]


class Computer:

    def __init__(self, program):
        self.memory = program.copy()
        self.instruction_pointer = 0

        self.instructions = {
            1: self.op_1,
            2: self.op_2,
            99: None,
        }

    def read(self, address=None):
        if address is None:
            address = self.instruction_pointer
            self.instruction_pointer += 1

        return self.memory[address]

    def write(self, value, address=None):
        if address is None:
            address = self.instruction_pointer

        self.memory[address] = value

    def op_1(self):
        x = self.read(self.read())
        y = self.read(self.read())

        self.write(x + y, self.read())

    def op_2(self):
        x = self.read(self.read())
        y = self.read(self.read())

        self.write(x * y, self.read())

    def execute(self):
        while True:
            op = self.read()

            if (instruction := self.instructions[op]) is not None:
                instruction()
            else:
                break


def part_one(data):
    data[1] = 12
    data[2] = 2

    computer = Computer(data)
    computer.execute()

    return computer.memory[0]


def part_two(data):
    for x, y in product(range(100), repeat=2):
        data[1] = x
        data[2] = y

        computer = Computer(data)
        computer.execute()

        if computer.memory[0] == 19690720:
            return 100 * x + y


def main():
    data = parse_data()

    print(f'Day 02 Part 01: {part_one(data)}')
    print(f'Day 02 Part 02: {part_two(data)}')
