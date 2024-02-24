with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)
sx, sy = 0, 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            sx, sy = x, y
            grid[y][x] = "."

def neighbours(x, y):
    yield (x - 1, y)
    yield (x + 1, y)
    yield (x, y - 1)
    yield (x, y + 1)

from functools import cache

@cache
def reachable_from(x, y, steps):
    if steps == 0:
        return {(x, y)}
    ret = set()
    for x, y in filter(lambda pos:0<= pos[0] < w and 0 <= pos[1] < h, neighbours(x, y)):
        if grid[y][x] != "#":
            ret |= reachable_from(x, y, steps - 1)
    return ret

print(len(reachable_from(sx, sy, 64)))
