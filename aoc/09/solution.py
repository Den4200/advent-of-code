from collections import deque
import itertools


def parse_data():
    with open('aoc/09/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def part_one(data):
    preamble = deque(data[:25], maxlen=25)
    nums = set(data[:25])

    for num in data[25:]:
        for compliment in preamble:
            if compliment * 2 != num and num - compliment in nums:
                break
        else:
            return num

        nums.remove(preamble[0])
        preamble.append(num)
        nums.add(num)


def part_two(data):
    invalid = part_one(data)

    rng = 2
    while True:
        for idx, _ in enumerate(data[25:]):
            contiguous = data[idx:idx + rng]

            if sum(contiguous) == invalid:
                return min(contiguous) + max(contiguous)

        rng += 1


def main():
    data = parse_data()

    print(f'Day 09 Part 01: {part_one(data)}')
    print(f'Day 09 Part 02: {part_two(data)}')
