from __future__ import annotations

import math


class Range:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __bool__(self) -> bool:
        return self.stop > self.start

    def __xor__(self, other: Range) -> list[Range]:
        ranges = []
        middle = self & other

        if left := Range(self.start, middle.start):
            ranges.append(left)

        if right := Range(middle.stop, self.stop):
            ranges.append(right)

        return ranges

    def __and__(self, other: Range) -> Range:
        return Range(max(self.start, other.start), min(self.stop, other.stop))

    def __sub__(self, other: Range) -> int:
        return self.start - other.start

    def __rshift__(self, offset: int) -> Range:
        return Range(self.start + offset, self.stop + offset)

    def __contains__(self, other: int | Range) -> bool:
        if isinstance(other, Range):
            return other.stop > self.start and other.start < self.stop

        return self.start <= other < self.stop

    def __lt__(self, other: Range) -> bool:
        return self.start < other.start


def parse_data():
    with open("2023/05/input.txt") as f:
        data = [lines.splitlines() for lines in f.read().split("\n\n")]

    seeds = [int(seed) for seed in data[0][0].partition(" ")[2].split()]

    maps = []
    for map_ in data[1:]:
        ranges = []

        for line in map_[1:]:
            dest, src, rng = map(int, line.split())
            ranges.append((Range(src, src + rng), Range(dest, dest + rng)))

        maps.append(ranges)

    return seeds, maps


def part_one(data):
    seeds, maps = data
    min_location = math.inf

    for seed in seeds:
        for map_ in maps:
            for srcs, dests in map_:
                if seed in srcs:
                    seed += dests - srcs
                    break

        if seed < min_location:
            min_location = seed

    return min_location


def part_two(data):
    seeds, maps = data

    si = iter(seeds)
    seeds = [Range(start, start + rng) for start, rng in zip(si, si)]

    for map_ in maps:
        new_seeds = []

        for seed in seeds:
            for srcs, dests in map_:
                if seed not in srcs:
                    continue

                seeds += seed ^ srcs
                new_seeds.append((seed & srcs) >> (dests - srcs))
                break
            else:
                new_seeds.append(seed)

        seeds = new_seeds

    return min(seeds).start


def main():
    data = parse_data()

    print(f"Day 05 Part 01: {part_one(data)}")
    print(f"Day 05 Part 02: {part_two(data)}")
