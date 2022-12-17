from collections import namedtuple
from itertools import cycle

ROCKS = [
    [
        [1, 1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1],
    ],
]


class Rock(namedtuple("Rock", "shape left_x bottom_y")):

    def __lshift__(self, value):
        return Rock(self.shape, self.left_x - value, self.bottom_y)

    def __rshift__(self, value):
        return Rock(self.shape, self.left_x + value, self.bottom_y)

    def __sub__(self, value):
        return Rock(self.shape, self.left_x, self.bottom_y - value)

    def __add__(self, value):
        return Rock(self.shape, self.left_x, self.bottom_y + value)

    @property
    def positions(self):
        return [
            (self.left_x + dx, self.bottom_y + dy)
            for dy, row in enumerate(self.shape)
            for dx, filled in enumerate(row)
            if filled
        ]

    def validate_move(self, grid):
        return all(0 <= pos[0] < 7 and pos[1] >= 0 and pos not in grid for pos in self.positions)


def parse_data():
    with open("2022/17/input.txt") as f:
        data = f.read()

    return list(data.strip())


def tetris_height(rocks, jet_directions):
    jets = cycle(enumerate(jet_directions))
    grid = set()
    highest = -1
    height_diffs = {}
    history = []
    repeated_state = None

    for rock_i, rock_shape in cycle(enumerate(ROCKS)):
        rock = Rock(rock_shape, 2, highest + 4)

        for jet_i, jet in jets:
            match jet:
                case ">":
                    rock >>= 1

                    if not rock.validate_move(grid):
                        rock <<= 1
                case "<":
                    rock <<= 1

                    if not rock.validate_move(grid):
                        rock >>= 1

            rock -= 1
            if not rock.validate_move(grid):
                rock += 1
                break

        prev_highest = highest
        highest = max(highest, max(rock.positions, key=lambda pos: pos[1])[1])

        prev_rows_hash = "".join(
            "1" if (x, y) in grid else "0"
            for y in range(max(prev_highest - 10, 0), prev_highest)
            for x in range(7)
        )
        current_state = (rock_i, jet_i, prev_rows_hash)

        history.append(current_state)
        if current_state in height_diffs:
            repeated_state = current_state
            break

        height_diffs[current_state] = highest - prev_highest
        grid |= set(rock.positions)

    cycle_start = history.index(repeated_state)
    cycle_length = len(height_diffs) - cycle_start
    cycle_sum = sum(
        height_diffs[history[i]]
        for i in range(cycle_start, cycle_start + cycle_length)
    )

    cycles, remainder = divmod(rocks - cycle_start, cycle_length)
    height = sum(height_diffs[history[i]] for i in range(cycle_start))
    height += cycles * cycle_sum
    height += sum(height_diffs[history[i]] for i in range(cycle_start, cycle_start + remainder))

    return height


def part_one(data):
    return tetris_height(2022, data)


def part_two(data):
    return tetris_height(1_000_000_000_000, data)


def main():
    data = parse_data()

    print(f"Day 17 Part 01: {part_one(data)}")
    print(f"Day 17 Part 02: {part_two(data)}")
