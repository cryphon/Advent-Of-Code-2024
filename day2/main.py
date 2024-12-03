import numpy as np
import pandas as pd



def could_safe(seq):
    if is_safe(seq):
        return True

    # Try removing one at a time and test again
    for i in range(len(seq)):
        test = seq[:i] + seq[i + 1:]

        if is_safe(test):
            return True
    return False


def is_safe(numbers):
    if len(numbers) < 2:
        return False
    
    # Check for repeating numbers
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return False
    
    is_increasing = numbers[1] > numbers[0]
    
    # Check all adjacent pairs
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        
        # Must maintain same direction throughout
        if (is_increasing and diff <= 0) or (not is_increasing and diff >= 0):
            return False
        
        # Changes must be between 1-3
        if abs(diff) > 3:
            return False
    
    return True

with open('input', 'r') as file:
    sequences = [list(map(int, line.split())) for line in file if line.strip()]
    safe_count = sum(1 for seq in sequences if is_safe(seq))
    could_count = sum(1 for seq in sequences if could_safe(seq))

print(f"day 2[PART 1]: {safe_count}")
print(f"day 2[PART 2]: {could_count}")
