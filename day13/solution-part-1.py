with open("./input.txt") as file:
    data = file.read().splitlines()
points = []
folds = []
max_x = max_y = 0
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
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for x, y in points:
    grid[y][x] = 1


def fold_point(pt, fold):
    x, y = pt
    a, b = fold
    if a:
        return (a - abs(x - a), y)
    return (x, b - abs(y - b))


def fold_grid(grid, fold):
    a, b = fold
    if a:
        grid2 = [[0 for _ in range(a + 1)] for _ in range(len(grid))]
    else:
        grid2 = [[0 for _ in range(len(grid[0]))] for _ in range(b + 1)]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            x_, y_ = fold_point((x, y), fold)
            grid2[y_][x_] += grid[y][x]
    return grid2


grid = fold_grid(grid, folds[0])
c = 0
for row in grid:
    for val in row:
        if val:
            c += 1
print(c)
