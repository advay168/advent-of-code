with open("./input.txt") as file:
    data = file.read().splitlines()

from functools import lru_cache


def all_rotations_single(beacon):
    x, y, z = beacon
    # facing +z
    yield (+x, +y, +z)
    yield (+y, -x, +z)
    yield (-x, -y, +z)
    yield (-y, +x, +z)
    # facing -z
    yield (-x, +y, -z)
    yield (-y, -x, -z)
    yield (+x, -y, -z)
    yield (+y, +x, -z)

    # facing +y
    yield (+y, +z, +x)
    yield (-x, +z, +y)
    yield (-y, +z, -x)
    yield (+x, +z, -y)
    # facing -y
    yield (+y, -z, -x)
    yield (-x, -z, -y)
    yield (-y, -z, +x)
    yield (+x, -z, +y)

    # facing +x
    yield (+z, +x, +y)
    yield (+z, +y, -x)
    yield (+z, -x, -y)
    yield (+z, -y, +x)
    # facing -x
    yield (-z, +x, -y)
    yield (-z, +y, +x)
    yield (-z, -x, +y)
    yield (-z, -y, -x)


@lru_cache(None)
def find_all_rotations(beacons):
    return list(zip(*map(all_rotations_single, beacons)))


@lru_cache(None)
def relative_to_beacons(beacons):
    lst = []
    for (orig_x, orig_y, orig_z) in beacons:
        lst.append({(x - orig_x, y - orig_y, z - orig_z) for (x, y, z) in beacons})
    return lst


def are_overlapping(beacons1, beacons2):
    relative_b1 = relative_to_beacons(tuple(beacons1))
    relative_b2 = relative_to_beacons(tuple(beacons2))
    for i, r1 in enumerate(relative_b1):
        for j, r2 in enumerate(relative_b2):
            if len(r1.intersection(r2)) >= 12:
                return (i, j)


scanners = []
current = []
for line in data:
    if line == "":
        scanners.append(current)
        current = []
        continue
    if line.startswith("---"):
        continue
    current.append(tuple(map(int, line.split(","))))
scanners.append(current)
correct_beacons = scanners[0]
scanners = [tuple(b) for b in scanners]
seen = {0}
while len(seen) != len(scanners):
    for idx in range(len(scanners)):
        if idx in seen:
            continue
        for beacons in find_all_rotations(scanners[idx]):
            if indices := are_overlapping(correct_beacons, beacons):
                i, j = indices
                dx, dy, dz = map(
                    lambda x: x[0] - x[1], zip(correct_beacons[i], beacons[j])
                )
                for (x, y, z) in beacons:
                    pos = (x + dx, y + dy, z + dz)
                    if pos not in correct_beacons:
                        correct_beacons.append(pos)
                seen.add(idx)
                break
print(len(correct_beacons))
