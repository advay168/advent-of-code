from collections import Counter, defaultdict, deque
from random import choice
from copy import deepcopy
from math import prod

with open("./input.txt") as file:
    data = file.read().splitlines()

nodes = set()
graph = defaultdict(set)
for line in data:
    name, components = line.split(": ")
    nodes.add(name)
    for c in components.split():
        graph[name].add(c)
        graph[c].add(name)
        nodes.add(c)


def shortest_path(start, end):
    queue = deque([(start, start)])
    seen = {}
    while queue:
        prev, node = queue.popleft()
        if node in seen:
            continue
        seen[node] = prev
        if node == end:
            path = []
            while node != start:
                path.append(node)
                node = seen[node]
            path.append(start)
            p = []
            for x in zip(path, path[1:]):
                a, b = sorted(x)
                p.append((a, b))
            return p
        for conn in graph[node]:
            queue.append((node, conn))


def flooder(node, marker, graph, seen):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen[node] = marker
        for conn in graph[node]:
            queue.append(conn)


def ans(graph, nodes):
    seen = {}
    for m, node in enumerate(nodes):
        flooder(node, m, graph, seen)
    if len(set(seen.values())) == 2:
        return prod(Counter(seen.values()).values())


nodes = list(nodes)
counter = Counter()
while True:
    a = choice(nodes)
    b = choice(nodes)
    path = shortest_path(a, b)
    counter.update(path)
    if len(counter) >= 3:
        ((a0, b0), _), ((a1, b1), _), ((a2, b2), _) = counter.most_common(3)
        g = deepcopy(graph)
        g[a0].remove(b0)
        g[b0].remove(a0)
        g[a1].remove(b1)
        g[b1].remove(a1)
        g[a2].remove(b2)
        g[b2].remove(a2)
        if a := ans(g, nodes):
            print(a)
            break
