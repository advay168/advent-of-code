import heapq

with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[int(cell) for cell in row] for row in data]
w, h = len(grid[0]), len(grid)



def dijkstra(start, goal):
    sx, sy = start
    frontier = [(0, (sx, sy, (1, 0), 0)), (0, (sx, sy, (0, 1), 0))]
    seen = set()

    while frontier:
        d, node = heapq.heappop(frontier)
        if node in seen:
            continue
        x, y, (dx, dy), straight_steps = node
        if (x, y) == goal:
            return d

        seen.add(node)
        neighbours = []
        if straight_steps < 3:
            neighbours.append((x + dx, y + dy, (dx, dy), straight_steps + 1))
        if dy != 0:
            neighbours.append((x + 1, y, (1, 0), 1))
            neighbours.append((x - 1, y, (-1, 0), 1))
        if dx != 0:
            neighbours.append((x, y + 1, (0, 1), 1))
            neighbours.append((x, y - 1, (0, -1), 1))

        for n in filter(lambda pos: 0 <= pos[0] < w and 0 <= pos[1] < h, neighbours):
            nx, ny, _, _ = n
            weight = grid[ny][nx]
            if n not in seen:
                heapq.heappush(frontier, (d + weight, n))
    assert False, "Not Found"


start = (0, 0)
goal = (w - 1, h - 1)
print(dijkstra(start, goal))
