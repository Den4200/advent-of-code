CHUNKS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SYNTAX_ERROR_POINTS = {
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
    score = 0
    for line in data:
        stack = []

        for char in line:
            if char in CHUNKS:
                stack.append(CHUNKS[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                score += SYNTAX_ERROR_POINTS[char]
                break

    return score


def part_two(data):
    scores = []
    for line in data:
        stack = []

        for char in line:
            if char in CHUNKS:
                stack.append(CHUNKS[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                break
        else:
            score = 0
            for c in stack[::-1]:
                score = score * 5 + COMPLETION_POINTS[c]

            scores.append(score)

    return sorted(scores)[len(scores) // 2]


def main():
    data = parse_data()

    print(f'Day 10 Part 01: {part_one(data)}')
    print(f'Day 10 Part 02: {part_two(data)}')
