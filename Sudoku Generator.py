import random


def generate_sudoku():
    grid = []
    for i in range(9):grid.append([0 for j in range(9)])
    ghh=random.randrange(6,22)
    for i in range(ghh):
        r = random.randrange(9);c = random.randrange(9);num = random.randrange(1, 10)
        while not check_valid(grid, r, c, num) or grid[r][c] != 0:
            r = random.randrange(9);c = random.randrange(9)
            num = random.randrange(1, 10)
        grid[r][c] = num
    print_grid(grid)


def print_grid(grid):
    for it in grid:print(*it)


def check_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i]==num and i!=col:return False
    for j in range(9):
        if grid[j][col]==num and j!=row:return False
    box_x=col//3
    box_y=row//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if grid[i][j]==num and (i,j)!=(row,col):return False
    return True


generate_sudoku()