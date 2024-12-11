import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs
from collections import deque, defaultdict
# get daily input
day = elfs.get_day(__file__)
data = elfs.read_data(day).strip()
# data = '12345'
# data = '2333133121414131402'

print(f'[DATA]: {data}')

arr = []
seen = []
mem_id = 0

for idx, char in enumerate(data):
    num = int(char)
    if idx % 2 == 0:
        # Add numeric IDs
        arr.extend([mem_id] * num)
        mem_id += 1
    else:
        # Add dots
        arr.extend(['.'] * num)

# print(f'[ARR]: {arr}')

# part 1, two pointer approach
def two_pointer_swap(arr):
    """
    Move files towards the rightmost free blocks, swapping with dots.
    """
    
    # Initialize variables
    p1, p2 = 0, len(arr) - 1
    
    # Queue to store positions of dots
    dot_positions = deque(i for i, val in enumerate(arr) if val == '.')

    # Pointer for numbers from the end
    p2 = len(arr) - 1

    # Process dots with numbers
    while dot_positions and p2 >= p1:
        # Get the next dot position
        p1 = dot_positions.popleft()
        # Skip non-numeric values at p2
        while p2 >= 0 and (arr[p2] == '.' or p2 in dot_positions):
            p2 -= 1
        # If a valid number is found, swap it with the dot
        if p2 > p1:  # Ensure valid swapping range
            arr[p1], arr[p2] = arr[p2], '.'
            p2 -= 1

    return arr



def memory_defragment(arr):
    """
    defragments memory by moving whole files to leftmost available free space
    processes files in decreasing order
    """
    file_positions = defaultdict(list)
    file_sizes = defaultdict(int)

    for i, val in enumerate(arr):
        if isinstance(val, int):
           file_positions[val].append(i)
           file_sizes[val] += 1

    # sort file IDs in decreasing order
    file_ids = sorted(file_sizes.keys(), reverse=True)

    # pre-calculate free space spans
    def get_free_spans():
        spans = []
        curr = 0
        pos = 0

        for i, val in enumerate(arr):
            if val == '.':
                if curr == 0:
                    start = i
                curr += 1
            else:
                if curr > 0:
                    spans.append((start, curr))
                curr = 0

        if curr > 0:
            spans.append((start, curr))
        return spans


    # process files

    for file in file_ids:
        size = file_sizes[file]
        curr_pos = file_positions[file]

        if not curr_pos:
            continue

    # get starting position of the file
    start_pos = min(curr_pos)

    # find suitable leftmost space to the left
    free_spans = get_free_spans()
    best_pos = None

    # look fot leftmost valid position
    for span_start, span_size in free_spans:
        if span_start < start_pos and span_size >= size:
            best_pos = span_start
            break

    if best_pos is not None:
        # clear old pos
        for pos in curr_pos:
            arr[pos] = '.'

        # place in new pos
        for i in range(size):
            arr[best_pos + i] = file

    return arr

from collections import defaultdict

def optimized_defragment(memory):
    """
    defragments memory by moving whole files to leftmost available free space
    processes files in decreasing order
    """
    # Track file positions and sizes in a single pass
    file_positions = defaultdict(list)
    file_sizes = defaultdict(int)
    
    # Pre-calculate file positions and sizes in O(n)
    for i, val in enumerate(memory):
        if isinstance(val, int):
            file_positions[val].append(i)
            file_sizes[val] += 1
    
    # Get sorted file IDs once
    file_ids = sorted(file_sizes.keys(), reverse=True)
    
    # Pre-calculate free space spans
    def get_free_spans():
        spans = []
        current_span = 0
        start_pos = 0
        
        for i, val in enumerate(memory):
            if val == '.':
                if current_span == 0:
                    start_pos = i
                current_span += 1
            else:
                if current_span > 0:
                    spans.append((start_pos, current_span))
                current_span = 0
                
        if current_span > 0:
            spans.append((start_pos, current_span))
            
        return spans
    
    # Process each file
    for file_id in file_ids:
        size = file_sizes[file_id]
        current_positions = file_positions[file_id]
        
        if not current_positions:
            continue
            
        # Get the starting position of the file
        start_pos = min(current_positions)
        
        # Find suitable free space to the left
        free_spans = get_free_spans()
        best_pos = None
        
        # Look for leftmost valid position
        for span_start, span_size in free_spans:
            if span_start < start_pos and span_size >= size:
                best_pos = span_start
                break
        
        # Move the file if a valid position was found
        if best_pos is not None:
            # Clear old positions
            for pos in current_positions:
                memory[pos] = '.'
            
            # Place in new position
            for i in range(size):
                memory[best_pos + i] = file_id
    
    return memory
    


print("start two pointer swap")
arr1 = two_pointer_swap(arr.copy())

# Initialize checksum
c1, c2 = 0, 0


# Iterate through the processed array
print("starting enumeration of results arr1")
for pos, val in enumerate(arr1):
    if isinstance(val, int):  # Check if the value is numeric
        c1 += pos * val


# Output the calculated checksum
print(f'[CHECKSUM 1]: {c1}')

print("start defragmentation")
arr2 = optimized_defragment(arr.copy())

print("starting enumeration of results arr2")
for pos, val in enumerate(arr2):
    if isinstance(val, int):
        c2 += pos * val

print(f'[CHECKSUM 2]: {c2}')










