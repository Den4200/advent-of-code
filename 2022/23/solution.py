from collections import defaultdict
import itertools

DIRECTIONS = [
    [(0, -1), (-1, -1), (1, -1)],  # North
    [(0, 1), (-1, 1), (1, 1)],     # South
    [(-1, 0), (-1, -1), (-1, 1)],  # West
    [(1, 0), (1, -1), (1, 1)],     # East
]


def parse_data():
    with open("2022/23/input.txt") as f:
        data = f.read()

    return {
        (x, y)
        for y, line in enumerate(data.splitlines())
        for x, point in enumerate(line)
        if point == "#"
    }


def has_neighbors(x, y, grid):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == dy == 0:
                continue

            if (x + dx, y + dy) in grid:
                return True

    return False


def simulate(grid, rounds=None):
    for r in itertools.count() if rounds is None else range(rounds):
        proposed_positions = defaultdict(list)
        updated_grid = set()

        for x, y in grid:
            if not has_neighbors(x, y, grid):
                updated_grid.add((x, y))
                continue

            for dir_offset in range(4):
                direction = DIRECTIONS[(r + dir_offset) % 4]

                if all((x + dx, y + dy) not in grid for dx, dy in direction):
                    dx, dy = direction[0]
                    proposed_positions[x + dx, y + dy].append((x, y))
                    break
            else:
                updated_grid.add((x, y))

        for pos, es in proposed_positions.items():
            if len(es) == 1:
                updated_grid.add(pos)
            else:
                updated_grid.update(es)

        if grid == updated_grid:
            break

        grid = updated_grid

    return r + 1, grid


def part_one(data):
    _, grid = simulate(data, rounds=10)
    width = max(x for x, _ in grid) - min(x for x, _ in grid) + 1
    height = max(y for _, y in grid) - min(y for _, y in grid) + 1

    return width * height - len(grid)


def part_two(data):
    rounds, _ = simulate(data)
    return rounds


def main():
    data = parse_data()

    print(f"Day 23 Part 01: {part_one(data)}")
    print(f"Day 23 Part 02: {part_two(data)}")
