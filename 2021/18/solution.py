import json
import operator
from abc import ABC, abstractmethod, abstractproperty
from functools import reduce
from itertools import permutations
from math import ceil, floor, inf


class SnailfishNumber(ABC):

    @abstractmethod
    def copy(self):
        pass

    @abstractproperty
    def magnitude(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Number(SnailfishNumber):

    def __init__(self, value):
        self.value = value

        self.leftmost = self
        self.rightmost = self

        self.leftn = None
        self.rightn = None

        self.parent = None

    def __repr__(self):
        return str(self.value)

    def copy(self):
        return Number(self.value)

    @property
    def magnitude(self):
        return self.value

    def update(self):
        pass


class Pair(SnailfishNumber):

    def __init__(self, left, right):
        self.parent = None
        self.side = None

        self._left = left
        self._right = right

        self.left = left
        self.right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left
        self.left.parent = self
        self.left.side = 0
        self.leftmost = self.left.leftmost
        self.left.rightmost.rightn = self.right.leftmost

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right
        self.right.parent = self
        self.right.side = 1
        self.rightmost = self.right.rightmost
        self.right.leftmost.leftn = self.left.rightmost

    @property
    def depth(self):
        if self.parent is None:
            return 0

        return self.parent.depth + 1

    @property
    def magnitude(self):
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    @classmethod
    def from_raw(cls, raw):
        if isinstance(raw, str):
            raw = json.loads(raw)

        if isinstance(raw, list):
            return Pair(*map(Pair.from_raw, raw))

        return Number(raw)

    def copy(self):
        return Pair(self.left.copy(), self.right.copy())

    def reduce(self):
        while explode(self) or split(self):
            pass

    def update(self):
        self.left.update()
        self.right.update()

        self.leftmost = self.left.leftmost
        self.rightmost = self.right.rightmost

        self.left.rightmost.rightn = self.right.leftmost
        self.right.leftmost.leftn = self.left.rightmost

    def __repr__(self):
        return f"[{self.left!r},{self.right!r}]"

    def __add__(self, pair):
        resultant = Pair(self.copy(), pair.copy())
        resultant.reduce()
        return resultant


def explode(pair, outer=None):
    if isinstance(pair, Number):
        return

    if outer is None:
        outer = pair

    if isinstance(pair.left, Number) and isinstance(pair.right, Number) and pair.depth >= 4:
        if pair.left.leftn is not None:
            pair.left.leftn.value += pair.left.value
        if pair.right.rightn is not None:
            pair.right.rightn.value += pair.right.value

        if pair.side == 0:
            pair.parent.left = Number(0)
        else:
            pair.parent.right = Number(0)

        outer.update()
        return True

    return explode(pair.left, outer) or explode(pair.right, outer)


def split(pair, outer=None):
    if outer is None:
        outer = pair

    if isinstance(pair, Pair):
        return split(pair.left, outer) or split(pair.right, outer)

    if pair.value >= 10:
        new_pair = Pair(Number(floor(pair.value / 2)), Number(ceil(pair.value / 2)))

        if pair.side == 0:
            pair.parent.left = new_pair
        else:
            pair.parent.right = new_pair

        outer.update()
        return True

    return False


def parse_data():
    with open('2021/18/input.txt') as f:
        data = f.read()

    return [Pair.from_raw(line) for line in data.splitlines()]


def part_one(data):
    return reduce(operator.add, data).magnitude


def part_two(data):
    return max((pair1 + pair2).magnitude for pair1, pair2 in permutations(data, r=2))


def main():
    data = parse_data()

    print(f'Day 18 Part 01: {part_one(data)}')
    print(f'Day 18 Part 02: {part_two(data)}')
