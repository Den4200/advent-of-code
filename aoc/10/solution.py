from collections import defaultdict
from functools import cache


def parse_data():
    with open('aoc/10/input.txt') as f:
        data = f.read()

    data = [int(num) for num in data.splitlines()]
    return (0, *sorted(data), max(data) + 3)


def part_one(data):
    nums = defaultdict(int)
    for i, _ in enumerate(data[1:], 1):
        nums[data[i] - data[i-1]] += 1

    return nums[1] * nums[3]


@cache
def part_two(data):
    total = 1

    if len(data) == 1:
        return 0

    if data[1] - data[0] not in (1, 2, 3):
        return 0

    for idx, num in enumerate(data):
        if idx == len(data) - 1:
            return total

        if data[idx + 1] - num in (1, 2):
            total += part_two((num,) + data[idx + 2:])

    return total


def main():
    data = parse_data()

    print(f'Day 10 Part 01: {part_one(data)}')
    print(f'Day 10 Part 02: {part_two(data)}')
