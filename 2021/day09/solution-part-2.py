with open("./input.txt") as file:
    data = file.read().splitlines()


def neighbours(grid, i, j):
    height = len(grid)
    width = len(grid[0])
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i + 1 < height:
        yield (i + 1, j)
    if j + 1 < width:
        yield (i, j + 1)


def get_count(grid, seen, i, j) -> int:
    if seen[i][j]:
        return 0
    if grid[i][j] == 9:
        return 0
    seen[i][j] = True
    s = 1
    for i_, j_ in neighbours(grid, i, j):
        s += get_count(grid, seen, i_, j_)
    return s


grid = [[int(x) for x in line] for line in data]
seen = [[False for _ in grid[0]] for _ in grid]
sizes = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        x = grid[i][j]
        if all(x < grid[i_][j_] for i_, j_ in neighbours(grid, i, j)):
            sizes.append(get_count(grid, seen, i, j))
x = sorted(sizes)
a = x[-1]
b = x[-2]
c = x[-3]
print(a * b * c)
