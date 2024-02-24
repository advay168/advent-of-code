with open("./input.txt") as file:
    data = file.read()

raw_workflows, parts = data.split("\n\n")

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
        cs.append((var, op, val, label))
    workflows[name] = [*cs, ("x", "<", "0", last)]


def process(part):
    current_workflow = "in"
    while True:
        conds = workflows[current_workflow]
        for var, op, val, current_workflow in conds:
            if eval(f"{part[var]} {op} {val}"):
                break
        if current_workflow == "R":
            return False
        elif current_workflow == "A":
            return True


import json
import re

parts = [
    json.loads(re.sub(r"(\w+):", r'"\1":', part.replace("=", ":")))
    for part in parts.splitlines()
]
accepted = []
for part in parts:
    if process(part):
        accepted.append(part)

s = 0
for part in accepted:
    s += sum(map(int, part.values()))
print(s)
