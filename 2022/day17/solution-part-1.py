import itertools

with open("./input.txt") as file:
    data = file.read().splitlines()

jetstream = itertools.cycle(data[0])

blocks_str = [
    "####",
    ".#.\n###\n.#.",
    "..#\n..#\n###",
    "#\n#\n#\n#",
    "##\n##",
]

blocks = []
for block_str in blocks_str:
    rows = block_str.splitlines()
    w, h = len(rows[0]), len(rows)
    block_grid = []
    for row in reversed(rows):
        current = []
        for cell in row:
            current.append(1 if cell == "#" else 0)
        block_grid.append(current)
    blocks.append(block_grid)
blocks = itertools.cycle(blocks)


def expand(grid, height):
    for _ in range(height - len(grid)):
        grid.append([0] * 7)


def insert_block(grid, block, i, j):
    bw, bh = len(block[0]), len(block)
    expand(grid, i + bh)
    for y in range(bh):
        for x in range(bw):
            grid[i + y][j + x] |= block[y][x]


def move_horizontal(grid, block, i, j, jetstream):
    bw = len(block[0])
    n = next(jetstream)
    n_overlapping = len(grid) - i
    if n == ">" and j + bw < 7:
        for dy in range(min(len(block), n_overlapping)):
            for x in range(bw):
                if grid[i + dy][j + x + 1] == 1 and block[dy][x] == 1:
                    return j
        return j + 1
    elif n == "<" and j > 0:
        for dy in range(min(len(block), n_overlapping)):
            for x in range(bw):
                if grid[i + dy][j + x - 1] == 1 and block[dy][x] == 1:
                    return j
        return j - 1
    return j


def spawn(grid):
    return len(grid) + 3, 2


def move_up(grid, block, i, j):
    if i > len(grid):
        return i - 1
    bw = len(block[0])
    n_overlapping = len(grid) - i + 1
    for dy in range(min(len(block), n_overlapping)):
        for x in range(bw):
            if grid[i + dy - 1][j + x] == 1 and block[dy][x] == 1:
                return i
    return i - 1


grid = [[1] * 7]
for idx in range(2022):
    i, j = spawn(grid)
    block = next(blocks)
    prev_i = None
    while i != prev_i:
        j = move_horizontal(grid, block, i, j, jetstream)
        prev_i = i
        i = move_up(grid, block, i, j)
    insert_block(grid, block, i, j)
print(len(grid) - 1)
