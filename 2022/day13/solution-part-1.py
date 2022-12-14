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


data.append("")
it = iter(data)
count = 0
for idx,(a, b,_) in enumerate(zip(it, it, it)):
    a, b = eval(a), eval(b)
    if compare(a, b) == 1:
        count += idx + 1
print(count)
