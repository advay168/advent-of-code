import heapq

with open("./input.txt") as file:
    data = file.read().splitlines()


def neighbours(height, width, i, j):
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i + 1 < height:
        yield (i + 1, j)
    if j + 1 < width:
        yield (i, j + 1)


def convert(val):
    n = [[0 for _ in range(5)] for _ in range(5)]
    n[0][0] = val
    for i in range(5):
        for j in range(5):
            if i == j == 0:
                continue
            if n[i - 1][j]:
                n[i][j] = n[i - 1][j] % 9 + 1
            else:
                n[i][j] = n[i][j - 1] % 9 + 1
    return n


def dijkstra(grid):
    width = len(grid)
    height = len(grid[0])
    distances = [[float("inf") for _ in range(width * 5)] for _ in range(height * 5)]
    distances[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while True:
        current_cost, current_x, current_y = heapq.heappop(queue)
        if (current_y, current_x) == (height - 1, width - 1):
            return current_cost
        for x, y in neighbours(height, width, current_x, current_y):
            d = current_cost + grid[y][x]
            if d < distances[y][x]:
                distances[y][x] = d
                heapq.heappush(queue, (d, x, y))


grid = []
sub_grids = []
for line in data:
    grid.append(list(map(int, line)))
    sub_grids.append([])
    for cell in grid[-1]:
        sub_grids[-1].append(convert(cell))

width = len(grid[0])
height = len(grid)


def at(y, x):
    sub_grid_x = x % width
    sub_grid_y = y % height
    j = x // width
    i = y // height
    return sub_grids[sub_grid_y][sub_grid_x][i][j]


new_grid = [[0 for _ in range(width * 5)] for _ in range(height * 5)]
for i in range(height * 5):
    for j in range(width * 5):
        new_grid[i][j] = at(i, j)

print(dijkstra(new_grid))
