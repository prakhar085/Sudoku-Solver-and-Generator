board = []
# taking input from the user
for i in range(9): board.append(list(map(int, input().split())))


def solve(bo):
    position = find_empty(bo)
    if not position: return True
    r, c = position
    for i in range(1, 10):
        if valid(bo, i, (r, c)):
            bo[r][c] = i
            if solve(bo):
                return True
            bo[r][c] = 0
    return False


def valid(bo, num, pos):
    for i in range(9):
        if bo[pos[0]][i] == num and i != pos[1]: return False
    for j in range(9):
        if bo[j][pos[1]] == num and j != pos[0]: return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos: return False
    return True


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j
    return None


solve(board)
for it in board: print(*it)
