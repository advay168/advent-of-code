with open("./input.txt") as file:
    data = file.read().splitlines()

from collections import defaultdict

vertices = defaultdict(list)
for line in data:
    a, b = line.split("-")
    if b != "start" and a != "end":
        vertices[a].append(b)
    if a != "start" and b != "end":
        vertices[b].append(a)


def walk(vertices, counts: defaultdict[str, int], vertex: str):
    if vertex == "end":
        return 1
    if vertex.islower():
        if counts[vertex] > 0:
            return 0
    counts[vertex] += 1
    s = 0
    for v in vertices[vertex]:
        s += walk(vertices, counts, v)
    counts[vertex] -= 1
    return s


print(walk(vertices, defaultdict(lambda: 0), "start"))
