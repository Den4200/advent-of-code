def parse_data():
    with open('aoc/15/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.split(',')]


def memory_game(data, n):
    spoken = dict()

    for turn, value in enumerate(data, start=1):
        spoken[value] = turn

    latest = data[-1]
    for turn in range(len(data), n):
        previous = latest

        if previous in spoken:
            latest = turn - spoken[previous]
        else:
            latest = 0

        spoken[previous] = turn

    return latest


def part_one(data):
    return memory_game(data, 2020)


def part_two(data):
    return memory_game(data, 30000000)


def main():
    data = parse_data()

    print(f'Day 15 Part 01: {part_one(data)}')
    print(f'Day 15 Part 02: {part_two(data)}')
