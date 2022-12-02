with open("./input.txt") as file:
    data = file.read().splitlines()

hallway = data[1][1:-1]
row_1 = data[2][1:-1]
row_4 = "#" + data[3][2:] + "#"


row_2 = "##D#C#B#A##"
row_3 = "##D#B#A#C##"
grid = [hallway, row_1, row_2, row_3, row_4]

ideal = "##A#B#C#D##"


def should_move(grid, i, j):
    if grid[i][j] in ".#":
        return False
    return any(grid[i_][j] != ideal[j] for i_ in range(i, len(grid)))


def move(grid, from_i, from_j, to_i, to_j):
    new_grid = [list(row) for row in grid]
    new_grid[to_i][to_j] = new_grid[from_i][from_j]
    new_grid[from_i][from_j] = "."
    return tuple("".join(row) for row in new_grid)


def calculate_cost(char, from_i, from_j, to_i, to_j):
    multiplier = 10 ** (ord(char) - ord("A"))
    return (abs(to_i - from_i) + abs(to_j - from_j)) * multiplier


def can_move(grid, from_i, from_j, to_i, to_j):
    step = 1 if from_j < to_j else -1
    if from_i == 0:
        for j in range(from_j + step, to_j, step):
            if grid[0][j] != ".":
                return False
        for i in range(1, to_i + 1):
            if grid[i][to_j] != ".":
                return False
        for i in range(to_i + 1, len(grid)):
            if grid[i][to_j] != ideal[to_j]:
                return False
        return True
    for i in range(from_i - 1, -1, -1):
        if grid[i][from_j] != ".":
            return False
    if to_j % 2 == 0 and to_j not in {0, len(grid[0]) - 1}:
        return False
    for j in range(from_j, to_j + step, step):
        if grid[0][j] != ".":
            return False
    return True


def possible_moves(grid, i, j):
    if not should_move(grid, i, j):
        return []
    char = grid[i][j]
    target_j = ideal.index(char)
    is_possible = lambda target: can_move(grid, i, j, *target)
    if i == 0:
        return filter(is_possible, ((i, target_j) for i in range(1, len(grid))))

    return filter(is_possible, zip(iter(int, None), range(11)))


from functools import cache


@cache
def best_cost(grid):
    if grid[1:] == (ideal,) * (len(grid) - 1):
        return 0
    minimum_cost = float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for target_i, target_j in possible_moves(grid, i, j):
                new_grid = move(grid, i, j, target_i, target_j)
                cost = calculate_cost(grid[i][j], i, j, target_i, target_j)
                cost += best_cost(new_grid)
                minimum_cost = min(minimum_cost, cost)
    return minimum_cost


print(best_cost(tuple(grid)))
