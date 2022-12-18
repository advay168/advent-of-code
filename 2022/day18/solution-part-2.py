with open("./input.txt") as file:
    data = file.read().splitlines()

cubes = set()
max_size = 0
for line in data:
    x, y, z = map(int, line.split(","))
    cubes.add((x, y, z))
    max_size = max([max_size, x, y, z])
max_size += 2


def neighbours(vertex):
    x, y, z = vertex
    def f():
        yield (x - 1, y, z)
        yield (x + 1, y, z)
        yield (x, y - 1, z)
        yield (x, y + 1, z)
        yield (x, y, z - 1)
        yield (x, y, z + 1)
    for v in f():
        if all(-2 <= dim < max_size for dim in v):
            yield v


visited = set()

def dfs(current):
    visited.add(current)
    count = 0
    for neighbour in neighbours(current):
        if neighbour in visited:
            continue
        if neighbour in cubes:
            count += 1
        else:
            count += dfs(neighbour)
    return count

import sys
sys.setrecursionlimit(10000)
print("This stack overflows on my machine so if it crashes without warning it won't work")
print(dfs((0, 0, 0)))
