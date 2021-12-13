from functools import partial


with open("./input.txt") as file:
    data = file.read().splitlines()

points = []
folds = []
for line in data:
    if line.startswith("fold"):
        l = line.removeprefix("fold along ")
        axis, val = l.split("=")
        if axis == "x":
            folds.append((int(val), 0))
        else:
            folds.append((0, int(val)))
    else:
        if line:
            x, y = line.split(",")
            points.append((int(x), int(y)))


def fold_point(fold, pt):
    x, y = pt
    a, b = fold
    if a:
        return (a - abs(x - a), y)
    return (x, b - abs(y - b))


for fold in folds:
    points = map(partial(fold_point, fold), points)

points = list(points)
max_x = max_y = 0
for x, y in points:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for x, y in points:
    grid[y][x] = 1

for row in grid:
    for cell in row:
        if cell:
            print("@", end="")
        else:
            print(" ", end="")
    print()
