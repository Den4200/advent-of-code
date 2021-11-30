import re


class Ticket:

    def __init__(self, values):
        self.values = values

    @classmethod
    def from_text(cls, text):
        return cls([int(value) for value in text.split(',')])


class Field:

    def __init__(self, name, x1, x2, y1, y2):
        self.name = name

        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)

    def __contains__(self, value):
        return self.x1 <= value <= self.x2 or self.y1 <= value <= self.y2

    @classmethod
    def from_text(cls, text):
        match = re.fullmatch(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', text)

        if not match:
            raise ValueError('Invalid field format!')

        return cls(*match.groups())


def parse_data():
    with open('2020/16/input.txt') as f:
        data = f.read()

    data = data.split('\n\n')

    fields = [Field.from_text(line) for line in data[0].splitlines()]
    ticket = Ticket.from_text(data[1].splitlines()[1])
    others = [Ticket.from_text(line) for line in data[2].splitlines()[1:]]

    return fields, ticket, others


def part_one(data):
    ticket_length = len(data[1].values)
    invalid_total = 0

    for ticket in data[2]:
        valid_values = 0

        for value in ticket.values:
            if any(value in field for field in data[0]):
                valid_values += 1

        if valid_values != len(ticket.values):
            for value in ticket.values:
                for field in data[0]:
                    if value not in field:
                        invalid_total += value
                        break

    return invalid_total


def part_two(data):
    ticket_length = len(data[1].values)
    valid_tickets = list()

    for ticket in data[2]:
        if all(any(value in field for field in data[0]) for value in ticket.values):
            valid_tickets.append(ticket)

    field_indices = dict()
    for field in data[0]:
        field_indices[field] = set(
            i for i in range(ticket_length)
            if all(ticket.values[i] in field for ticket in valid_tickets)
        )

    fields = dict()
    while field_indices:
        for field, indices in field_indices.items():
            if len(indices) == 1:
                index = next(iter(indices))
                fields[index] = field

                del field_indices[field]

                for indices in field_indices.values():
                    if index in indices:
                        indices.remove(index)

                break

    result = 1
    for idx, field in fields.items():
        if field.name.startswith('departure'):
            result *= data[1].values[idx]

    return result


def main():
    data = parse_data()

    print(f'Day 16 Part 01: {part_one(data)}')
    print(f'Day 16 Part 02: {part_two(data)}')
