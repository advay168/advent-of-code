with open("./input.txt") as file:
    data = file.read()


def is_reflection_line(grid, y):
    a, b = y - 1, y
    while a >= 0 and b < len(grid):
        if grid[a] != grid[b]:
            return False
        a -= 1
        b += 1
    return True

s = 0
for pattern in data.split("\n\n"):
    grid = pattern.splitlines()
    h = len(grid)
    for y in range(1, h):
        if is_reflection_line(grid, y):
            s += 100 * y
    grid = list(map("".join, zip(*grid)))
    h = len(grid)
    for y in range(1, h):
        if is_reflection_line(grid, y):
            s += y
print(s)
