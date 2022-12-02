with open("./input.txt") as file:
    data = file.read().splitlines()


def add_left(lst, val):
    l, _ = lst
    if isinstance(l, int):
        lst[0] = l + val
    else:
        add_left(l, val)


def add_right(lst, val):
    _, r = lst
    if isinstance(r, int):
        lst[1] = r + val
    else:
        add_right(r, val)


def reduce_nests(lst, level=0):
    global num_changes
    l, r = lst
    if level == 4:
        return l, r, True
    if isinstance(l, list):
        a, b, immediate = reduce_nests(l, level + 1)
        if num_changes == 2:
            return a, b, immediate
        if b != -1:
            num_changes += 1
            if isinstance(r, list):
                add_left(r, b)
            else:
                lst[1] = r + b
            if immediate:
                lst[0] = 0
        if a != -1 or b != -1:
            return a, -1, False
    if isinstance(r, list):
        a, b, immediate = reduce_nests(r, level + 1)
        if num_changes == 2:
            return a, b, immediate
        if a != -1:
            num_changes += 1
            if isinstance(l, list):
                add_right(l, a)
            else:
                lst[0] = l + a
            if immediate:
                lst[1] = 0
        if a != -1 or b != -1:
            return -1, b, False
    return -1, -1, False


def reduce_numbers(lst):
    global changed
    l, r = lst
    if isinstance(l, int) and not changed:
        if l >= 10:
            replacement = [l // 2, l // 2 + l % 2]
            lst[0] = replacement
            changed = True
    elif isinstance(l, list) and not changed:
        reduce_numbers(l)
    if isinstance(r, int) and not changed:
        if r >= 10:
            replacement = [r // 2, r // 2 + r % 2]
            lst[1] = replacement
            changed = True
    elif isinstance(r, list) and not changed:
        reduce_numbers(r)


def reduce_completely(num):
    global changed, num_changes
    changed = True
    while changed:
        num_changes = 2
        while num_changes:
            num_changes = 0
            reduce_nests(num)
        changed = False
        reduce_numbers(num)
    return num


def add_num(lst1, lst2):
    return reduce_completely([lst1, lst2])


def magnitude_num(lst) -> int:
    l, r = lst
    if isinstance(l, list):
        l = magnitude_num(l)
    if isinstance(r, list):
        r = magnitude_num(r)
    return 3 * l + 2 * r


from json import loads

acc_num = loads(data[0])
for line in data[1:]:
    num = loads(line)
    acc_num = add_num(acc_num, num)
print(magnitude_num(acc_num))
