# Grid with all bombs
def full_grid(grid):
    return ['0' * len(grid[0]) for _ in range(len(grid))]


# Convert words to list in grid
def grid_to_list(grid):
    return [list(word) for word in grid]


# Convert list of words to words
def list_to_grid(grid):
    return ["".join(lst) for lst in grid]


# Find the position of bombs in the grid
def find_bombs(grid):
    bombs = []
    listed_grid = grid_to_list(grid)
    for row in range(0, len(grid)):
        for column in range(0, len(grid[0])):
            if listed_grid[row][column] == "0":
                bombs.append([row, column])
    return bombs


# Blast the bomb and nearby bombs
def blast(grid, bomb_row, bomb_column):
    grid[bomb_row][bomb_column] = "."
    if bomb_row + 1 < len(grid):
        grid[bomb_row + 1][bomb_column] = "."
    if bomb_row - 1 >= 0:
        grid[bomb_row - 1][bomb_column] = "."
    if bomb_column + 1 < len(grid[0]):
        grid[bomb_row][bomb_column + 1] = "."
    if bomb_column - 1 >= 0:
        grid[bomb_row][bomb_column - 1] = "."
    return grid


# Playing bomber man
def bomber_man(n, grid):
    if n % 2 == 0:
        return full_grid(grid)
    elif n % 4 == 3:
        full_listed_grid = grid_to_list(full_grid(grid))
        bombs = find_bombs(grid)
        for bomb in bombs:
            blasted = blast(full_listed_grid, bomb[0], bomb[1])
        return list_to_grid(blasted)
    else:
        return grid


n = int(input("Enter the number of seconds to simulate: "))
row, column = [int(x) for x in input("Input the number of rows and columns in the grid (e.g. 3 3): ").split()]
grid = []

for i in range(row):
    r = input(f"Input row {i+1} in the grid: ")
    if len(r) is not column:
        print(f"Error: the number of columns should be {column}")
        break
    grid.append(r)
else:
    new_grid = bomber_man(n, grid)
    for row in new_grid:
        print(row)
