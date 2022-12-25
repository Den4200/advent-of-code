from __future__ import annotations

from collections import namedtuple
from enum import Enum
from typing import Literal


class Position(namedtuple("Position", "x y")):

    def __add__(self, other: Position) -> Position:
        return Position(self.x + other.x, self.y + other.y)


class Tile(Enum):
    FLOOR = "."
    WALL = "#"
    EMPTY = " "


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def left(self) -> Direction:
        return Direction((self.value - 1) % len(Direction))

    def right(self) -> Direction:
        return Direction((self.value + 1) % len(Direction))

    def turn(self, instruction: Literal["L", "R"]) -> Direction:
        match instruction:
            case "L": return self.left()
            case "R": return self.right()

    def opposite(self) -> Direction:
        return self.right().right()

    def delta(self) -> Position:
        match self:
            case Direction.RIGHT: return Position(1, 0)
            case Direction.DOWN: return Position(0, 1)
            case Direction.LEFT: return Position(-1, 0)
            case Direction.UP: return Position(0, -1)


def fill_range(start: int, stop: int) -> range:
    if start < stop:
        return range(start, stop)
    return range(start - 1, stop - 1, -1)


def generate_edge_positions(
    edge: tuple[int | list[int], int | list[int], Direction],
    edge_length: int
) -> list[Position]:
    x, y, direction = edge

    if isinstance(x, int):
        match direction:
            case Direction.LEFT: xs = [x * edge_length + 1 for _ in range(edge_length)]
            case Direction.RIGHT: xs = [x * edge_length for _ in range(edge_length)]

        ys = fill_range(y[0] * edge_length + 1, y[1] * edge_length + 1)
        return [Position(*coords) for coords in zip(xs, ys)]

    if isinstance(y, int):
        xs = fill_range(x[0] * edge_length + 1, x[1] * edge_length + 1)

        match direction:
            case Direction.UP: ys = [y * edge_length + 1 for _ in range(edge_length)]
            case Direction.DOWN: ys = [y * edge_length for _ in range(edge_length)]

        return [Position(*coords) for coords in zip(xs, ys)]


def generate_edge_portals(edges, edge_length) -> \
        dict[tuple[Position, Direction], tuple[Position, Direction]]:
    portals = {}

    for edge1, edge2 in edges:
        for pos1, pos2 in zip(
            generate_edge_positions(edge1, edge_length),
            generate_edge_positions(edge2, edge_length),
        ):
            portals[pos1, edge1[2]] = pos2, edge2[2].opposite()
            portals[pos2, edge2[2]] = pos1, edge1[2].opposite()

    return portals


EDGE_LENGTH = 50
EDGE_PORTALS = generate_edge_portals([
        ((2, [2, 3], Direction.RIGHT), (3, [1, 0], Direction.RIGHT)),
        ((2, [1, 2], Direction.RIGHT), ([2, 3], 1, Direction.DOWN)),
        ((1, [3, 4], Direction.RIGHT), ([1, 2], 3, Direction.DOWN)),
        (([0, 1], 4, Direction.DOWN), ([2, 3], 0, Direction.UP)),
        ((0, [2, 3], Direction.LEFT), (1, [1, 0], Direction.LEFT)),
        ((0, [3, 4], Direction.LEFT), ([1, 2], 0, Direction.UP)),
        (([0, 1], 2, Direction.UP), (1, [1, 2], Direction.LEFT)),
    ],
    EDGE_LENGTH,
)


def parse_data() -> tuple[Position, list[int | str], dict[Position, Tile]]:
    with open("2022/22/input.txt") as f:
        data = f.read()

    grid_str, instructions_str = data.split("\n\n")

    grid = {}
    start = None
    for y, line in enumerate(grid_str.splitlines()):
        for x, char in enumerate(line.rstrip()):
            pos = Position(x + 1, y + 1)
            grid[pos] = Tile(char)

            if start is None and grid[pos] != Tile.EMPTY:
                start = pos

    instructions = []
    current_number = 0
    for char in instructions_str.strip():
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            instructions.append(current_number)
            current_number = 0

            instructions.append(char)

    instructions.append(current_number)

    return start, instructions, grid


def walk_straight(
    position: Position,
    direction: Direction,
    steps: int,
    grid: dict[Position, Tile],
    fold: bool = False
) -> Position:
    for _ in range(steps):
        new_position = position + direction.delta()
        tile = grid.get(new_position, Tile.EMPTY)

        match tile:
            case Tile.WALL:
                return position, direction

            case Tile.FLOOR:
                position = new_position

            case Tile.EMPTY:
                if fold:
                    new_position, new_direction = EDGE_PORTALS[position, direction]
                else:
                    opposite_direction = direction.opposite()
                    opposite_edge_position = position

                    while grid.get(opposite_edge_position, Tile.EMPTY) != Tile.EMPTY:
                        opposite_edge_position = opposite_edge_position + opposite_direction.delta()

                    new_position = opposite_edge_position + direction.delta()
                    new_direction = direction

                if grid[new_position] == Tile.WALL:
                    return position, direction

                position = new_position
                direction = new_direction

    return position, direction


def walk(
    start: Position,
    instructions: list[int | str],
    grid: dict[Position, Tile],
    fold: bool = False
) -> tuple[Position, Direction]:
    position = start
    direction = Direction.RIGHT

    for instruction in instructions:
        match instruction:
            case str():
                direction = direction.turn(instruction)
            case int():
                position, direction = walk_straight(position, direction, instruction, grid, fold)

    return position.x * 4 + position.y * 1000 + direction.value


def part_one(data):
    return walk(*data)


def part_two(data):
    return walk(*data, fold=True)


def main():
    data = parse_data()

    print(f"Day 22 Part 01: {part_one(data)}")
    print(f"Day 22 Part 02: {part_two(data)}")
