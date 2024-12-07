import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs

# get daily input
day = elfs.get_day(__file__)
input = elfs.read_data(day)

grid = input.strip().split('\n')
rows = len(grid)
cols = len(grid[0])

res1 = 0
res2 = 0

# Direction vectors for [Up, Right, Down, Left]
DIRECTIONS = [
    (-1, 0),  # Up:    move up 1 row (-1 row, 0 columns)
    (0, 1),   # Right: move right 1 column (0 rows, +1 column)
    (1, 0),   # Down:  move down 1 row (+1 row, 0 columns)
    (0, -1)   # Left:  move left 1 column (0 rows, -1 column)
]

# find cursor
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^':
            start_row, start_col = r, c



for o_row in range(rows):
    for o_col in range(cols):
        row, col = start_row, start_col
        direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left

        # unique combinations of pos and direction
        seen = set()
        # unique positions without direction
        seen_x = set()

        while True:
            if (row, col, direction) in seen:
                res2 += 1
                break

            seen.add((row, col, direction))
            seen_x.add((row, col))

            dr, dc = DIRECTIONS[direction]
            rr = row + dr  # new row pos
            cc = col + dc  # new col pos

            # check bounds
            if not(0 <= rr < rows and 0 <= cc < cols):
                if grid[o_row][o_col] == '#':
                    res1 = len(seen_x)
                break
            
            if grid[rr][cc] == '#' or rr == o_row and cc == o_col:
                direction = (direction + 1) % 4
            else:
                row = rr    # Use proper assignment
                col = cc    # Use proper assignment


print(f"day 6[PART 1]: {res1}")
print(f"day 6[PART 2]: {res2}")


