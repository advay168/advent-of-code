with open("./input.txt") as file:
    data = file.read().splitlines()


def neighbours(grid, i, j):
    height = len(grid)
    width = len(grid[0])
    if i > 0:
        yield grid[i - 1][j]
    if j > 0:
        yield grid[i][j - 1]
    if i + 1 < height:
        yield grid[i + 1][j]
    if j + 1 < width:
        yield grid[i][j + 1]


grid = [[int(x) for x in line] for line in data]
sum_ = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        x = grid[i][j]
        if all(x < neighbour for neighbour in neighbours(grid, i, j)):
            sum_ += x + 1
print(sum_)
