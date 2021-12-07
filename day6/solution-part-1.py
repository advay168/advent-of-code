with open("./input.txt") as file:
    data = file.read().splitlines()


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def update(self):
        if self.timer > 0:
            self.timer -= 1
            return
        self.timer = 6
        return Fish(8)

    def __repr__(self) -> str:
        return str(self.timer)


allFishes = []
for timer in data[0].split(","):
    allFishes.append(Fish(int(timer)))

for day in range(80):
    temp = []
    for fish in allFishes:
        t = fish.update()
        if t:
            temp.append(t)
    allFishes += temp
print(len(allFishes))
