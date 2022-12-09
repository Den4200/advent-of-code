import numpy as np


def parse_data():
    with open("2022/09/input.txt") as f:
        data = f.read()

    return [((parts := line.split())[0], int(parts[1])) for line in data.splitlines()]


MOVEMENTS = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "L": np.array([-1, 0]),
    "R": np.array([1, 0]),
}


def part_one(data):
    head_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])

    tail_positions = {tuple(tail_pos)}

    for direction, amount in data:
        movement = MOVEMENTS[direction]

        for _ in range(amount):
            head_pos += movement
            diff = np.abs(tail_pos - head_pos)

            if (diff > 1).any():
                if direction in ("L", "R") and tail_pos[1] != head_pos[1]:
                    tail_pos[1] = head_pos[1]
                if direction in ("D", "U") and tail_pos[0] != head_pos[0]:
                    tail_pos[0] = head_pos[0]

                tail_pos += movement
                tail_positions.add(tuple(tail_pos))

    return len(tail_positions)


def part_two(data):
    tail_positions = {(0, 0)}
    nodes = [np.array([0, 0]) for _ in range(10)]

    for direction, amount in data:
        rope_head = nodes[0]

        for _ in range(amount):
            rope_head += MOVEMENTS[direction]

            for head, tail in zip(nodes, nodes[1:]):
                diff = head - tail

                if (np.abs(diff) > 1).any():
                    tail += np.sign(diff)

            tail_positions.add(tuple(nodes[-1]))

    return len(tail_positions)


def main():
    data = parse_data()

    print(f"Day 09 Part 01: {part_one(data)}")
    print(f"Day 09 Part 02: {part_two(data)}")
