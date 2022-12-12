from heapq import heappop, heappush
from string import ascii_lowercase


def parse_data():
    with open("2022/12/input.txt") as f:
        data = [list(line.strip()) for line in f.readlines()]

    start = None
    end = None
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            if height == "S":
                start = (x, y)
                data[y][x] = "a"
            elif height == "E":
                end = (x, y)
                data[y][x] = "z"

            if start is not None and end is not None:
                break

    return {
        (x, y): ascii_lowercase.index(height)
        for y, line in enumerate(data)
        for x, height in enumerate(line)
    }, start, end


def neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def find_shortest_path(height_map, start, end):
    open = [(0, start)]
    closed = set()
    min_steps = {start: 0}

    while open:
        steps, coord = heappop(open)
        closed.add(coord)

        if coord == end:
            return steps

        for neighbor in neighbors(*coord):
            if (
                neighbor in closed
                    or neighbor not in height_map
                    or height_map[neighbor] - height_map[coord] > 1
            ):
                continue

            if neighbor not in min_steps or steps + 1 < min_steps[neighbor]:
                min_steps[neighbor] = steps + 1
                heappush(open, (steps + 1, neighbor))


def part_one(data):
    return find_shortest_path(*data)


def part_two(data):
    height_map, _, end = data
    return min(
        path
        for coord, height in height_map.items()
        if height == 0 and (path := find_shortest_path(height_map, coord, end)) is not None
    )


def main():
    data = parse_data()

    print(f"Day 12 Part 01: {part_one(data)}")
    print(f"Day 12 Part 02: {part_two(data)}")
