import numpy as np

# Load data
data = np.loadtxt('input', dtype=int)

# Split into two arrays
arr1, arr2 = list(data[:, 0]), list(data[:, 1])  # Convert to lists for mutability


# Calculate all differences at once using numpy operations
# Sort both arrays and sum absolute differences
ans = np.sum(np.abs(np.sort(arr1) - np.sort(arr2)))

print("day 1[PART 1]: " + str(ans))
