from collections import defaultdict
import re

import networkx as nx


def parse_data():
    with open("2022/16/input.txt") as f:
        data = f.read()

    parsed = re.findall(
        r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)",
        data,
    )

    G = nx.Graph()
    flow_rates = {"AA": 0}
    for valve in parsed:
        if (flow_rate := int(valve[1])) > 0:
            flow_rates[valve[0]] = flow_rate

        for tun in valve[2].split(", "):
            G.add_edge(valve[0], tun)

    graph = defaultdict(list)
    for source in flow_rates:
        for dest in flow_rates:
            graph[source].append((dest, nx.shortest_path_length(G, source, dest) + 1))

    return graph, flow_rates


def find_max_pressure(valve, graph, flow_rates, visited, minutes, elephant=False, memo=None):
    if memo is None:
        memo = {}

    state = (valve, visited, minutes, elephant)
    if state in memo:
        return memo[state]

    if minutes == 0:
        if elephant:
            return find_max_pressure(
                "AA",
                graph,
                flow_rates,
                visited,
                26,
                elephant=False,
                memo=memo,
            )
        return 0

    best_pressure = 0
    for dest, dist in graph[valve]:
        if dist >= minutes or dest in visited:
            continue

        pressure = find_max_pressure(
            dest,
            graph,
            flow_rates,
            visited | {dest},
            minutes - dist,
            elephant,
            memo,
        ) + flow_rates[dest] * (minutes - dist)

        best_pressure = max(best_pressure, pressure)

    if elephant and best_pressure == 0:
        return find_max_pressure("AA", graph, flow_rates, visited, 26, elephant=False, memo=memo)

    memo[state] = best_pressure
    return best_pressure


def part_one(data):
    return find_max_pressure("AA", *data, frozenset(["AA"]), 30)


def part_two(data):
    return find_max_pressure("AA", *data, frozenset(["AA"]), 26, elephant=True)


def main():
    data = parse_data()

    print(f"Day 16 Part 01: {part_one(data)}")
    print(f"Day 16 Part 02: {part_two(data)}")
