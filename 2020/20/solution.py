import re
from collections import defaultdict
from itertools import product

import networkx as nx
import numpy as np
from scipy.ndimage import convolve


LOCHNESS = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
)


def parse_data():
    with open('2020/20/input.txt') as f:
        data = f.read()

    data = [
        re.fullmatch(r'Tile (\d+):\n([#\.\n]+)', tile).groups()
        for tile in data.split('\n\n') if tile
    ]

    return {
        int(tile_id): np.array([
            [int(char == '#') for char in line]
            for line in tile.splitlines()
        ])
        for tile_id, tile in data
    }


def get_borders(tile):
    for i in ((0,), (..., -1), (-1,), (..., 0)):
        norm = ''.join(map(str, tile[i]))
        rev = ''.join(map(str, tile[i][::-1]))

        if int(norm) < int(rev):
            yield norm
        else:
            yield rev


def get_border_tiles(data):
    border_tiles = defaultdict(list)

    for tile_id, tile in data.items():
        for border in get_borders(tile):
            border_tiles[border].append(tile_id)

    return border_tiles


def get_orientations(tile):
    for _ in range(4):
        tile = np.rot90(tile)
        
        yield tile
        yield tile.T


def part_one(data):
    border_tiles = get_border_tiles(data)

    answer = 1
    for tile_id, tile in data.items():
        if sum(len(border_tiles[border]) for border in get_borders(tile)) == 6:
            answer *= tile_id

    return answer


def part_two(data):
    border_tiles = get_border_tiles(data)
    G = nx.Graph(border for border in border_tiles.values() if len(border) == 2)

    for node in G:
        if len(G[node]) == 2:
            break
    
    for tile in get_orientations(data[node]):
        if [len(border_tiles[border]) for border in get_borders(tile)] == [1, 2, 2, 1]:
            del data[node]
            break

    grid = {(0, 0): (node, tile)}

    for y, x in product(range(12), repeat=2):
        node, tile = grid[y, x]

        for neighbor in G[node]:
            if neighbor not in data:
                continue

            for oriented_neighbor in get_orientations(data[neighbor]):
                if np.array_equal(tile[-1], oriented_neighbor[0]):
                    grid[y + 1, x] = neighbor, oriented_neighbor

                elif np.array_equal(tile[:,-1], oriented_neighbor[:,0]):
                    grid[y, x + 1] = neighbor, oriented_neighbor

                else:
                    continue

                break

            del data[neighbor]

    image = np.block([[grid[y, x][1][1:-1,1:-1] for x in range(12)] for y in range(12)])
    lochness = np.array([[int(char == '#') for char in line] for line in LOCHNESS])

    for lochness in get_orientations(lochness):
        convolution = convolve(image, lochness, output=int, mode='constant')

        if count := (convolution == lochness.sum()).sum():
            return image.sum() - count * lochness.sum()


def main():
    data = parse_data()

    print(f'Day 20 Part 01: {part_one(data)}')
    print(f'Day 20 Part 02: {part_two(data)}')
