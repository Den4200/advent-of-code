CHUNKS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SYNTAX_ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_data():
    with open('2021/10/input.txt') as f:
        data = f.read()

    return data.splitlines()


def part_one(data):
    syntax_error_score = 0
    for line in data:
        queue = []

        for char in line:
            if char in CHUNKS:
                queue.append(CHUNKS[char])
            elif char == queue[-1]:
                queue.pop()
            else:
                syntax_error_score += SYNTAX_ERROR_SCORES[char]
                break

    return syntax_error_score


def part_two(data):
    totals = []
    for line in data:
        queue = []

        for char in line:
            if char in CHUNKS:
                queue.append(CHUNKS[char])
            elif char == queue[-1]:
                queue.pop()
            else:
                break
        else:
            total = 0
            for c in reversed(queue):
                total = total * 5 + COMPLETION_POINTS[c]

            totals.append(total)

    return sorted(totals)[len(totals) // 2]


def main():
    data = parse_data()

    print(f'Day 10 Part 01: {part_one(data)}')
    print(f'Day 10 Part 02: {part_two(data)}')
