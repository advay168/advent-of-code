with open("./input.txt") as file:
    data = file.read().splitlines()


def priority(char):
    if char.isupper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


s = 0
it = iter(data)
for _1, _2, _3 in zip(it, it, it):
    (c,) = set(_1).intersection(_2, _3)
    s += priority(c)
print(s)
