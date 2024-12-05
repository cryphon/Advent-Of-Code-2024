import numpy as np
import re

def read_input(file_path):
    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f]
    return grid


# use regex to fina all instances of "XMAS" or "SAMX"
def count_horizontal(grid):
    return sum(len(re.findall(r"(?=XMAS|SAMX)", row)) for row in grid)

# zip(*grid) transposes the grid
def rotate_grid(grid):
    return ["".join(row) for row in zip(*grid)]


def count_vertical(grid):
    rotated = rotate_grid(grid)
    return count_horizontal(rotated)


def get_diagonals(grid):
    rows, cols = len(grid), len(grid[0])
    diagonals = []

    # top left to bottom right
    for d in range(rows + cols -1):
        diagonal = []
        for i in range(max(0, d - cols + 1), min(d + 1, rows)):
            j = d - i
            diagonal.append(grid[i][j])
        diagonals.append("".join(diagonal))

    return diagonals


# extract top-right to bottom left diagonals
def get_reversed_diagonals(grid):
    reversed_grid = [row[::-1] for row in grid]
    return get_diagonals(reversed_grid)

def count_diagonal(grid):
    diagonals = get_diagonals(grid)
    reversed_diagonals = get_reversed_diagonals(grid)
    return count_horizontal(diagonals) + count_horizontal(reversed_diagonals)


def count(grid):
    h = count_horizontal(grid)
    v = count_vertical(grid)
    d = count_diagonal(grid)
    return h + v + d

input_grid = [
    "XMAS....",
    "....XMAS",
    "..XMAS..",
    "X...MASX",
    "....XMAS",
    "SAMX....",
    "....SAMX",
    "SAMX...."
]

# Split into lines if input is a string
# grid = input_grid
grid = read_input("input")

# Count occurrences of XMAS and SAMX
total_count = count(grid)
print("Total Matches:", total_count)

