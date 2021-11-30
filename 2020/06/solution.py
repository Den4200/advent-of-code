import re
from collections import Counter


def parse_data():
    with open('2020/06/input.txt') as f:
        data = f.read()

    return [(re.findall(r'\w', line), len(line.splitlines())) for line in data.split('\n\n')]


def part_one(data):
    return sum(len(set(group[0])) for group in data)


def part_two(data):
    return sum(len([k for k, v in Counter(group[0]).items() if v == group[1]]) for group in data)


def main():
    data = parse_data()

    print(f'Day 06 Part 01: {part_one(data)}')
    print(f'Day 06 Part 02: {part_two(data)}')
