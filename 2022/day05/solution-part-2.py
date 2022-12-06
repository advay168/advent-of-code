import re

with open("./input.txt") as file:
    data = file.read()


def parse_row(line):
    return re.findall(r".(.). ?", line)


def create_stacks(parsed_lines):
    stacks = []
    for column in zip(*parsed_lines):
        stacks.append([x for x in reversed(column) if x != " "])
    return stacks


def parse_move(line):
    match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    return tuple(map(int, match.groups()))


first, second = map(str.splitlines, data.split("\n\n"))
parsed = [parse_row(line) for line in first[:-1]]
stacks = create_stacks(parsed)

for num, frm, to in map(parse_move, second):
    stacks[to - 1].extend(stacks[frm - 1][-num:])
    del stacks[frm - 1][-num:]
print("".join(s[-1] for s in stacks))
