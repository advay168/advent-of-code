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


def dijkstra(grid):
    height = len(grid)
    width = len(grid[0])
    unvisited = set()
    for y in range(height):
        for x in range(width):
            unvisited.add((x, y))
    distances = {}
    for vertex in unvisited:
        distances[vertex] = float("inf")
    distances[(0, 0)] = 0
    current_x, current_y = 0, 0
    while True:
        current_cost = distances[(current_x, current_y)]
        for new_y, new_x in neighbours(height, width, current_y, current_x):
            if (new_x, new_y) not in unvisited:
                continue
            through_current_cost = grid[new_y][new_x]
            previous_cost = distances[(new_x, new_y)]
            distances[(new_x, new_y)] = min(
                through_current_cost + current_cost, previous_cost
            )
        unvisited.remove((current_x, current_y))
        if (width - 1, height - 1) == (current_x, current_y):
            return distances[(width - 1, height - 1)]
        min_till_now = float("inf")
        for unvis in unvisited:
            dist = distances[unvis]
            if dist < min_till_now:
                current_x, current_y = unvis
                min_till_now = dist


grid = []
for line in data:
    grid.append(list(map(int, line)))


print(dijkstra(grid))
