from collections import namedtuple
from math import prod
import re

Blueprint = namedtuple(
    "Blueprint",
    "id ore_robot_cost clay_robot_cost obsidian_robot_ore_cost obsidian_robot_clay_cost "
    "geode_robot_ore_cost geode_robot_obsidian_cost"
)

State = namedtuple(
    "State",
    "ores clay obsidian ore_robots clay_robots obsidian_robots minutes_left"
)


def parse_data():
    with open("2022/19/input.txt") as f:
        data = f.read()

    return [
        Blueprint(*(int(num) for num in re.findall(r"(\d+)", line)))
        for line in data.splitlines()
    ]


def find_max_geodes(blueprint, duration):
    memo = {}
    initial_state = State(0, 0, 0, 1, 0, 0, duration)

    max_ore_robots = max(
        blueprint.ore_robot_cost,
        blueprint.clay_robot_cost,
        blueprint.obsidian_robot_ore_cost
    )
    max_clay_robots = blueprint.obsidian_robot_clay_cost
    max_obsidian_robots = blueprint.geode_robot_obsidian_cost

    def solve(state):
        nonlocal memo

        if state.minutes_left == 0:
            return 0

        if state in memo:
            return memo[state]

        new_ores = state.ores + state.ore_robots
        new_clay = state.clay + state.clay_robots
        new_obsidian = state.obsidian + state.obsidian_robots

        best = solve(State(new_ores, new_clay, new_obsidian, *state[3:-1], state.minutes_left - 1))

        if state.ores >= blueprint.ore_robot_cost and state.ore_robots < max_ore_robots:
            best = max(
                best,
                solve(State(
                    new_ores - blueprint.ore_robot_cost,
                    new_clay,
                    new_obsidian,
                    state.ore_robots + 1,
                    state.clay_robots,
                    state.obsidian_robots,
                    state.minutes_left - 1
                ))
            )

        if state.ores >= blueprint.clay_robot_cost and state.clay_robots < max_clay_robots:
            best = max(
                best,
                solve(State(
                    new_ores - blueprint.clay_robot_cost,
                    new_clay,
                    new_obsidian,
                    state.ore_robots,
                    state.clay_robots + 1,
                    state.obsidian_robots,
                    state.minutes_left - 1
                ))
            )

        if (
            state.ores >= blueprint.obsidian_robot_ore_cost
            and state.clay >= blueprint.obsidian_robot_clay_cost
            and state.obsidian_robots < max_obsidian_robots
        ):
            best = max(
                best,
                solve(State(
                    new_ores - blueprint.obsidian_robot_ore_cost,
                    new_clay - blueprint.obsidian_robot_clay_cost,
                    new_obsidian,
                    state.ore_robots,
                    state.clay_robots,
                    state.obsidian_robots + 1,
                    state.minutes_left - 1
                ))
            )

        if (
            state.ores >= blueprint.geode_robot_ore_cost
            and state.obsidian >= blueprint.geode_robot_obsidian_cost
        ):
            best = max(
                best,
                state.minutes_left - 1 + solve(State(
                    new_ores - blueprint.geode_robot_ore_cost,
                    new_clay,
                    new_obsidian - blueprint.geode_robot_obsidian_cost,
                    *state[3:-1],
                    state.minutes_left - 1
                ))
            )

        memo[state] = best
        return best

    return solve(initial_state)


def part_one(data):
    return sum(blueprint.id * find_max_geodes(blueprint, 24) for blueprint in data)


def part_two(data):
    return prod(find_max_geodes(blueprint, 32) for blueprint in data[:3])


def main():
    data = parse_data()

    print(f"Day 19 Part 01: {part_one(data)}")
    print(f"Day 19 Part 02: {part_two(data)}")
