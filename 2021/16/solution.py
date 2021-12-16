from math import prod

TYPE_MAP = {
    0: lambda packets: sum(packets),
    1: lambda packets: prod(packets),
    2: lambda packets: min(packets),
    3: lambda packets: max(packets),
    5: lambda packets: int(packets[0] > packets[1]),
    6: lambda packets: int(packets[0] < packets[1]),
    7: lambda packets: int(packets[0] == packets[1]),
}


def parse_data():
    with open('2021/16/input.txt') as f:
        data = f.read()

    return list("".join(bin(int(h, 16))[2:].zfill(4) for h in data.strip()))


def bin_int(num):
    return int("".join(num), 2)


def parse_packets(bits, idx=0):
    vsum = bin_int(bits[idx:idx+3])
    type_id = bin_int(bits[idx+3:idx+6])
    idx += 6

    if type_id == 4:
        value = []

        while True:
            group = bits[idx:idx+5]
            idx += 5
            value += group[1:]

            if group[0] == "0":
                break

        return idx, vsum, bin_int(value)

    else:
        packets = []
        idx += 1

        if bits[idx - 1] == "0":
            bit_length = bin_int(bits[idx:idx+15])
            idx += 15

            orig_idx = idx
            while idx - orig_idx < bit_length:
                idx, version, rest = parse_packets(bits, idx)
                vsum += version
                packets.append(rest)

        else:
            subpackets = bin_int(bits[idx:idx+11])
            idx += 11

            for _ in range(subpackets):
                idx, version, rest = parse_packets(bits, idx)
                vsum += version
                packets.append(rest)

        return idx, vsum, TYPE_MAP[type_id](packets)


def part_one(data):
    return parse_packets(data)[1]


def part_two(data):
    return parse_packets(data)[2]


def main():
    data = parse_data()

    print(f'Day 16 Part 01: {part_one(data)}')
    print(f'Day 16 Part 02: {part_two(data)}')
