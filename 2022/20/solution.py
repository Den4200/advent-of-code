class Node:

    def __init__(self, value, next=None, left=None, right=None):
        self.value = value
        self.next = next
        self.left = left
        self.right = right

    def __rshift__(self, other):
        self.right = other
        other.left = self
        return other


def parse_data():
    with open("2022/20/input.txt") as f:
        data = f.read()

    nums = [Node(int(num)) for num in data.splitlines()]
    for n1, n2 in zip(nums, nums[1:]):
        n1.next = n2
        n1 >> n2

    nums[-1] >> nums[0]
    return nums[0], len(nums) - 1


def mix(root, length):
    current = root

    while current is not None:
        current.left >> current.right
        dist = current.value % length

        if dist > 0:
            for _ in range(dist):
                current.right = current.right.right
            current.left = current.right.left

        elif dist < 0:
            for _ in range(length - dist):
                current.left = current.left.left
            current.right = current.left.right

        current.left >> current >> current.right
        current = current.next


def grove_coordinates_sum(root):
    current = root

    while current.value != 0:
        current = current.right

    gcsum = 0
    for _ in range(3):
        for _ in range(1000):
            current = current.right

        gcsum += current.value

    return gcsum


def part_one(data):
    root, length = data
    mix(root, length)
    return grove_coordinates_sum(root)


def part_two(data):
    root, length = data

    current = root
    while current is not None:
        current.value *= 811589153
        current = current.next

    for _ in range(10):
        mix(root, length)

    return grove_coordinates_sum(root)


def main():
    data = parse_data()

    print(f"Day 20 Part 01: {part_one(data)}")
    print(f"Day 20 Part 02: {part_two(data)}")
