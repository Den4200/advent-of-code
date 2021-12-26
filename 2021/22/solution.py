import re
from bisect import bisect_left, bisect_right
from itertools import product

CUBOID_RE = re.compile(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)")


class BitArray:

    def __init__(self, size):
        self.bytes = bytearray((size >> 3) + 1)

    def __getitem__(self, index):
        return (self.bytes[index >> 3] >> (index & 7)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[index >> 3] |= 1 << (index & 7)
        else:
            self.bytes[index >> 3] &= ~(1 << (index & 7))


def parse_data():
    with open('2021/22/input.txt') as f:
        data = f.read()

    return [
        (
            *map(int, (c := CUBOID_RE.fullmatch(line).groups())[1:]),
            c[0] == "on"
        )
        for line in data.splitlines()
    ]


def part_one(data):
    return sum({
        (x, y, z): cuboid[6]
        for cuboid in data
        for x in range(max(cuboid[0], -50), min(cuboid[1], 50) + 1)
        for y in range(max(cuboid[2], -50), min(cuboid[3], 50) + 1)
        for z in range(max(cuboid[4], -50), min(cuboid[5], 50) + 1)
    }.values())


def part_two(data):
    xs = set()
    ys = set()
    zs = set()

    for cuboid in data:
        xs |= {cuboid[0], cuboid[1] + 1}
        ys |= {cuboid[2], cuboid[3] + 1}
        zs |= {cuboid[4], cuboid[5] + 1}

    xs = sorted(xs)
    ys = sorted(ys)
    zs = sorted(zs)

    grid = [[BitArray(len(zs)) for _ in range(len(ys))] for _ in range(len(xs))]

    for *coords, state in data:
        for x, y, z in product(*(
            range(bisect_left(cs, c1), bisect_right(cs, c2))
            for c1, c2, cs in zip(
                coords[::2],
                coords[1::2],
                (xs, ys, zs),
            )
        )):
            grid[x][y][z] = state

    volume = 0
    for x, yba in enumerate(grid):
        for y, zba in enumerate(yba):
            for z, state in enumerate(zba):
                if state:
                    volume += (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y]) * (zs[z + 1] - zs[z])

    return volume


def main():
    data = parse_data()

    print(f'Day 22 Part 01: {part_one(data)}')
    print(f'Day 22 Part 02: {part_two(data)}')
