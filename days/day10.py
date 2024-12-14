import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs
from typing import List, Set
from collections import deque

# get daily input
day = elfs.get_day(__file__)
data = elfs.read_data(day).strip().split('\n')


def bfs(grid: List[List[int]], pos: tuple) -> int:
    """
    BFS on the grid starting from pos.
    Counts reachable zeros when moving to cells with values exactly one less than current.
    """
    if not grid or not grid[0]:
        return 0
        
    queue = deque([pos])
    seen = set()
    rows, cols = len(grid), len(grid[0])
    ans = 0

    row, col = pos

    # four possible directions: right, down, left, up
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, col = queue.popleft()
        if (row, col) in seen:
            continue
        
        seen.add((row, col))
        curr_val = grid[row][col]

        if curr_val == 0:
            ans += 1

        # check directions
        for dr, dc in dirs:
            new_r, new_c = row + dr, col + dc

            # check bounds and ensure position hasn't been seen
            if (0 <= new_r < rows and 
                0 <= new_c < cols and 
                (new_r, new_c) not in seen):
                new_val = grid[new_r][new_c]
                if new_val == curr_val - 1:
                    queue.append((new_r, new_c))
    
    return ans


cache = {}
def part2(row ,col):
    if grid[row][col]==0:
        return 1
    if (row,col) in cache:
        return cache[(row,col)]
    ans = 0
    for dir_row ,dir_col in [(-1,0),(0,1),(1,0),(0,-1)]:
        next_row = row + dir_row
        next_col = col + dir_col
        if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == grid[row][col] - 1:
            ans += part2(next_row, next_col)
    cache[(row, col)] = ans
    return ans


grid = []
for line in data:
    if line.strip():
        grid.append([int(c) for c in line.strip()])


rows, cols = len(grid), len(grid[0])


res1, res2 = 0, 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 9:
            res1 += bfs(grid, (row, col))
            res2 += part2(row, col)


print(res1)
print(res2)
