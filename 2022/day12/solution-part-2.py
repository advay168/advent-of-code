import heapq

with open("./input.txt") as file:
    data = file.read().splitlines()

grid = []
start = (0, 0)
end = (0, 0)
for line in data:
    grid.append([ord(char) for char in line.replace("S", "a")])
    if ord("E") in grid[-1]:
        end = (grid[-1].index(ord("E")), len(grid) - 1)
        grid[-1][end[0]] = ord("z")


def neighbours(height, width, i, j):
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i + 1 < width:
        yield (i + 1, j)
    if j + 1 < height:
        yield (i, j + 1)


def dijkstra(grid, starts, end):
    height = len(grid)
    width = len(grid[0])
    distances = [[float("inf")] * width for _ in range(height)]
    queue = []
    for start in starts:
        distances[start[1]][start[0]] = 0
        heapq.heappush(queue, (0, start[0], start[1], 0))
    while True:
        current_cost, current_x, current_y, s = heapq.heappop(queue)
        if (current_x, current_y) == end:
            return s
        for x, y in neighbours(height, width, current_x, current_y):
            d = current_cost + grid[y][x]
            if d < distances[y][x] and grid[y][x] <= 1 + grid[current_y][current_x]:
                distances[y][x] = d
                heapq.heappush(queue, (d, x, y, s + 1))


s = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == ord("a"):
            s.append((x, y))
print(dijkstra(grid, s, end))
