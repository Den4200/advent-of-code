import operator

from sympy import Eq, Symbol, solve

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "=": Eq,
}


def parse_data():
    with open("2022/21/input.txt") as f:
        data = f.read()

    return {
        (parts := line.split(": "))[0]: int(parts[1])
        if parts[1].isdigit() else parts[1].split()
        for line in data.splitlines()
    }


def yell(equations):
    numbers = {k: v for k, v in equations.items() if not isinstance(v, list)}

    stack = ["root"]
    while stack:
        name = stack.pop()
        eq = equations[name]

        if eq[0] in numbers and eq[2] in numbers:
            numbers[name] = OPERATORS[eq[1]](
                numbers[eq[0]],
                numbers[eq[2]]
            )
            continue

        stack.append(name)
        if eq[0] not in numbers:
            stack.append(eq[0])
        if eq[2] not in numbers:
            stack.append(eq[2])

    return numbers["root"]


def part_one(data):
    return round(yell(data))


def part_two(data):
    data["root"][1] = "="
    data["humn"] = Symbol("humn")

    return round(solve(yell(data))[0])


def main():
    data = parse_data()

    print(f"Day 21 Part 01: {part_one(data)}")
    print(f"Day 21 Part 02: {part_two(data)}")
