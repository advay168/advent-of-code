from pathlib import Path

with open(Path(__file__).parent / "./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)
sx, sy = grid[0].index("."), 0


def neighbours(x, y):
    return list(
        filter(
            lambda pos: 0 <= pos[0] < w
            and 0 <= pos[1] < h
            and grid[pos[1]][pos[0]] != "#"
            and pos not in visited,
            [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)],
        )
    )


def walk(x, y):
    if y == h - 1:
        return 1
    visited.add((x, y))
    added = [(x, y)]
    l = neighbours(x, y)
    while len(l) == 1:
        el = l[0]
        if el[1] == h - 1:
            break
        added.append(el)
        visited.add(el)
        l = neighbours(el[0], el[1])
    m = 0
    for nx, ny in l:
        path = walk(nx, ny)
        if path:
            m = max(m, path + len(added) + 1)
    for s in added:
        visited.remove(s)
    return m


visited = set()
print((walk(sx, sy)) - 1)
