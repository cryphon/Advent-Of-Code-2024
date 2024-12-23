import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs

# get daily input
day = elfs.get_day(__file__)
data = elfs.read_data(day)
data.strip()
data = [int(x) for x in data.split()]




cache = {}
def calculate_length(number, steps_remaining):
    if (number, steps_remaining) in cache:
        return cache[(number, steps_remaining)]
    
    if steps_remaining == 0:
        result = 1  # Base case: single number has length 1
    elif number == 0:
        result = calculate_length(1, steps_remaining - 1)
    elif len(str(number)) % 2 == 0:  # Even number of digits
        num_string = str(number)
        mid = len(num_string) // 2
        first_half = int(num_string[:mid])
        second_half = int(num_string[mid:])
        # Split number and process each half
        result = calculate_length(first_half, steps_remaining - 1) + \
                calculate_length(second_half, steps_remaining - 1)
    else:  # Odd number of digits
        result = calculate_length(number * 2024, steps_remaining - 1)
    
    cache[(number, steps_remaining)] = result
    return result


def solve(t):
    return sum(calculate_length(x, t) for x in data)


print(solve(25))
print(solve(75))
