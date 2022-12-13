from ast import literal_eval
from functools import cmp_to_key


def parse_data():
    with open("2022/13/input.txt") as f:
        data = f.read()

    return [[literal_eval(line) for line in lines.splitlines()] for lines in data.split("\n\n")]


def validate_pair(pair):
    left, right = pair

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0

        return -1

    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    if isinstance(left, list) and isinstance(right, list):
        for sub_pair in zip(left, right):
            is_valid = validate_pair(sub_pair)
            if is_valid == -1:
                return -1

            if is_valid == 1:
                return 1

        if len(left) < len(right):
            return 1
        elif len(left) == len(right):
            return 0

    return -1


def part_one(data):
    return sum(i for i, pair in enumerate(data, start=1) if validate_pair(pair) == 1)


def part_two(data):
    sorted_packets = sorted(
        [packet for pair in data for packet in pair] + [[[2]], [[6]]],
        key=cmp_to_key(lambda p1, p2: validate_pair([p2, p1]))
    )
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


def main():
    data = parse_data()

    print(f"Day 13 Part 01: {part_one(data)}")
    print(f"Day 13 Part 02: {part_two(data)}")
