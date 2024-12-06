import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs

# get daily input
day = elfs.get_day(__file__)
input = elfs.read_data(day)
print(type(input))

input = input.splitlines()

def could_safe(seq):
    if is_safe(seq):
        return True

    # true removing one at a time and test again
    for i in range(len(seq)):
        test = seq[:i] + seq[i+1:]

        if is_safe(test):
            return True

    return False


def is_safe(numbers):
    if(len(numbers)) < 2:
       return False

    # check for repeating numbers
    for i in  range(len(numbers) - 1):
       if numbers[i] == numbers[i+1]:
           return False

    is_increasing = numbers[1] > numbers[0]
    
    # check all madjacent pairs
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]

        # must maintain same direction throughout
        if(is_increasing and diff <= 0) or (not is_increasing and diff >= 0):
            return False

        if abs(diff) > 3:
            return False
    
    return True


sequences = [list(map(int, line.split())) for line in input if line.strip()]
safe_count = sum(1 for seq in sequences if is_safe(seq))
could_count = sum(1 for seq in sequences if could_safe(seq))

print(f"day 2[PART 1]: {safe_count}")
print(f"day 2[PART 2]: {could_count}")
    

