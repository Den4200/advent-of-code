from collections import defaultdict
from itertools import product


def parse_data():
    with open('aoc/24/input.txt') as f:
        data = f.read()

    return data.splitlines()


def get_black_tiles(data):
    black_tiles = set()

    for line in data:
        row = 0
        col = 0

        directions = iter(line)

        while True:
            try:
                direction = next(directions)
            except StopIteration:
                break

            if direction in ('n', 's'):
                direction += next(directions)

            row += direction == 'e'
            row -= direction == 'w'

            col += direction == 'se'
            col -= direction == 'nw'

            row -= direction == 'sw'
            col += direction == 'sw'

            row += direction == 'ne'
            col -= direction == 'ne'

        coords = (row, col)
        if coords in black_tiles:
            black_tiles.remove(coords)
        else:
            black_tiles.add(coords)

    return black_tiles


def part_one(data):
    return len(get_black_tiles(data))


def part_two(data):
    black_tiles = get_black_tiles(data)

    for i in range(100):
        neighbors = defaultdict(int)

        for row, col in black_tiles:
            if neighbors.get((row, col)) is None:
                neighbors[row, col] = 0

            for dr, dc in product(range(-1, 2), repeat=2):
                if dr != dc:
                    neighbors[row + dr, col + dc] += 1

        for tile, amt in neighbors.items():
            if tile in black_tiles and not 1 <= amt <= 2:
                black_tiles.remove(tile)
            elif tile not in black_tiles and amt == 2:
                black_tiles.add(tile)

    return len(black_tiles)


def main():
    data = parse_data()

    print(f'Day 24 Part 01: {part_one(data)}')
    print(f'Day 24 Part 02: {part_two(data)}')
