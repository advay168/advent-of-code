with open("./input.txt") as file:
    data = file.read().splitlines()


def turn(grid):
    for row in grid:
        for i in range(1, len(row)):
            if row[i] != "O":
                continue
            while i > 0 and row[i - 1] == ".":
                row[i] = "."
                row[i - 1] = "O"
                i -= 1


def cycle(grid):
    grid = [list(l) for l in zip(*grid)]
    turn(grid)

    grid = [list(l) for l in zip(*grid)]
    turn(grid)

    grid = [list(l) for l in zip(*grid[::-1])]
    turn(grid)

    grid = [list(l)[::-1] for l in zip(*grid)][::-1]
    turn(grid)

    grid = [row[::-1] for row in grid]
    return grid


def memoize(grid, turn, cache):
    grid = tuple(tuple(row) for row in grid)
    if grid in cache:
        prev = cache[grid]
        period = turn - prev
        for _ in range(1, (1_000_000_000 - turn) % period):
            grid = cycle(grid)
        s = 0
        for row in [*zip(*grid)]:
            for i in range(len(row)):
                s += (row[i] == "O") * (len(row) - i)
        print(s)
        return True
    cache[grid] = turn
    return False


cache = {}
grid = [row for row in data]
for i in range(1_000_000_000):
    grid = cycle(grid)
    if memoize(grid, i, cache):
        break
