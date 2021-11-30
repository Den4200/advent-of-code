import itertools

from sympy.ntheory.modular import crt


def parse_data():
    with open('2020/13/input.txt') as f:
        data = f.read()

    earliest, ids = data.splitlines()
    return (
        int(earliest),
        {idx: int(id_) for idx, id_ in enumerate(ids.split(',')) if id_ != 'x'}
    )


def part_one(data):
    schedules = [(bus - data[0] % bus, bus) for bus in data[1].values()]
    minimum = min(schedules)

    return minimum[0] * minimum[1]


def part_two(data):
    modulii = list()
    remainders = list()

    for idx, id_ in data[1].items():
        modulii.append(id_)
        remainders.append(-idx % id_)

    return crt(modulii, remainders)[0]


def main():
    data = parse_data()

    print(f'Day 13 Part 01: {part_one(data)}')
    print(f'Day 13 Part 02: {part_two(data)}')
