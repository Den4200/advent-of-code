def parse_data():
    with open("2022/02/input.txt") as f:
        data = f.read()

    return [line.split() for line in data.splitlines()]


def rps(p1, p2):
    print(p1, p2)
    if p1 == "A":
        if p2 == "X":
            return 0
        if p2 == "Y":
            return -1
        if p2 == "Z":
            return 1
    if p1 == "B":
        if p2 == "X":
            return 1
        if p2 == "Y":
            return 0
        if p2 == "Z":
            return -1
    if p1 == "C":
        if p2 == "X":
            return -1
        if p2 == "Y":
            return 1
        if p2 == "Z":
            return 0


def to_rps(move, intention):
    if move == "A":
        if intention == "X":
            return "Z"
        if intention == "Y":
            return "X"
        if intention == "Z":
            return "Y"
    if move == "B":
        if intention == "X":
            return "X"
        if intention == "Y":
            return "Y"
        if intention == "Z":
            return "Z"
    if move == "C":
        if intention == "X":
            return "Y"
        if intention == "Y":
            return "Z"
        if intention == "Z":
            return "X"


def to_value(move):
    if move in ("A", "X"):
        return 1
    if move in ("B", "Y"):
        return 2
    if move in ("C", "Z"):
        return 3


def part_one(data):
    score = 0
    for p1, p2 in data:
        score += to_value(p2)

        if rps(p2, p1) == 1:
            score += 6
        elif rps(p2, p1) == 0:
            score += 3

    return score


def part_two(data):
    score = 0
    for p1, intention in data:
        p2 = to_rps(p1, intention)
        score += to_value(p2)

        x = rps(p1, p2)
        print(x)
        if x == -1:
            score += 6
        elif x == 0:
            score += 3

        print(score)

    return score


def main():
    data = parse_data()

    print(f"Day 02 Part 01: {part_one(data)}")
    print(f"Day 02 Part 02: {part_two(data)}")
