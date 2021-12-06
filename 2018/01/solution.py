from itertools import cycle


def parse_data():
    with open('2018/01/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def part_one(data):
    return sum(data)


def part_two(data):
    frequencies = {0}
    frequency = 0
    for change in cycle(data):
        frequency += change

        if frequency in frequencies:
            return frequency

        frequencies.add(frequency)


def main():
    data = parse_data()

    print(f'Day 01 Part 01: {part_one(data)}')
    print(f'Day 01 Part 02: {part_two(data)}')
