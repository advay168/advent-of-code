from pathlib import Path

with open(Path(__file__).parent / "./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)


class Light:
    been = set()

    @staticmethod
    def reset():
        Light.been = set()

    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir

    def go(self):
        if (self.pos, self.dir) in self.been:
            return []
        px, py = self.pos
        if not (0 <= px < w):
            return []
        if not (0 <= py < h):
            return []
        Light.been.add((self.pos, self.dir))
        match grid[py][px]:
            case "/":
                match self.dir:
                    case (1, 0):
                        return [Light((px, py - 1), (0, -1))]
                    case (-1, 0):
                        return [Light((px, py + 1), (0, 1))]
                    case (0, 1):
                        return [Light((px - 1, py), (-1, 0))]
                    case (0, -1):
                        return [Light((px + 1, py), (1, 0))]
                    case _:
                        assert False
            case "\\":
                match self.dir:
                    case (1, 0):
                        return [Light((px, py + 1), (0, 1))]
                    case (-1, 0):
                        return [Light((px, py - 1), (0, -1))]
                    case (0, 1):
                        return [Light((px + 1, py), (1, 0))]
                    case (0, -1):
                        return [Light((px - 1, py), (-1, 0))]
                    case _:
                        assert False
            case "|":
                match self.dir:
                    case (0, 1):
                        return [Light((px, py + 1), self.dir)]
                    case (0, -1):
                        return [Light((px, py - 1), self.dir)]
                    case _:
                        return [
                            Light((px, py - 1), (0, -1)),
                            Light((px, py + 1), (0, 1)),
                        ]
            case "-":
                match self.dir:
                    case (1, 0):
                        return [Light((px + 1, py), (1, 0))]
                    case (-1, 0):
                        return [Light((px - 1, py), (-1, 0))]
                    case _:
                        return [
                            Light((px + 1, py), (1, 0)),
                            Light((px - 1, py), (-1, 0)),
                        ]
            case _:
                dx, dy = self.dir
                return [Light((px + dx, py + dy), self.dir)]


def energy(px, py, dx, dy):
    Light.reset()
    lights = [Light((px, py), (dx, dy))]
    while lights:
        n = []
        for light in lights:
            n += light.go()
        lights = n
    return len({pos for (pos, _) in Light.been})


m = 0
for x in range(0, w):
    m = max(m, energy(x, 0, 0, 1))
    m = max(m, energy(x, h - 1, 0, -1))
for y in range(0, h):
    m = max(m, energy(0, y, 1, 0))
    m = max(m, energy(w - 1, y, -1, 0))
print(m)
