from typing import *

Matrix = List[List[int]]

# assigning initial values to the grid
initial_grid: Matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# a grid with no solution
no_solution: Matrix = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True


def is_completed(grid: Matrix) -> bool:
    return all(all(cell != 0 for cell in row) for row in grid)


def find_empty_location(grid: Matrix) -> Optional[Tuple[int, int]]:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def sudoku(grid: Matrix) -> Optional[Matrix]:
    if is_completed(grid):
        return grid

    location = find_empty_location(grid)
    if location is not None:
        row, column = location
    else:
        return grid

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku(grid) is not None:
                return grid

            grid[row][column] = 0

    return None


def print_solution(grid: Matrix) -> None:
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    for example_grid in (initial_grid, no_solution):
        print("\nExample grid:\n" + "=" * 20)
        print_solution(example_grid)
        print("\nExample grid solution:")
        solution = sudoku(example_grid)
        if solution is not None:
            print_solution(solution)
        else:
            print("Cannot find a solution.")
