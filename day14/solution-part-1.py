from collections import Counter

with open("./input.txt") as file:
    data = file.read().splitlines()

template = data[0]

rules = {}
for line in data[2:]:
    a, b = line.split(" -> ")
    rules[a] = b


def transform(template):
    return_template = template[0]
    for a, b in zip(template[:], template[1:]):
        return_template += rules[a + b] + b
    return return_template


for _ in range(10):
    template = transform(template)


counts = Counter(template)
max_count = counts[max(counts, key=lambda x: counts[x])]
min_count = counts[min(counts, key=lambda x: counts[x])]
print(max_count - min_count)
