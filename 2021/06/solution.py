def parse_data():
    with open('2021/06/input.txt') as f:
        data = f.read()

    fish = [0] * 9
    for num in data.split(","):
        fish[int(num)] += 1

    return fish


def lanternfish(data, days):
    data = data.copy()

    for day in range(days):
        data[(day + 7) % 9] += data[day % 9]

    return sum(data)


def part_one(data):
    return lanternfish(data, 80)


def part_two(data):
    return lanternfish(data, 256)


def main():
    data = parse_data()

    print(f'Day 06 Part 01: {part_one(data)}')
    print(f'Day 06 Part 02: {part_two(data)}')
