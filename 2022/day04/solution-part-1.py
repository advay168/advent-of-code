import re

with open("./input.txt") as file:
    data = file.read().splitlines()


def enclosed(a, b, c, d):
    if a < c:
        return d <= b
    elif a == c:
        return True
    else:
        return enclosed(c, d, a, b)


count = 0
for line in data:
    start_1, end_1, start_2, end_2 = map(
        int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()
    )
    if enclosed(start_1, end_1, start_2, end_2):
        count += 1
print(count)
