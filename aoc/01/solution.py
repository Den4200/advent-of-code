import itertools


def parse_data():
    with open('aoc/01/input.txt') as f:
        data = f.read()

    return [int(n) for n in data.splitlines()]


def part_one(data):
    for x, y in itertools.combinations(data, r=2):
        if x + y == 2020:
            return x * y


def part_two(data):
    for x, y, z in itertools.combinations(data, r=3):
        if x + y + z == 2020:
            return x * y * z


def main():
    data = parse_data()

    print(f'Day 01 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 01 Part 02: {part_two(data) or "skipped"}')
