from heapq import heappop, heappush
from itertools import product


def parse_data():
    with open('2021/15/input.txt') as f:
        data = f.read().splitlines()

    return (
        {
            (x, y): int(risk)
            for y, line in enumerate(data)
            for x, risk in enumerate(line)
        },
        len(data[0]),
        len(data),
    )


def neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def path(cavern, start, end):
    open = [(0, start)]
    closed = set()
    mins = {start: 0}

    while open:
        risk, coord = heappop(open)
        closed.add(coord)

        if coord == end:
            return risk

        for neighbor in neighbors(*coord):
            if neighbor in closed or neighbor not in cavern:
                continue

            new_risk = cavern[neighbor] + risk
            if neighbor not in mins or new_risk < mins[neighbor]:
                mins[neighbor] = new_risk
                heappush(open, (new_risk, neighbor))


def part_one(data):
    cavern, size_x, size_y = data
    return path(cavern, (0, 0), (size_x - 1, size_y - 1))


def part_two(data):
    cavern, size_x, size_y = data

    new_cavern = {
        (size_x * i + x, size_y * j + y): (risk + i + j - 1) % 9 + 1
        for (x, y), risk in cavern.items()
        for i, j in product((0, 1, 2, 3, 4), repeat=2)
    }
    return path(new_cavern, (0, 0), (size_x * 5 - 1, size_y * 5 - 1))


def main():
    data = parse_data()

    print(f'Day 15 Part 01: {part_one(data)}')
    print(f'Day 15 Part 02: {part_two(data)}')
