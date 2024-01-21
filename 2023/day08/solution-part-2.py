with open("./input.txt") as file:
    data = file.read().splitlines()

from itertools import cycle

directions, _, *nodes = data
directions = cycle(directions)

graph = {}
for node in nodes:
    current, steps = node.split(" = ")
    l, r = steps[1:-1].split(", ")
    graph[current] = (l, r)

currents = [node for node in graph if node[-1] == "A"]
cycles = []
for current in currents:
    steps = 0
    for dir in directions:
        steps += 1
        if dir == "R":
            current = graph[current][1]
        elif dir == "L":
            current = graph[current][0]
        if current[-1] == "Z":
            break
    cycles.append(steps)

from math import lcm
print(lcm(*cycles))
