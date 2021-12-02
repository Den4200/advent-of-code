from functools import reduce
import numpy as np


def parse_data():
    with open('2019/03/input.txt') as f:
        data = f.read()

    return [wire.split(",") for wire in data.splitlines()]


def wire_circuit(data):
    directions = {
        "U": np.array([0, 1]),
        "D": np.array([0, -1]),
        "L": np.array([-1, 0]),
        "R": np.array([1, 0]),
    }

    wires = [[(directions[part[0]], int(part[1:])) for part in wire] for wire in data]

    wire_locations = []
    for wire in wires:
        current_location = (0, 0)
        locations = [current_location]

        for direction, steps in wire:
            locations += [
                tuple(current_location + direction * step) for step in range(1, steps + 1)
            ]
            current_location += direction * steps

        wire_locations.append(locations)

    intersections = reduce(lambda loc1, loc2: set(loc1) & set(loc2), wire_locations)
    intersections.remove((0, 0))

    return wire_locations, intersections


def part_one(data):
    _, intersections = wire_circuit(data)
    return min(sum(np.abs(intersection)) for intersection in intersections)


def part_two(data):
    wire_locations, intersections = wire_circuit(data)
    return min(
        sum(locations.index(intersection) for locations in wire_locations)
        for intersection in intersections
    )


def main():
    data = parse_data()

    print(f'Day 03 Part 01: {part_one(data)}')
    print(f'Day 03 Part 02: {part_two(data)}')
