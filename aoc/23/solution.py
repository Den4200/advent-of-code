from collections import deque
from itertools import islice


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def parse_data():
    with open('aoc/23/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.strip()]


def part_one(data):
    cups = deque(data)

    for i in range(100):
        current = cups[i % len(cups)]

        cups.rotate(-cups.index(current))

        choices = [cups[j] for j in range(1, 4)]
        for choice in choices:
            cups.remove(choice)

        dest = current - 1
        min_cups = min(cups)
        while dest not in cups:
            if dest < min_cups:
                dest = max(cups)
            else:
                dest -= 1

        for idx, choice in enumerate(choices, start=cups.index(dest) + 1):
            cups.insert(idx, choice)

        cups.rotate(i % len(cups))

    cups.rotate(-cups.index(1))

    return ''.join(str(cup) for cup in islice(cups, 1, len(cups)))


def part_two(data):
    nodes = {i: Node(i) for i in range(1, 1_000_001)}

    for current, next_ in zip(data, data[1:]):
        nodes[current].next = nodes[next_]

    if len(data) == 1_000_000:
        nodes[data[-1]].next = nodes[data[0]]
    else:
        nodes[data[-1]].next = nodes[len(data) + 1]

        for i in range(len(data) + 1, 1_000_000):
            nodes[i].next = nodes[i + 1]

        nodes[1_000_000].next = nodes[data[0]]

    head = nodes[data[0]]

    for _ in range(10_000_000):
        start = head.next
        end = head.next.next.next

        dest = head.value - 1 if head.value > 1 else 1_000_000

        while dest in (start.value, start.next.value, end.value):
            dest -= 1

            if dest == 0:
                dest = 1_000_000

        head.next = end.next
        end.next = nodes[dest].next
        nodes[dest].next = start

        head = head.next

    return nodes[1].next.value * nodes[1].next.next.value


def main():
    data = parse_data()

    print(f'Day 23 Part 01: {part_one(data)}')
    print(f'Day 23 Part 02: {part_two(data)}')
