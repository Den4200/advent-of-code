from collections import defaultdict


def parse_data():
    with open('2021/03/input.txt') as f:
        data = f.read()

    return len(data.splitlines()[0]), [int(binary, 2) for binary in data.splitlines()]


def part_one(data):
    binary_length, data = data

    bits = defaultdict(int)
    for binary in data:
        for i in range(12):
            bits[i] += 1 if binary & (1 << (binary_length - 1) >> i) > 0 else 0

    gamma = 0
    for i, amt in bits.items():
        if amt >= len(data) >> 1:
            gamma |= 1 << (binary_length - 1) >> i

    return gamma * (gamma ^ 2 ** binary_length - 1)


def gas_filter(binary_length, data, compare_func):
    for i in range(12):
        ones = sum(binary & (1 << (binary_length - 1) >> i) > 0 for binary in data)

        bit_compare = int.__gt__ if compare_func(ones, len(data) - ones) else int.__eq__
        data = [binary for binary in data if bit_compare(binary & (1 << (binary_length - 1) >> i), 0)]

        if len(data) == 1:
            break

    return data[0]


def part_two(data):
    return gas_filter(*data, int.__ge__) * gas_filter(*data, int.__lt__)


def main():
    data = parse_data()

    print(f'Day 03 Part 01: {part_one(data)}')
    print(f'Day 03 Part 02: {part_two(data)}')
