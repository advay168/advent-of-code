with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)


class Light:
    been = set()

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
                    case (1, 0):
                        return [
                            Light((px, py - 1), (0, -1)),
                            Light((px, py + 1), (0, 1)),
                        ]
                    case (-1, 0):
                        return [
                            Light((px, py - 1), (0, -1)),
                            Light((px, py + 1), (0, 1)),
                        ]
                    case (0, 1):
                        return [Light((px, py + 1), (0, 1))]
                    case (0, -1):
                        return [Light((px, py - 1), (0, -1))]
                    case _:
                        assert False
            case "-":
                match self.dir:
                    case (1, 0):
                        return [Light((px + 1, py), (1, 0))]
                    case (-1, 0):
                        return [Light((px - 1, py), (-1, 0))]
                    case (0, 1):
                        return [
                            Light((px + 1, py), (1, 0)),
                            Light((px - 1, py), (-1, 0)),
                        ]
                    case (0, -1):
                        return [
                            Light((px + 1, py), (1, 0)),
                            Light((px - 1, py), (-1, 0)),
                        ]
                    case _:
                        assert False
            case _:
                dx, dy = self.dir
                return [Light((px + dx, py + dy), self.dir)]


lights = [Light((0, 0), (1, 0))]
while lights:
    n = []
    for light in lights:
        n += light.go()
    lights = n
print(len({pos for (pos, _) in Light.been}))
