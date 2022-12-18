with open("./input.txt") as file:
    data = file.read().splitlines()

cubes = set()
for line in data:
    x, y, z = map(int, line.split(","))
    cubes.add((x, y, z))


def neighbours(vertex):
    x, y, z = vertex
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def count_faces(cube):
    count = 0
    for v in neighbours(cube):
        if v not in cubes:
            count += 1
    return count


c = 0
for cube in cubes:
    c += count_faces(cube)
print(c)
