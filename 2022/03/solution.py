from string import ascii_letters

from more_itertools import chunked


def parse_data():
    with open("2022/03/input.txt") as f:
        data = f.read()

    return [(line[:len(line) // 2], line[len(line) // 2:]) for line in data.splitlines()]


def part_one(data):
    return sum(ascii_letters.index(next(iter(set(c1) & set(c2)))) + 1 for c1, c2 in data)


def part_two(data):
    s = 0
    for group in chunked(data, 3):
        c = set("".join(group[0]))

        for c1, c2 in group[1:]:
            c &= set(c1 + c2)

        s += ascii_letters.index(next(iter(c))) + 1

    return s


def main():
    data = parse_data()

    print(f"Day 03 Part 01: {part_one(data)}")
    print(f"Day 03 Part 02: {part_two(data)}")
