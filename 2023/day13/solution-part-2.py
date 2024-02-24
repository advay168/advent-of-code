with open("./input.txt") as file:
    data = file.read()

def is_reflection_line(grid, y):
    a, b = y - 1, y
    s = 0
    while a >= 0 and b < len(grid):
        for p, q in zip(grid[a], grid[b]):
            s += p != q
        a -= 1
        b += 1
    return s == 1

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
