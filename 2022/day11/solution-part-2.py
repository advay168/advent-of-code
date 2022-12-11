import re

with open("./input.txt") as file:
    data = file.read().splitlines()


class Monkey:
    def __init__(self, starting, func, test, true_test, false_test, all_monkeys):
        self.starting = [int(n) for n in starting]
        self.func = func
        self.test = int(test)
        self.true_test = int(true_test)
        self.false_test = int(false_test)
        self.all_monkeys = all_monkeys
        self.inspections = 0

    def inspect(self, modulo):
        items = self.starting.copy()
        self.starting = []
        for item in items:
            self.inspections += 1
            worry = self.func(item)
            worry %= modulo
            if worry % self.test == 0:
                self.all_monkeys[self.true_test].starting.append(worry)
            else:
                self.all_monkeys[self.false_test].starting.append(worry)

    def __repr__(self):
        return str(self.starting)
        

monkeys = []
for i in range(0, len(data), 7):
    starting = []
    func = lambda x:x
    if m := re.match(r".*: (.*)", data[i + 1]):
        starting = m.groups()[0].split(", ")
    if m := re.match(r".*= (old .*)", data[i + 2]):
        op = m.groups()[0]
        func = lambda old, op=op:eval(op)
    test = data[i + 3].split()[-1]
    true_test = data[i + 4].split()[-1]
    false_test = data[i + 5].split()[-1]
    monkeys.append(Monkey(starting, func, test, true_test, false_test, monkeys))

modulo = 1
for monkey in monkeys:
    modulo *= monkey.test

for i in range(10000): 
    for monkey in monkeys:
        monkey.inspect(modulo)

inspections = [monkey.inspections for monkey in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])
