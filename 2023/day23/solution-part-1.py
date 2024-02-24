with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)
sx, sy = grid[0].index("."), 0

def neighbours(x, y):
    return list(
        filter(
            lambda pos: 0 <= pos[0] < w
            and 0 <= pos[1] < h
            and grid[pos[1]][pos[0]] != "#",
            [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)],
        )
    )

def walk(x, y):
    if y == h - 1:
        return 1
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    m = 0
    for nx, ny in neighbours(x, y):
        match grid[ny][nx]:
            case "#":
                continue
            case ".":
                path = walk(nx, ny)
                if path:
                    m = max(m, path + 1)
            case ">":
                path = walk(nx + 1, ny)
                if path:
                    m = max(m, path + 2)
            case "<":
                path = walk(nx - 1, ny)
                if path:
                    m = max(m, path + 2)
            case "^":
                path = walk(nx, ny - 1)
                if path:
                    m = max(m, path + 2)
            case "v":
                path = walk(nx, ny + 1)
                if path:
                    m = max(m, path + 2)
    visited.remove((x, y))
    return m

import sys
sys.setrecursionlimit(10**6)

visited = set()
print((walk(sx, sy)) - 1)
