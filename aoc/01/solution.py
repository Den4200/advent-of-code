import itertools

from aoc import submit


def parse_data(data):
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
    with open('aoc/01/input.txt') as f:
        problem_input = f.read()

    data = parse_data(problem_input)

    answer_one = part_one(data)
    answer_two = part_two(data)

    print(f'Day 01 Part 01: {answer_one or "skipped"}')
    print(f'Day 01 Part 02: {answer_two or "skipped"}')

    submit(1, 1, answer_one)
    submit(1, 2, answer_two)
