with open("./input.txt") as file:
    data = file.read().splitlines()

hallway = data[1][1:-1]
room_row_1 = data[2][1:-1]
room_row_2 = "#" + data[3][2:] + "#"
grid = [hallway, room_row_1, room_row_2]


ideal = "##A#B#C#D##"


def should_move(grid, i, j):
    if grid[i][j] in ".#":
        return False
    if i == 1:
        return grid[i][j] != ideal[j] or grid[i + 1][j] != ideal[j]
    if i == 2:
        return grid[i][j] != ideal[j]
    return True


def move(grid, from_i, from_j, to_i, to_j):
    assert can_move(grid, from_i, from_j, to_i, to_j), breakpoint()
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
        if to_i == 1:
            if grid[to_i + 1][to_j] != ideal[to_j]:
                return False
        return True
    if from_i == 2:
        if grid[1][from_j] != ".":
            return False
    if to_j % 2 == 0 and to_j not in [0, 10]:
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
        return filter(is_possible, [(1, target_j), (2, target_j)])

    return filter(is_possible, zip([0] * 11, range(11)))


from functools import cache


@cache
def best_cost(grid):
    if grid[1:] == (ideal,) * 2:
        return 0
    minimum_cost = float("inf")
    for i in range(3):
        for j in range(11):
            for target_i, target_j in possible_moves(grid, i, j):
                new_grid = move(grid, i, j, target_i, target_j)
                cost = calculate_cost(grid[i][j], i, j, target_i, target_j)
                cost += best_cost(new_grid)
                minimum_cost = min(minimum_cost, cost)
    return minimum_cost


print(best_cost(tuple(grid)))
