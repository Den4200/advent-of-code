from dataclasses import dataclass
import re

import z3


@dataclass
class Scanner:
    x: int
    y: int
    closest_beacon_x: int
    closest_beacon_y: int

    def no_beacon_area_from_row(self, row):
        ys = range(
            self.y - self.dist_from_closest_beacon,
            self.y + self.dist_from_closest_beacon + 1
        )

        if row not in ys:
            return None

        dx = self.dist_from_closest_beacon - abs(row - self.y)
        return set(range(self.x - dx, self.x + dx + 1))

    @property
    def dist_from_closest_beacon(self):
        return abs(self.closest_beacon_x - self.x) + abs(self.closest_beacon_y - self.y)


def parse_data():
    with open("2022/15/input.txt") as f:
        data = f.read()

    return [
        Scanner(*(
            int(coord)
            for coord in re.match(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                line
            ).groups()
        ))
        for line in data.splitlines()
    ]


def part_one(data):
    no_beacon_area = set()

    for scanner in data:
        if (no_beacons := scanner.no_beacon_area_from_row(2000000)) is not None:
            no_beacon_area |= no_beacons

    no_beacon_area ^= {
        scanner.closest_beacon_x
        for scanner in data
        if scanner.closest_beacon_y == 2000000
    }

    return len(no_beacon_area)


def part_two(data):
    x = z3.Int("x")
    y = z3.Int("y")

    solver = z3.Solver()
    solver.add(x >= 0, x <= 4000000, y >= 0, y <= 4000000)

    for scanner in data:
        solver.add(
            z3.Abs(y - scanner.y) + z3.Abs(x - scanner.x) > scanner.dist_from_closest_beacon
        )

    solver.check()
    model = solver.model()

    return model[x].as_long() * 4000000 + model[y].as_long()


def main():
    data = parse_data()

    print(f"Day 15 Part 01: {part_one(data)}")
    print(f"Day 15 Part 02: {part_two(data)}")
