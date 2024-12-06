import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs

# get daily input
day = elfs.get_day(__file__)
input = elfs.read_data(day)

# code for both parts
xmas = "XMAS"
mas = "MAS"

def string_check(to_check, check):
  return to_check == check or to_check == check[::-1]

def xmas_count(data, row, col):
  height = len(data)
  width = len(data[0])
  xmas_count = 0
  mas_count = 0
  checks = []
  
  # part 1
  # only check part 1 if the current cell is X or S
  if data[row][col] in ['X', 'S']:
    # horizontal check
    if col + 3 < width:
      checks.append(data[row][col:col+4])
    
    # vertical check
    if row + 3 < height:
      checks.append(str.join('',[data[row+i][col] for i in range(0,4)]))
    
    # diagonal check
    # top left to bottom right
    if row + 3 < height and col + 3 < width:
      checks.append(str.join('', [data[row+i][col+i] for i in range(0,4)]))

    # top right to bottom left
    if row + 3 < height and col - 3 >= 0:
      checks.append(str.join('', [data[row+i][col-i] for i in range(0,4)]))
    
    for check in checks:
      xmas_count += int(string_check(check, xmas))
  
  # part 2
  # only check part 2 if the current cell is M or S
  if data[row][col] in ['M', 'S']:
    # mas in form of X count
    if row + 2 < height and col + 2 < width:
      # top left to bottom right
      right = str.join('', [data[row+i][col+i] for i in range(0,3)])
      right_check = string_check(right, mas)
      
      # top right to bottom left
      left = str.join('', [data[row+i][col+2-i] for i in range(0,3)])
      left_check = string_check(left, mas)
      
      if right_check and left_check:
        mas_count += 1
  
  return [xmas_count, mas_count]



input = input.splitlines()
grid = [line.strip() for line in input]

result_part_1 = 0
result_part_2 =  0
for row in range(len(grid)):
  for col in range(len(grid[row])):
    count = xmas_count(grid, row, col)
    result_part_1 += count[0]
    result_part_2 += count[1]


# print the results
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")





