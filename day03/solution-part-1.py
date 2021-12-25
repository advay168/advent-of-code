with open("./input.txt") as file:
    data = file.read().splitlines()

counts = [0] * len(data[0])
for line in data:
    for i, char in enumerate(line):
        counts[i] += (char == "1") * 2 - 1
g = 0
for count in counts:
    g <<= 1
    g += count > 0
length = len(counts)
e = 2 ** length - g - 1
print(g * e)
