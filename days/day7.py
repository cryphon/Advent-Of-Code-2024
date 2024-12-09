import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs
from collections import defaultdict

# get daily input
day = elfs.get_day(__file__)
puzzle_input = elfs.read_data(day)

# Initialize counters
p1 = 0
p2 = 0

def valid(target, ns, p2):
    stack = [(ns, [])]
    seen = set()

    while stack:
        nums, res = stack.pop()

        # if only one number left and eq to target
        if len(nums) == 1 and nums[0] == target:
            return True

        # Try combining first two numbers
        if len(nums) >= 2:
            n1, n2 = nums[0], nums[1]
            rest = nums[2:]  # Get remaining numbers as a list

            # addition
            new_n = n1 + n2
            if tuple([new_n] + rest) not in seen:
                stack.append(([new_n] + rest, res + [(n1, '+', n2)]))
                seen.add(tuple([new_n] + rest))

            # multiplication
            new_n = n1 * n2
            if tuple([new_n] + rest) not in seen:
                stack.append(([new_n] + rest, res + [(n1, '*', n2)]))
                seen.add(tuple([new_n] + rest))

            # concatenation (if p2)
            if p2:
                new_n = int(str(n1) + str(n2))
                if tuple([new_n] + rest) not in seen:
                    stack.append(([new_n] + rest, res + [(n1, '&', n2)]))
                    seen.add(tuple([new_n] + rest))

    return False

for line in puzzle_input.strip().split('\n'):
    target, ns = line.strip().split(':')
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if valid(target, ns, p2=False):
        p1 += target
    if valid(target, ns, p2=True):
        p2 += target

print(f"day 7[PART 1]: {p1}")
print(f"day 7[PART 2]: {p2}")
