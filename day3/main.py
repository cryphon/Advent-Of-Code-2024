import string
import re
import math

test_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
test_data_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('input', 'r') as file:
    data = file.read()


def find_nums(txt):
    pattern = r'mul\((\d+),\s*(\d+)\)'
    matches = re.finditer(pattern, txt)


    ans = 0
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        ans += (num1 * num2)

    return ans



def sum_enabled_multiplications(text):
    pattern = r'(?:mul\((\d+),(\d+)\)|(?:don\'t|do)\(\))'
    matches = re.finditer(pattern, text)
    
    enabled = True  # Start with enabled state
    total = 0
    
    for match in matches:
        instruction = match.group(0)
        
        if instruction == "don't()":
            enabled = False
        elif instruction == "do()":
            enabled = True
        else:
            # It's a mul instruction
            if enabled:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                total += num1 * num2
    
    return total
# part 1
res = find_nums(data)
print(f'day 3[PART 1]: {res}')

# part 2


res2 = sum_enabled_multiplications(data)
print(f'day 3[PART 2]: {res2}')
        



