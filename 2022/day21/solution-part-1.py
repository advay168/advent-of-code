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


def walk(current):
    x = variables[current]
    if isinstance(x, int):
        return x
    opr1, opr, opr2 = x
    return eval(f"{walk(opr1)} {opr} {walk(opr2)}")


print(walk("root"))
