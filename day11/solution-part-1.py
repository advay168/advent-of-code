with open("./input.txt") as file:
    data = file.read().splitlines()


def neighbours(width, height, i, j):
    for y in [i - 1, i + 0, i + 1]:
        for x in [j - 1, j + 0, j + 1]:
            if 0 <= y < height and 0 <= x < width and (y, x) != (i, j):
                yield (y, x)


def step(grid, height, width):
    flashed = [[False for _ in line] for line in grid]
    flashes = 0
    for i in range(height):
        for j in range(width):
            grid[i][j] += 1
    changed = True
    while changed:
        changed = False
        for i in range(height):
            for j in range(width):
                if flashed[i][j]:
                    continue
                if grid[i][j] <= 9:
                    continue
                flashed[i][j] = True
                flashes += 1
                changed = True
                for i_, j_ in neighbours(width, height, i, j):
                    grid[i_][j_] += 1
    for i in range(height):
        for j in range(width):
            if flashed[i][j]:
                grid[i][j] = 0
    return flashes


grid = [[int(x) for x in line] for line in data]
height, width = len(grid), len(grid[0])
flashes = 0
for i in range(100):
    flashes += step(grid, height, width)
print(flashes)
