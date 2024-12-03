import numpy as np

ans = 0

# Load data
data = np.loadtxt('input', dtype=int)

# Split into two arrays
arr1, arr2 = list(data[:, 0]), list(data[:, 1])  # Convert to lists for mutability


def get_smallest(arr):
    if len(arr) == 0:  # Check if the array is empty
        return None, None
    smallest = min(arr)
    index = arr.index(smallest)
    return smallest, index


def diff(a, b):
    return abs(a - b)


# Calculate differences
for _ in range(len(arr1)):
    a1, a1idx = get_smallest(arr1)
    a2, a2idx = get_smallest(arr2)

    ans += diff(a1, a2)
    # Remove elements by value
    arr1.pop(a1idx)
    arr2.pop(a2idx)

print("day 1[PART 1]: " + str(ans))

