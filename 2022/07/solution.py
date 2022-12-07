from functools import cached_property
import operator


def parse_data():
    with open("2022/07/input.txt") as f:
        data = f.read()

    return data.splitlines()


class Node:

    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    @cached_property
    def inner_size(self):
        return sum(child.inner_size if child.size == 0 else child.size for child in self.children)


def parse_commands(lines):
    root_node = current_node = Node("/")

    for line in lines:
        match line.split():
            case ["$", "cd", "/"]: current_node = root_node
            case ["$", "cd", ".."]: current_node = current_node.parent
            case ["$", "cd", dir]:
                for child in current_node.children:
                    if child.name == dir:
                        current_node = child
                        break
            case ["$", "ls"]: pass
            case ["dir", name]: current_node.children.append(Node(name, 0, current_node))
            case [size, name]: current_node.children.append(Node(name, int(size), current_node))

    return root_node


def filter_dirs(root_dir, compare_func, limit, dirs=None):
    if dirs is None:
        dirs = []

    for child in root_dir.children:
        if child.size == 0 and compare_func(child.inner_size, limit):
            dirs.append(child)

        filter_dirs(child, compare_func, limit, dirs)

    return dirs


def part_one(data):
    root = parse_commands(data)
    nodes = filter_dirs(root, operator.lt, 100_000)

    return sum(node.inner_size for node in nodes)


def part_two(data):
    root = parse_commands(data)
    needed_space = 30_000_000 - (70_000_000 - root.inner_size)
    nodes = filter_dirs(root, operator.gt, needed_space)

    return min(nodes, key=lambda node: node.inner_size).inner_size


def main():
    data = parse_data()

    print(f"Day 07 Part 01: {part_one(data)}")
    print(f"Day 07 Part 02: {part_two(data)}")
