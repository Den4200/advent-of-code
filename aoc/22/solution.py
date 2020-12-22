from collections import deque
from itertools import islice


def parse_data():
    with open('aoc/22/input.txt') as f:
        data = f.read()

    return [[int(num) for num in nums.splitlines()[1:]] for nums in data.split('\n\n')]


def part_one(data):
    player_one = deque(data[0])
    player_two = deque(data[1])

    winner = None

    while True:
        if (one := player_one.popleft()) > (two := player_two.popleft()):
            player_one.extend((one, two))
        else:
            player_two.extend((two, one))

        if len(player_one) == 0:
            winner = player_two
        elif len(player_two) == 0:
            winner = player_one
        else:
            continue

        break

    return sum(mul * num for mul, num in enumerate(reversed(winner), start=1))


def recursive_combat(player_one, player_two):
    player_one = deque(player_one)
    player_two = deque(player_two)

    rounds = set()

    while len(player_one) > 0 and len(player_two) > 0:
        current = (tuple(player_one), tuple(player_two))

        if current in rounds:
            return 0, player_one

        rounds.add(current)

        one = player_one.popleft()
        two = player_two.popleft()

        if len(player_one) >= one and len(player_two) >= two:
            winner = recursive_combat(islice(player_one, 0, one), islice(player_two, 0, two))[0]
        else:
            winner = two > one

        if winner:
            player_two.extend((two, one))
        else:
            player_one.extend((one, two))

    return (0, player_one) if len(player_two) == 0 else (1, player_two)


def part_two(data):
    winner = recursive_combat(*data)
    return sum(mul * num for mul, num in enumerate(reversed(winner[1]), start=1))


def main():
    data = parse_data()

    print(f'Day 22 Part 01: {part_one(data)}')
    print(f'Day 22 Part 02: {part_two(data)}')
