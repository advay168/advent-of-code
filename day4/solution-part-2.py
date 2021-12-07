with open("./input.txt") as file:
    data = file.read().splitlines()

board_type = list[list[tuple[str, bool]]]

num = (len(data) - 1) // 6

boards: list[board_type] = []
for i in range(num):
    board = [
        [(num, False) for num in row.split()] for row in data[2 + i * 6 : 7 + i * 6]
    ]
    boards.append(board)


def strike(n, board: board_type):
    for i, row in enumerate(board):
        for j, (num, taken) in enumerate(row):
            board[i][j] = (num, taken or num == n)


def is_winning(board: board_type):
    for i in range(5):
        if all(taken for _, taken in board[i]):
            return True
        if all(taken for _, taken in [board[k][i] for k in range(5)]):
            return True
    return False


def score(board: board_type):
    s = 0
    for row in board:
        for n, taken in row:
            if not taken:
                s += int(n)
    return s


def print_board(board: board_type):
    for row in board:
        for n, taken in row:
            print(f"{n:>3} ({int(taken)})", end=" ")
        print()


for num in data[0].split(","):
    for board in boards[:]:
        strike(num, board)
        if is_winning(board):
            if len(boards) == 1:
                print(score(board) * int(num))
            boards.remove(board)
