with open("./input.txt") as file:
    data = file.read().splitlines()

_: list[list[str]] = [[cell for cell in row] for row in data]

grid: list[list[tuple[int, int] | str]] = [[cell for cell in row] for row in data]
h = len(grid)
w = len(grid[0])

count = 0
for row, new_row in zip(_, grid):
    running = ""
    running_start = 0
    for i, cell in enumerate(row):
        if cell.isdigit():
            if running == "":
                running_start = i
            running += cell
        elif running != "":
            for j in range(running_start, i):
                new_row[j] = (count, int(running))
            running = ""
            count += 1
    if running != "":
        for j in range(running_start, w):
            new_row[j] = (count, int(running))


def neighbours(x_: int, y_: int):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0:
                continue
            if not (0 <= x + x_ < w):
                continue
            if not (0 <= y + y_ < h):
                continue
            yield grid[y + y_][x + x_]


nums = set()
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if isinstance(cell, str):
            continue
        for c in neighbours(j, i):
            if isinstance(c, tuple):
                continue
            if c == ".":
                continue
            nums.add(cell)
            break

print(sum(b for _, b in nums))
