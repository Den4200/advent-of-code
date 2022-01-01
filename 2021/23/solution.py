import re
from copy import deepcopy
from heapq import heappop, heappush

PART_TWO_INSERTIONS = {
    'A': ['D', 'D'],
    'B': ['C', 'B'],
    'C': ['B', 'A'],
    'D': ['A', 'C'],
}


class Burrow:
    AMPHIPODS = {
        "A": 1,
        "B": 10,
        "C": 100,
        "D": 1000,
    }

    PATHS = {
        0: {
            "A": [0, 1],
            "B": [0, 1, 2],
            "C": [0, 1, 2, 3],
            "D": [0, 1, 2, 3, 4],
        },
        1: {
            "A": [1],
            "B": [1, 2],
            "C": [1, 2, 3],
            "D": [1, 2, 3, 4],
        },
        2: {
            "A": [2],
            "B": [2],
            "C": [2, 3],
            "D": [2, 3, 4],
        },
        3: {
            "A": [3, 2],
            "B": [3],
            "C": [3],
            "D": [3, 4],
        },
        4: {
            "A": [4, 3, 2],
            "B": [4, 3],
            "C": [4],
            "D": [4],
        },
        5: {
            "A": [5, 4, 3, 2],
            "B": [5, 4, 3],
            "C": [5, 4],
            "D": [5],
        },
        6: {
            "A": [6, 5, 4, 3, 2],
            "B": [6, 5, 4, 3],
            "C": [6, 5, 4],
            "D": [6, 5],
        },
    }

    def __init__(self, state, cost=0):
        self.state = state
        self.cost = cost

    def __hash__(self):
        return hash(tuple(tuple(v) for v in self.state.values()))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.cost < other.cost

    @property
    def is_organized(self):
        return all(all(amph1 == amph2 for amph2 in self.state[amph1]) for amph1 in self.AMPHIPODS)

    @property
    def possible_moves(self):
        for hallway_pos, amphipod in enumerate(self.state["H"]):
            if amphipod and self.is_room_open(amphipod) and self.is_path_clear(hallway_pos, amphipod):
                room_pos = self.find_room_spot(amphipod)
                new_burrow = self.copy()
                new_burrow.move("H", hallway_pos, amphipod, room_pos)
                return [new_burrow]

        possible_states = []
        for room in self.AMPHIPODS:
            if not self.is_room_open(room):
                amphipod = [a for a in self.state[room] if a][0]
                room_pos = self.state[room].index(amphipod)

                for hallway_pos in self.PATHS:
                    if not self.state["H"][hallway_pos] and self.is_path_clear(hallway_pos, room):
                        new_burrow = self.copy()
                        new_burrow.move(room, room_pos, "H", hallway_pos)
                        possible_states.append(new_burrow)

        return possible_states

    @property
    def organized(self):
        open = [self]
        closed = set()

        while open:
            burrow = heappop(open)

            if burrow.is_organized:
                return burrow
            elif burrow not in closed:
                for move in burrow.possible_moves:
                    heappush(open, move)

                closed.add(burrow)

    def is_room_open(self, room):
        return all(a in (None, room) for a in self.state[room])

    def find_room_spot(self, room):
        return len(self.state[room]) - 1 - self.state[room][::-1].index(None)

    def is_path_clear(self, hallway_pos, room):
        for pos in self.PATHS[hallway_pos][room]:
            if pos != hallway_pos and self.state["H"][pos]:
                return False

        return True

    def calc_move_cost(self, hallway_pos, room, room_pos, amphipod):
        distance = len(self.PATHS[hallway_pos][room]) * 2 + room_pos

        if hallway_pos in (0, 6):
            distance -= 1

        return distance * self.AMPHIPODS[amphipod]

    def move(self, room0, pos0, room, pos):
        if room0 == "H":
            self.cost += self.calc_move_cost(pos0, room, pos, room)
        else:
            self.cost += self.calc_move_cost(pos, room0, pos0, self.state[room0][pos0])

        self.state[room][pos] = self.state[room0][pos0]
        self.state[room0][pos0] = None

    def copy(self):
        return Burrow(deepcopy(self.state), self.cost)


def parse_data():
    with open('2021/23/input.txt') as f:
        data = f.read()

    amphipods = re.findall(r"[A-D]", data)
    return {
        "H": [None] * 7,
        "A": [amphipods[0], amphipods[4]],
        "B": [amphipods[1], amphipods[5]],
        "C": [amphipods[2], amphipods[6]],
        "D": [amphipods[3], amphipods[7]],
    }


def part_one(data):
    return Burrow(data).organized.cost


def part_two(data):
    for room, insertions in PART_TWO_INSERTIONS.items():
        data[room] = [data[room][0], *insertions, data[room][1]]

    return Burrow(data).organized.cost


def main():
    data = parse_data()

    print(f'Day 23 Part 01: {part_one(data)}')
    print(f'Day 23 Part 02: {part_two(data)}')
