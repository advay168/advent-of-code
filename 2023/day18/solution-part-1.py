import sys

with open("./input.txt") as file:
    data = file.read().splitlines()

plan = []
for line in data:
    d, n, _ = line.split()
    plan.append((d, int(n)))

cx, cy = 0, 0
ground = {}
ground[(cx, cy)] = "#"
for op, n in plan:
    match op:
        case "U":
            for _ in range(n):
                cy -= 1
                ground[(cx, cy)] = "#"
        case "D":
            for _ in range(n):
                cy += 1
                ground[(cx, cy)] = "#"
        case "L":
            for _ in range(n):
                cx -= 1
                ground[(cx, cy)] = "#"
        case "R":
            for _ in range(n):
                cx += 1
                ground[(cx, cy)] = "#"

max_x = max_y = 0
min_x = min_y = 1000000
for cx, cy in ground:
    max_x = max(max_x, cx)
    min_x = min(min_x, cx)
    max_y = max(max_y, cy)
    min_y = min(min_y, cy)

grid = []
for y in range(min_y, max_y + 1):
    r = []
    for x in range(min_x, max_x + 1):
        if (x, y) in ground:
            r.append("#")
        else:
            r.append(".")
    grid.append(r)

w, h = len(grid[0]), len(grid)
grid = [["."] * w] + grid + [["."] * w]
grid = [(["."] + row + ["."]) for row in grid]
w = 1 + w + 1
h = 1 + h + 1


def floodfill(grid, x, y, seen):
    if (x, y) in seen:
        return
    grid[y][x] = "@"
    seen.add((x, y))
    for x, y in filter(
        lambda pos: 0 <= pos[0] < w and 0 <= pos[1] < h,
        [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)],
    ):
        if grid[y][x] == "#":
            continue
        floodfill(grid, x, y, seen)


sys.setrecursionlimit(1000000)
floodfill(grid, 0, 0, set())

print(sum(sum(cell != "@" for cell in row) for row in grid))
