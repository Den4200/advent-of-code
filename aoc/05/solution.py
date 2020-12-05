def parse_data():
    with open('aoc/05/input.txt') as f:
        data = f.read()

    return [(line[:-3], line[-3:]) for line in data.splitlines()]


def get_ids(data):
    ids = set()

    for line in data:

        row = 0
        for idx, char in enumerate(line[0][::-1]):
            row += 2 ** idx if char == 'B' else 0

        col = 0
        for idx, char in enumerate(line[1][::-1]):
            col += 2 ** idx if char == 'R' else 0

        ids.add(row * 8 + col)

    return ids


def part_one(data):
    return max(get_ids(data))


def part_two(data):
    ids = get_ids(data)
    rng = set(range(min(ids), max(ids) + 1))

    return [*(rng - ids)][0]


def main():
    data = parse_data()

    print(f'Day 05 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 05 Part 02: {part_two(data) or "skipped"}')
