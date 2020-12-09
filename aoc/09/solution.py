import itertools


def parse_data():
    with open('aoc/09/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def part_one(data):
    for idx, num in enumerate(data[25:], start=25):
        valid = {x + y for x, y in itertools.combinations(data[idx - 25:idx], r=2)}

        if num not in valid:
            return num


def part_two(data):
    invalid = part_one(data)

    rng = 2
    while True:
        for idx, _ in enumerate(data[25:]):
            contiguous = data[idx:idx + rng]

            if sum(contiguous) == invalid:
                return min(contiguous) + max(contiguous)

        rng += 1


def main():
    data = parse_data()

    print(f'Day 09 Part 01: {part_one(data)}')
    print(f'Day 09 Part 02: {part_two(data)}')
