with open("./input.txt") as file:
    data = file.read()


class Range:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val

    def change(self, other):
        # I don't want to explain this mess
        if self.end <= other.start:
            return [Range(self.start, self.end, self.val)]
        if other.end <= self.start:
            return [Range(self.start, self.end, self.val)]
        if other.start <= self.start and self.end <= other.end:
            return [Range(self.start, self.end, other.val)]
        if other.start <= self.start:
            return [
                Range(self.start, other.end, other.val),
                Range(other.end, self.end, self.val),
            ]
        if self.end <= other.end:
            return [
                Range(self.start, other.start, self.val),
                Range(other.start, self.end, other.val),
            ]
        return [
            Range(self.start, other.start, self.val),
            Range(other.start, other.end, other.val),
            Range(other.end, self.end, self.val),
        ]

    def add(self):
        return Range(self.start + self.val, self.end + self.val, 0)


seeds, *data = data.split("\n\n")
seeds = [
    Range(int(source), int(source) + int(length), 0) for source, length in zip(*[iter(seeds.split()[1:])] * 2)
]

categories = []
for cat in data:
    for cat_range in cat.splitlines()[1:]:
        dest, source, length = map(int, cat_range.split())
        cat_range = Range(source, source + length, dest - source)
        tmp = []
        for seed in seeds:
            tmp += seed.change(cat_range)
        seeds = tmp
    seeds = [s.add() for s in seeds]

print(min([s.start for s in seeds]))
