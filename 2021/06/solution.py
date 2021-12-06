from functools import cache


def parse_data():
    with open('2021/06/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.split(",")]


@cache
def lanternfish(age, day):
    if age >= day:
        return 1

    return lanternfish(7, day - age) + lanternfish(9, day - age)


def part_one(data):
    return sum(lanternfish(age, 80) for age in data)


def part_two(data):
    return sum(lanternfish(age, 256) for age in data)


def main():
    data = parse_data()

    print(f'Day 06 Part 01: {part_one(data)}')
    print(f'Day 06 Part 02: {part_two(data)}')
