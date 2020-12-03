def parse_data():
    with open('aoc/03/input.txt') as f:
        data = f.read()

    return data.splitlines()


def get_trees(data, dx, dy):
    trees = 0
    x = 0
    for row in data[::dy]:
        if row[x] == '#':
            trees += 1

        x = (x + dx) % len(row)

    return trees


def part_one(data):
    return get_trees(data, 3, 1)


def part_two(data):
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    answer = 1
    for slope in slopes:
        answer *= get_trees(data, *slope)

    return answer


def main():
    data = parse_data()

    print(f'Day 03 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 03 Part 02: {part_two(data) or "skipped"}')
