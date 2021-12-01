def parse_data():
    with open('2019/01/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def part_one(data):
    return sum(mass // 3 - 2 for mass in data)


def part_two(data):
    total = 0
    for num in data:
        while (num := num // 3 - 2) > 0:
            total += num

    return total


def main():
    data = parse_data()

    print(f'Day 01 Part 01: {part_one(data)}')
    print(f'Day 01 Part 02: {part_two(data)}')
