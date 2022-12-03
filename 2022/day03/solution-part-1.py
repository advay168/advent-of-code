with open("./input.txt") as file:
    data = file.read().splitlines()


def priority(char):
    if char.isupper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


s = 0
for line in data:
    l = len(line)
    a = set(line[: l // 2])
    b = set(line[l // 2 :])
    (c,) = a.intersection(b)
    s += priority(c)
print(s)
