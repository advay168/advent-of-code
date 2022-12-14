from functools import cmp_to_key

with open("./input.txt") as file:
    data = file.read().splitlines()


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return +1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            if x := compare(a, b):
                return x
        return compare(len(left), len(right))
    elif isinstance(left, int):
        return compare([left], right)
    else:
        return compare(left, [right])


data.append("[[2]]")
data.append("[[6]]")

d = sorted(map(eval, filter(bool, data)), key=cmp_to_key(compare), reverse=True)
print((d.index([[2]]) + 1) * (d.index([[6]]) + 1))
