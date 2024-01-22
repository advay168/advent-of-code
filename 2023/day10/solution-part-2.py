with open("./input.txt") as file:
    data = file.read().splitlines()

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

SHADED = 1
UNSHADED = 0
grid = [[UNSHADED] * 2 * w for _ in range(2 * h)]
w, h = 2 * w, 2 * h

for (x0, y0), (x1, y1) in zip(path, path[1:] + [start]):
    # Shade current and cell in path to next
    grid[y0 + y0][x0 + x0] = SHADED
    grid[y0 + y1][x0 + x1] = SHADED

grid = [[UNSHADED] * w] * 2 + grid + [[UNSHADED] * w] * 2
grid = [[UNSHADED] * 2 + row + [UNSHADED] * 2 for row in grid]
w, h = w + 4, h + 4

to_shade = [(0, 0)]
while to_shade:
    x, y = to_shade.pop()
    grid[y][x] = SHADED
    for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= x < w and 0 <= y < h and grid[y][x] != SHADED:
            to_shade.append((x, y))

count = 0
for y in range(0, h, 2):
    for x in range(0, w, 2):
        if (
            UNSHADED
            == grid[y][x]
            == grid[y + 1][x]
            == grid[y][x + 1]
            == grid[y + 1][x + 1]
        ):
            count += 1
print(count)
