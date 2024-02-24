from pathlib import Path
# Run with pypy
with open(Path(__file__).parent / "./input.txt") as file:
    data = file.read().splitlines()

bricks = []
for i, line in enumerate(data):
    a, b = line.split("~")
    x0, y0, z0 = eval(a)
    x1, y1, z1 = eval(b)
    bricks.append(((x0, y0, z0), (x1 - x0, y1 - y0, z1 - z0), i))


def intersects(x, y, dx, dy, bx, by, bdx, bdy):
    for (a, da), (b, db) in zip([(x, dx), (y, dy)], [(bx, bdx), (by, bdy)]):
        if not ((b <= a + da <= b + db) or (a <= b + db <= a + da)):
            return False
    return True

def fall(bricks):
    final = []
    for (x, y, _), (dx, dy, dz), i in bricks:
        z = 1
        for (bx, by, bz), (bdx, bdy, bdz), _ in final:
            if intersects(x, y, dx, dy, bx, by, bdx, bdy):
                z = max(z, bz + bdz + 1)
        final.append(((x, y, z), (dx, dy, dz), i))
    return final

bricks.sort(key=lambda brick:brick[0][2])
final = fall(bricks)
final.sort(key=lambda brick:brick[0][2])
count = 0
for i in range(len(final)):
    xs = final[:i] + final[i + 1:]
    new = fall(xs)
    count += len(set(xs) - set(new))
    print(i, count)
print(count)
