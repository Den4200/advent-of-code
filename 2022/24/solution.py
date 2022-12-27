from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
import itertools


class Direction(Enum):
    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "v"

    @property
    def delta(self):
        match self:
            case Direction.LEFT: return (-1, 0)
            case Direction.RIGHT: return (1, 0)
            case Direction.UP: return (0, -1)
            case Direction.DOWN: return (0, 1)


@dataclass
class Blizzard:
    x: int
    y: int
    direction: Direction

    bw: int
    bh: int

    @property
    def position(self):
        return self.x, self.y

    def update(self):
        dx, dy = self.direction.delta
        nx = self.x + dx
        ny = self.y + dy

        if 0 <= nx < self.bw and 0 <= ny < self.bh:
            self.x = nx
            self.y = ny
            return

        match self.direction:
            case Direction.LEFT: self.x = self.bw - 1
            case Direction.RIGHT: self.x = 0
            case Direction.UP: self.y = self.bh - 1
            case Direction.DOWN: self.y = 0


def parse_data():
    with open("2022/24/input.txt") as f:
        data = f.read()

    grid = [line[1:-1] for line in data.splitlines()[1:-1]]
    basin_width = len(grid[0])
    basin_height = len(grid)

    return [
        Blizzard(x, y, Direction(direction), basin_width, basin_height)
        for y, line in enumerate(grid)
        for x, direction in enumerate(line)
        if direction != "."
    ], basin_width, basin_height


def shortest_path(blizzards, basin_width, basin_height, start, target):
    positions = {start}

    for minutes in itertools.count():
        open_positions = {(x, y) for y in range(basin_height) for x in range(basin_width)}
        open_positions.add(start)
        open_positions.add(target)

        for blizzard in blizzards:
            blizzard.update()

            if blizzard.position in open_positions:
                open_positions.remove(blizzard.position)

        positions |= {(x + d.delta[0], y + d.delta[1]) for x, y in positions for d in Direction}
        positions &= open_positions

        if target in positions:
            return minutes + 1


def part_one(data):
    blizzards, bw, bh = data
    return shortest_path(deepcopy(blizzards), bw, bh, (0, -1), (bw - 1, bh))


def part_two(data):
    blizzards, bw, bh = data
    start = (0, -1)
    target = (bw - 1, bh)
    return shortest_path(blizzards, bw, bh, start, target) \
        + shortest_path(blizzards, bw, bh, target, start) \
        + shortest_path(blizzards, bw, bh, start, target)


def main():
    data = parse_data()

    print(f"Day 24 Part 01: {part_one(data)}")
    print(f"Day 24 Part 02: {part_two(data)}")
