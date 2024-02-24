with open("./input.txt") as file:
    data = file.read().splitlines()


def hash_(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


words = data[0].split(",")
s = 0
for word in words:
    s += hash_(word)
print(s)
