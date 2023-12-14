with open("./input.txt") as file:
    data = file.read()

seeds, *data = data.split("\n\n")
seeds = list(map(int, seeds.split()[1:]))
categories = []
for c in data:
    categories.append([tuple(map(int, x.split())) for x in c.splitlines()[1:]])

locs = []
for seed in seeds:
    current = seed
    for cat in categories:
        for dest, source, n in cat:
            if source <= current < source + n:
                current = current - source + dest
                break
    locs.append(current)
print(min(locs))
