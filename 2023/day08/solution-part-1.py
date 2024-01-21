with open("./input.txt") as file:
    data = file.read().splitlines()

from itertools import cycle

directions, _, *nodes = data
directions = cycle(directions)

graph = {}
for node in nodes:
    current, steps = node.split(" = ")
    l, r = steps[1:-1].split(", ")
    graph[current] = {"L": l, "R": r}

current = "AAA"
steps = 0
for dir in directions:
    steps += 1
    current = graph[current][dir]
    if current == "ZZZ":
        break
print(steps)
