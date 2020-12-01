import itertools


def part_one(data):
    data = [int(n) for n in data.splitlines()]

    for x, y in itertools.combinations(data, r=2):
        if x + y == 2020:
            print(x * y)
            break


def part_two(data):
    data = [int(n) for n in data.splitlines()]

    for x, y, z in itertools.combinations(data, r=3):
        if x + y + z== 2020:
            print(x * y * z)
            break


if __name__ == '__main__':
    with open('aoc/01/input.txt') as f:
        problem_input = f.read()

    part_one(problem_input)
    part_two(problem_input)
