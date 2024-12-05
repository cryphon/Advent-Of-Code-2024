import sys
sys.path.insert(1, sys.path[0].replace("days", "elfs"))
import elfs as elfs
import numpy as np
from collections import Counter

# get daily input
day = elfs.get_day(__file__)
input = elfs.read_data(day)

data = np.array([list(map(int, line.split())) for line in input.splitlines()])  # For multiple columns


arr1, arr2 = list(data[:, 0]), list(data[:, 1])

# part 2
freq = Counter(arr2)

ans = np.sum(np.abs(np.sort(arr1) - np.sort(arr2)))


# part 2
sim_score = [value * freq[value] for value in arr1]

print("day 1[PART 1]: " + str(ans))
print("day 1[PART 2]: " + str(sim_score))


