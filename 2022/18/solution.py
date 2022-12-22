from collections import deque


def parse_data():
    with open("2022/18/input.txt") as f:
        data = f.read()

    return {tuple(int(coord) for coord in coords.split(",")) for coords in data.splitlines()}


def neighbors(x, y, z):
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


def part_one(data):
    return sum(neighbor not in data for cube in data for neighbor in neighbors(*cube))


def part_two(data):
    surface = set()
    surface_area = 0
    bound = max(max(coords) for coords in data) + 1

    for cube in data:
        for neighbor in neighbors(*cube):
            if neighbor in data:
                continue

            open_neighbors = deque([neighbor])
            visited = set()

            while open_neighbors:
                n = open_neighbors.popleft()

                if n in surface or any(coord == bound for coord in n):
                    surface.update(visited)
                    surface_area += 1
                    break

                for neighbor in neighbors(*n):
                    if neighbor not in visited and neighbor not in data:
                        visited.add(neighbor)
                        open_neighbors.append(neighbor)

    return surface_area


def main():
    data = parse_data()

    print(f"Day 18 Part 01: {part_one(data)}")
    print(f"Day 18 Part 02: {part_two(data)}")
