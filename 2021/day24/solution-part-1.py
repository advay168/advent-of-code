with open("./input.txt") as file:
    data = file.read().splitlines()


import re


class ALU:
    def __init__(self):
        self.state = {"w": "0", "x": "0", "y": "0", "z": "0"}
        self.digits = iter("abcdefghijklmn")
        self.constraints = []

    @staticmethod
    def is_constant(expr):
        return all(char in "-1234567890" for char in expr)

    def dispatch(self, instruction):
        op, a, *b = instruction.split()
        getattr(self, op)(a, *b)

    def add(self, a, b):
        expr_a = self.state[a]
        expr_b = self.state[b] if b in "wxyz" else b
        if expr_b == "0":
            return
        self.state[a] = f"({expr_a} + {expr_b})"
        if expr_a == "0":
            self.state[a] = f"{expr_b}"
        elif self.is_constant(expr_a) and self.is_constant(expr_b):
            self.state[a] = str(eval(self.state[a]))
        elif self.is_constant(expr_b):
            if match := re.match(r"\(([a-v]) \+ ([0-9]+)\)", expr_a):
                variable = match.group(1)
                const = match.group(2)
                self.state[a] = f"({variable} + {int(const) + int(expr_b)})"

    def mul(self, a, b):
        expr_a = self.state[a]
        expr_b = self.state[b] if b in "wxyz" else b
        if expr_b == "0":
            self.state[a] = "0"
        elif expr_b == "1":
            self.state[a] = expr_a
        elif self.is_constant(expr_a) and self.is_constant(expr_b):
            self.state[a] = str(int(expr_a) * int(expr_b))
        else:
            self.state[a] = f"{expr_a} * {expr_b}"

    def div(self, a, b):
        expr_a = self.state[a]
        expr_b = self.state[b] if b in "wxyz" else b
        if expr_b != "1" and (
            m := re.match(r"^\((\(.*\)) \* 26 \+ \([a-v] \+ .*\)\)$", expr_a)
        ):
            self.state[a] = m.group(1)

    def mod(self, a, b):
        assert b == "26"
        expr_a = self.state[a]
        if (m := re.match(r"^\([a-v] \+ ([0-9]+)\)$", expr_a)) and int(m.group(1)) < 16:
            self.state[a] = expr_a
        elif m := re.match(r"^\(.* \* 26 \+ (\([a-v] \+ [0-9]+\))\)$", expr_a):
            self.state[a] = m.group(1)

    def eql(self, a, b):
        expr_a = self.state[a]
        expr_b = self.state[b] if b in "wxyz" else b
        self.state[a] = f"({expr_a} == {expr_b})"
        if expr_b in "qertuiopasdfghjklcvbnmm" and self.is_constant(expr_a):
            self.state[a] = "0"
        elif self.is_constant(expr_a) and self.is_constant(expr_b):
            self.state[a] = str(int(eval(self.state[a])))
        elif (m := re.match(r"^\(([a-v]) \+ ([0-9]+)\)$", expr_a)) and int(
            m.group(2)
        ) >= 10:
            self.state[a] = "0"
        elif expr_b == "0":
            if m := re.match(r"\(\((.*)\) == (.)\)", expr_a):
                x, y = m.groups()
                self.constraints.append(f"{y} = {x}")
                self.state[a] = "0"

    def inp(self, a):
        self.state[a] = next(self.digits)


alu = ALU()
for line in data:
    alu.dispatch(line)
constraints = alu.constraints
a = b = c = d = e = f = g = h = i = j = k = l = m = n = 9
for variable in "abcdefghijklmn":
    for i in range(9, 0, -1):
        locals()[variable] = i
        for expr in constraints:
            if variable in expr:
                exec(expr)
        invalid = False
        for v in "abcdefghijklmn":
            if not (0 < locals()[v] < 10):
                invalid = True
        if not invalid:
            break

for expr in constraints:
    exec(expr)
print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, sep="")
