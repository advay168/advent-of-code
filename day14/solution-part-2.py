from collections import Counter

with open("./input.txt") as file:
    data = file.read().splitlines()

template = data[0]

rules: dict[str, tuple[str, str]] = {}
for line in data[2:]:
    (x, y), b = line.split(" -> ")
    rules[x + y] = (x + b, b + y)

counted_pairs = Counter(map("".join, zip(template[:], template[1:])))


def transform(counted_pairs: Counter):
    new_counted_pairs = Counter()
    for pair, counts in counted_pairs.items():
        p1, p2 = rules[pair]
        new_counted_pairs[p1] += counts
        new_counted_pairs[p2] += counts
    return new_counted_pairs


for _ in range(40):
    counted_pairs = transform(counted_pairs)

counts = Counter(template[0] + template[-1])
for (char1, char2), count in counted_pairs.items():
    counts[char1] += count
    counts[char2] += count
c = counts.values()
max_count, min_count = max(c), min(c)
print((max_count - min_count) // 2)
