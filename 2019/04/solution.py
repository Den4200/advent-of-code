from itertools import groupby


def parse_data():
    with open('2019/04/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.split("-")]


def part_one(data):
    total = 0

    for num in range(data[0], data[1] + 1):
        places = str(num)

        for prev, curr in zip(places, places[1:]):
            if prev == curr:
                break
        else:
            continue

        for prev, curr in zip(places, places[1:]):
            if curr < prev:
                break
        else:
            total += 1

    return total


def part_two(data):
    total = 0

    for num in range(data[0], data[1] + 1):
        places = str(num)

        if not any(len("".join(g)) == 2 for _, g in groupby(places)):
            continue

        for prev, curr in zip(places, places[1:]):
            if curr < prev:
                break
        else:
            total += 1

    return total


def main():
    data = parse_data()

    print(f'Day 04 Part 01: {part_one(data)}')
    print(f'Day 04 Part 02: {part_two(data)}')
