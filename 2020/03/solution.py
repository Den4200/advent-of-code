def parse_data():
    with open('2020/03/input.txt') as f:
        data = f.read()

    return data.splitlines()


def get_trees(data, dx, dy):
    height = len(data)
    width = len(data[0])

    trees = 0
    x = 0
    for y in range(0, height, dy):
        if data[y][x] == '#':
            trees += 1

        x = (x + dx) % width

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

    print(f'Day 03 Part 01: {part_one(data)}')
    print(f'Day 03 Part 02: {part_two(data)}')
