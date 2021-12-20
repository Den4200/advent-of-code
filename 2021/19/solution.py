import math
from copy import deepcopy
from itertools import combinations, permutations

import numpy as np


def parse_data():
    with open('2021/19/input.txt') as f:
        data = f.read()

    return [
        np.array([
            [int(coord) for coord in line.split(",")]
            for line in scanner.splitlines()[1:]
        ])
        for scanner in data.split("\n\n")
    ]


def rotations():
    rots = [
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    ]
    rots = [np.array(rot) for rot in rots]

    for ri, rj in permutations(rots, r=2):
        if ri @ rj == 0:
            rk = np.cross(ri, rj)
            yield lambda mat: mat @ np.array([ri, rj, rk])


def find_transformations(scanners, diffs, s1i, s2i, mat):
    s1 = scanners[s1i]
    s2 = scanners[s2i]

    for rot in rotations():
        s2r = rot(s2)
        p = diffs[s1i][mat][0]

        for q in diffs[s2i][mat]:
            diff = s1[p, :] - s2r[q, :]

            s1_beacons = set(tuple(beacon) for beacon in s1)
            s2r_beacons = set(tuple(beacon) for beacon in s2r + diff)

            if len(s1_beacons & s2r_beacons) >= 12:
                return diff, s2r_beacons, rot


def absolute_diffs(coords):
    return {
        tuple(sorted(abs(diff) for diff in coords[s1i, :] - coords[s2i, :])): (s1i, s2i)
        for s1i, s2i in combinations(range(coords.shape[0]), r=2)
    }


def match(diffs):
    for (s1i, s1_diffs), (s2i, s2_diffs) in combinations(enumerate(diffs), r=2):
        if len(matches := set(s1_diffs) & set(s2_diffs)) >= math.comb(12, 2):
            yield s1i, s2i, next(iter(matches))


def find_scanners(scanners):
    positions = {0: (0, 0, 0)}
    diffs = [absolute_diffs(scanner) for scanner in scanners]
    beacons = {tuple(beacon) for beacon in scanners[0]}

    while len(positions) < len(scanners):
        for s1i, s2i, mat in match(diffs):
            if (s1i in positions) == (s2i in positions):
                continue

            elif s2i in positions:
                s1i, s2i = s2i, s1i

            positions[s2i], new_beacons, rot = find_transformations(scanners, diffs, s1i, s2i, mat)
            scanners[s2i] = rot(scanners[s2i]) + positions[s2i]
            beacons |= new_beacons

    return list(positions.values()), beacons


def part_one(data):
    _, beacons = find_scanners(deepcopy(data))
    return len(beacons)


def part_two(data):
    scanners, _ = find_scanners(deepcopy(data))
    return max(np.abs(s1 - s2).sum() for s1, s2 in combinations(scanners, r=2))


def main():
    data = parse_data()

    print(f'Day 19 Part 01: {part_one(data)}')
    print(f'Day 19 Part 02: {part_two(data)}')
