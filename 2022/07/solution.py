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

    @staticmethod
    def from_text(text, parent=None):
        parts = text.split()
        if parts[0] == "dir":
            return Node(parts[1], 0, parent)

        return Node(parts[1], int(parts[0]), parent)

    @property
    def inner_size(self):
        return sum(child.inner_size if child.size == 0 else child.size for child in self.children)


def parse_commands(lines):
    root_node = current_node = Node("/")
    index = 1

    while index < len(lines):
        parts = lines[index].split()

        if parts[1] == "cd":
            if parts[2] == "..":
                current_node = current_node.parent
            elif parts[2] == "/":
                current_node = root_node
            else:
                for child in current_node.children:
                    if child.name == parts[2]:
                        current_node = child
                        break

            index += 1
        elif parts[1] == "ls":
            while index < len(lines):
                index += 1
                try:
                    line = lines[index]
                except IndexError:
                    break

                if line[0] == "$":
                    break

                current_node.children.append(Node.from_text(line, current_node))

    return root_node


def filter_dirs(root_dir, compare_func, limit, dirs):
    for child in root_dir.children:
        if compare_func(child.size == 0 and child.inner_size, limit):
            dirs.append(child)

        filter_dirs(child, compare_func, limit, dirs)

    return dirs


def part_one(data):
    root = parse_commands(data)
    nodes = filter_dirs(root, operator.lt, 100000, [])

    return sum(node.inner_size for node in nodes)


def part_two(data):
    root = parse_commands(data)
    needed_space = 30000000 - (70000000 - root.inner_size)
    nodes = filter_dirs(root, operator.gt, needed_space, [])

    return min(nodes, key=lambda node: node.inner_size).inner_size


def main():
    data = parse_data()

    print(f"Day 07 Part 01: {part_one(data)}")
    print(f"Day 07 Part 02: {part_two(data)}")
