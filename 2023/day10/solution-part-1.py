with open("./input.txt") as file:
    data = file.read().splitlines()

connections = {}
start = None

w, h = len(data[0]), len(data)
connections = {}
start = None
for y, line in enumerate(data):
    for x, cell in enumerate(line):
        match cell:
            case "-":
                connections[(x, y)] = ((x - 1, y), (x + 1, y))
            case "|":
                connections[(x, y)] = ((x, y - 1), (x, y + 1))
            case "L":
                connections[(x, y)] = ((x, y - 1), (x + 1, y))
            case "J":
                connections[(x, y)] = ((x, y - 1), (x - 1, y))
            case "7":
                connections[(x, y)] = ((x, y + 1), (x - 1, y))
            case "F":
                connections[(x, y)] = ((x, y + 1), (x + 1, y))
            case "S":
                start = (x, y)
assert start is not None

path = [start]
current = None
for current, conns in connections.items():
    if start in conns:
        break
assert current is not None
while current != start:
    path.append(current)
    a, b = connections[current]
    current = a if b == path[-2] else b
print(len(path) // 2)
