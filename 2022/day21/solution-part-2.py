with open("./input.txt") as file:
    data = file.read().splitlines()

variables = {}
for line in data:
    var = line[:4]
    if line[6:].isnumeric():
        val = int(line[6:])
        variables[var] = val
    else:
        a = line[6:10]
        b = line[11]
        c = line[13:]
        variables[var] = (a, b, c)

a, b, c = variables["root"]
variables["root"] = (a, "==", c)


def inverse(target, val, opr, isleft):
    if opr == "==":
        return val
    if opr == "/":
        if isleft:
            return val / target
        return val * target
    if opr == "-":
        if isleft:
            return val - target
        return val + target
    if opr == "+":
        return target - val
    if opr == "*":
        return target / val


def find_path(current):
    if current == "humn":
        return ["humn"], True
    x = variables[current]
    if isinstance(x, int):
        return [], False
    opr1, _, opr2 = x
    path, on_path = find_path(opr1)
    if on_path:
        path.append(current)
        return path, True
    path, on_path = find_path(opr2)
    if on_path:
        path.append(current)
        return path, True
    return [], False


def walk(current, target, path):
    if current == "humn":
        print(target)
        return target
    x = variables[current]
    if isinstance(x, int):
        return x
    opr1, opr, opr2 = x
    if opr1 in path:
        b = walk(opr2, target, path)
        t = inverse(target, b, opr, False)
        a = walk(opr1, t, path)
    elif opr2 in path:
        a = walk(opr1, target, path)
        t = inverse(target, a, opr, True)
        b = walk(opr2, t, path)
    else:
        a = walk(opr1, target, path)
        b = walk(opr2, target, path)
    return eval(f"{a} {opr} {b}")


path, _ = find_path("root")
path.pop()
walk("root", 150, path)
