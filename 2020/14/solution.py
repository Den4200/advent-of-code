import itertools
import re


def parse_data():
    with open('2020/14/input.txt') as f:
        data = f.read()

    mem = dict()

    previous = None
    values = list()
    for line in data.splitlines():

        if match := re.fullmatch(r'mask = (.+)', line):
            if previous is not None:
                mem[previous] = values

            previous = match[1]
            values = list()

        elif match := re.fullmatch(r'mem\[(\d+)\] = (\d+)', line):
            values.append([int(num) for num in match.groups()])

    mem[previous] = values
    return mem


def part_one(data):
    mem = dict()

    for mask, values in data.items():
        for addr, value in values:
            result = 0

            for i in range(36):
                bit = mask[-i - 1]

                b = 1 << i
                if bit == 'X' and (value & b) > 0 or bit == '1':
                    result |= b

            mem[addr] = result

    return sum(mem.values())


def part_two(data):
    mem = dict()

    for mask, values in data.items():
        for addr, value in values:
            result = 0

            bits = list()
            for i in range(36):
                bit = mask[-i - 1]

                b = 1 << i
                if bit == 'X':
                    bits.append(b)
                elif bit == '1' or (addr & b) > 0:
                    result += b

            for r in range(len(bits) + 1):
                for bs in itertools.combinations(bits, r=r):
                    mem[sum(bs) + result] = value

    return sum(mem.values())


def main():
    data = parse_data()

    print(f'Day 14 Part 01: {part_one(data)}')
    print(f'Day 14 Part 02: {part_two(data)}')
