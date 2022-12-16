from collections import defaultdict
from functools import cache
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


def find_max_pressure(source, dest, min1, min2, graph, flow_rates, total_flow_rate, visited, minutes):
    if minutes == 0:
        return total_flow_rate

    if min1 > 0 and min2 > 0:
        return find_max_pressure(source, dest, min1 - 1, min2 - 1, graph, flow_rates, total_flow_rate, visited, minutes - 1)

    best_flow_rate = total_flow_rate
    if min1 == 0:
        found_best = False

        for to, dist in graph[source]:
            if dist >= minutes or to in visited:
                continue

            found_best = True
            visited.add(to)

            flow_rate = find_max_pressure(
                to,
                dest,
                dist,
                min2,
                graph,
                flow_rates,
                total_flow_rate + flow_rates[to] * (minutes - dist),
                visited,
                minutes,
            )
            visited.remove(to)

            if flow_rate > best_flow_rate:
                best_flow_rate = flow_rate

        if found_best:
            return best_flow_rate

    if min2 == 0:
        for to, dist in graph[dest]:
            if dist >= minutes or to in visited:
                continue

            visited.add(to)

            flow_rate = find_max_pressure(
                source,
                to,
                min1,
                dist,
                graph,
                flow_rates,
                total_flow_rate + flow_rates[to] * (minutes - dist),
                visited,
                minutes,
            )
            visited.remove(to)

            if flow_rate > best_flow_rate:
                best_flow_rate = flow_rate

    return best_flow_rate


def part_one(data):
    return find_max_pressure("AA", "AA", 100, 0, *data, 0, {"AA"}, 30)


def part_two(data):
    return find_max_pressure("AA", "AA", 0, 0, *data, 0, {"AA"}, 26)


def main():
    data = parse_data()

    print(f"Day 16 Part 01: {part_one(data)}")
    print(f"Day 16 Part 02: {part_two(data)}")
