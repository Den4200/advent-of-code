import itertools
from collections import deque


def parse_data():
    with open('aoc/13/input.txt') as f:
        data = f.read()

    earliest, ids = data.splitlines()
    return int(earliest), [int(id_) if id_.isdigit() else id_ for id_ in ids.split(',')]


def part_one(data):
    for i in itertools.count(data[0]):
        for id_ in data[1]:
            if id_ != 'x' and i % id_ == 0:
                return id_ * (i - data[0])


def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


def modular_inverse(a, m):
    return extended_euclidean(a, m)[1] % m


def chinese_remainder_theorem(modulii, remainders):
    while True: 
        a = modular_inverse(modulii[1], modulii[0]) * remainders[0] * modulii[1]
        b = modular_inverse(modulii[0], modulii[1]) * remainders[1] * modulii[0]

        modulus = modulii[0] * modulii[1]

        remainders.popleft()
        remainders.popleft()
        remainders.appendleft((a + b) % modulus)

        modulii.popleft()
        modulii.popleft()
        modulii.appendleft(modulus)

        if len(remainders) == 1:
            return remainders[0]


def part_two(data):
    modulii = deque()
    remainders = deque()

    for idx, id_ in enumerate(data[1]):
        if id_ =='x':
            continue

        modulii.append(id_)
        remainders.append(-idx % id_)

    return chinese_remainder_theorem(modulii, remainders)


def main():
    data = parse_data()

    print(f'Day 13 Part 01: {part_one(data)}')
    print(f'Day 13 Part 02: {part_two(data)}')
