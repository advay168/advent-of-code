from math import prod

with open("./input.txt") as file:
    data = file.read()

raw_workflows, _ = data.split("\n\n")

workflows = {}
for line in raw_workflows.splitlines():
    # ASCII value of open brace so that vim indenting does not get confused
    name, conditions = line.split(chr(123))
    conditions = conditions[:-1]
    *conditions, last = conditions.split(",")
    cs = []
    for cond in conditions:
        cond, label = cond.split(":")
        if "<" in cond:
            op = "<"
            var, val = cond.split("<")
        else:
            op = ">"
            var, val = cond.split(">")
        cs.append((var, op, int(val), label))
    workflows[name] = [*cs, last]


def process(part, current_workflow):
    if current_workflow == "R":
        return 0
    elif current_workflow == "A":
        return prod(b - a + 1 for a, b in part.values())
    conds = workflows[current_workflow]
    s = 0
    for var, op, val, label in conds[:-1]:
        minn, maxx = part[var]
        if op == "<":
            part[var] = (minn, val - 1)
            s += process(part.copy(), label)
            part[var] = (val, maxx)
        else:
            part[var] = (val + 1, maxx)
            s += process(part.copy(), label)
            part[var] = (minn, val)
    s += process(part.copy(), conds[-1])
    return s


print(process({k:(1, 4000) for k in "xmas"}, "in"))
