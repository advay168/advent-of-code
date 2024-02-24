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
boxes = [{} for _ in range(256)]
for word in words:
    if word[-1] == "-":
        label = word[:-1]
        h = hash_(label)
        box = boxes[h]
        if label in box:
            del box[label]
    else:
        label = word[:-2]
        d = word[-1]
        h = hash_(label)
        box = boxes[h]
        box[label] = d


s = 0
for i, box in enumerate(boxes, 1):
    # python dicts remember insertion order
    for j, power in enumerate(box.values(), 1):
        s += i * j * int(power)
print(s)
