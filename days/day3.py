import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs
import re
import math

# get daily input
day = elfs.get_day(__file__)
input = elfs.read_data(day)


def find_nums(txt):
    pattern = r'mul\((\d+),\s*(\d+)\)'
    matches = re.finditer(pattern, txt)

    ans = 0
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        ans += (num1 * num2)
    return ans



def sum_enabled_mul(txt):
    pattern = r'(?:mul\((\d+),(\d+)\)|(?:don\'t|do)\(\))'
    matches = re.finditer(pattern, txt)

    enabled = True
    total = 0

    for match in matches:
        inst = match.group(0)

        if inst == "don't()":
            enabled = False
        elif inst == "do()":
            enabled = True
        else:
            # its a mul inst
            if enabled:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                total += num1 * num2
    return total



res = find_nums(input)
print(f'day 3[PART 1]: {res}')

res2 = sum_enabled_mul(input)
print(f'day 3[PART 2]: {res2}')




