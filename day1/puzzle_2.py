import numpy as np
from collections import Counter

# Load data
data = np.loadtxt('input', dtype=int)
arr1 = list(data[:, 0])  # First column: values
arr2 = list(data[:, 1])  # Second column: frequencies


# count freq in right list
freq = Counter(arr2)

# calc freq similarity score (value * freq in arr2)
sim_score = [value * freq[value] for value in arr1]
print("day 1[PART 2]: " + str(sum(sim_score)))
