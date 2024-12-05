import re

def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]


CROSS_DIRS = [
    [(-1, -1), (0, 0), (1, 1)],  # Top-left to bottom-right
    [(1, -1), (0, 0), (-1, 1)],  # Top-right to bottom-left
]



def apply_dir(x, y, dirs, width, height):
    coords = [(x + dx, y + dy) for dx, dy in dirs]
    return [(x, y) for x, y in coords if 0 <= x < width and 0 <= y < height]


def get_cross_coords(x, y, width, height):
    return [
        apply_dir(x, y, dirs, width, height)
        for dirs in CROSS_DIRS
        if len(apply_dir(x, y, dirs, width, height)) == 3
    ]


def get_cross_strings(grid, x, y, width, height):
    crosses = get_cross_coords(x, y, width, height)
    return ["".join(grid[cy][cx] for cx, cy in coords) for coords in crosses]

def is_cross_mas(grid, x, y, width, height):
    cross_strings = get_cross_strings(grid, x, y, width, height)
    return cross_strings.count("MAS") == 2


def count_x(grid):
    height = len(grid)
    width = len(grid[0])
    count = 0

    for y in range(height):
        for x in range(width):
            if is_cross_mas(grid, x, y, width, height):
                count += 1

    return count


input_file = "input"
grid = read_input(input_file)
total_count = count_x(grid)
print("Total X-MAS Matches:", total_count)

