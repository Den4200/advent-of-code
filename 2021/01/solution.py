def parse_data():
    with open('2021/01/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def part_one(data):
    return sum(curr > prev for prev, curr in zip(data, data[1:]))


def part_two(data):
    return sum(sum(data[i-2:i+1]) > sum(data[i-3:i]) for i, _ in enumerate(data[3:], 3))


def main():
    data = parse_data()

    print(f'Day 01 Part 01: {part_one(data)}')
    print(f'Day 01 Part 02: {part_two(data)}')
