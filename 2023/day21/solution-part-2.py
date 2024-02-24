with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)
sx, sy = 0, 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            sx, sy = x, y
            grid[y][x] = "."

def reachable_from(x, y, steps, seen, ans):
    if (x, y, steps) in seen:
        return
    seen.add((x, y, steps))
    if steps == 0:
        ans.add((x, y))
        return
    for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if grid[y % h][x % w] != "#":
            reachable_from(x, y, steps - 1, seen, ans)


n = 26501365
ans = set()
reachable_from(sx, sy, n % w, set(), ans)
y0 = len(ans)
ans = set()
reachable_from(sx, sy, w + n % w, set(), ans)
y1 = len(ans)
ans = set()
reachable_from(sx, sy, w + w + n % w, set(), ans)
y2 = len(ans)

c = y0
a = (y2 - c) // 2 - (y1 - c)
b = y1 - (a + c)
x = n // w
print(a * x * x + b * x + c)
