LETTER_VALUES = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}


def parse_data():
    with open("2022/02/input.txt") as f:
        data = f.read()

    return [(LETTER_VALUES[p1], LETTER_VALUES[p2]) for p1, _, p2 in data.splitlines()]


def part_one(data):
    return sum(p2 + 1 + 3 * ((p2 - p1 + 1) % 3) for p1, p2 in data)


def part_two(data):
    return sum(p2 * 3 + 1 + (p1 + p2 - 1) % 3 for p1, p2 in data)


def main():
    data = parse_data()

    print(f"Day 02 Part 01: {part_one(data)}")
    print(f"Day 02 Part 02: {part_two(data)}")
