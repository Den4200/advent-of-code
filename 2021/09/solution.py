from math import prod

import networkx as nx


def parse_data():
    with open('2021/09/input.txt') as f:
        data = f.read()

    G = nx.grid_graph((100, 100))

    for y, line in enumerate(data.splitlines()):
        for x, height in enumerate(line):
            G.add_node((x, y), height=int(height))

    return G


def part_one(G):
    return sum(
        G.nodes[node]["height"] + 1
        for node in G
        if all(G.nodes[node]["height"] < G.nodes[neighbor]["height"] for neighbor in G[node])
    )


def part_two(G):
    G.remove_nodes_from([node for node in G if G.nodes[node]["height"] == 9])
    return prod(sorted(len(basin) for basin in nx.connected_components(G))[-3:])


def main():
    data = parse_data()

    print(f'Day 09 Part 01: {part_one(data)}')
    print(f'Day 09 Part 02: {part_two(data)}')
