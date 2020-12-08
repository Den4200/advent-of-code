import re


def parse_data():
    with open('aoc/02/input.txt') as f:
        data = f.read()

    return list(re.findall(r'(\d+)-(\d+) (\w): (\w+)', data))


def part_one(data):
    return sum(
        int(lower) <= pw.count(letter) <= int(upper) for lower, upper, letter, pw in data
    )


def part_two(data):
    return sum(
        (pw[int(first) - 1] == letter) ^ (pw[int(second) - 1] == letter) for first, second, letter, pw in data
    )


def main():
    data = parse_data()

    print(f'Day 02 Part 01: {part_one(data)}')
    print(f'Day 02 Part 02: {part_two(data)}')
