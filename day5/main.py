import sys

# Read input file and split into rules and updates sections
with open("input", "r") as file:
    data = file.read()

rules_input, updates = data.split("\n\n")
rules_input = rules_input.splitlines()
updates = [u.split(',') for u in updates.splitlines()]

# Create dictionary to store rules
# Key: first page number in rule, Value: list of pages that must come after it
rules = {}

for rule in rules_input:
    rule = rule.split("|")
    if rules.get(rule[0]) == None:
        rules[rule[0]] = []
    rules[rule[0]].append(rule[1])

def check(update):
    """
    Check if update sequence violates any rules
    For each rule "A|B", checks if A appears before B in the sequence
    Returns (is_valid, [i,j]) where i,j are indices of conflicting pages if invalid
    """
    u_len = len(update)
    incorrect = []

    for i in range(u_len):
        for j in range(i+1, u_len):
            # Check if page[j] has rules and if page[i] must come after it
            if update[j] in list(rules.keys()) and update[i] in rules[update[j]]:
                incorrect = [i, j]
                return False, incorrect
    return True, incorrect

def switch(list, elems):
    """Swap elements at indices elems[0] and elems[1]"""
    list[elems[0]], list[elems[1]] = list[elems[1]], list[elems[0]]
    return list

res1 = 0  # Sum of middle pages in valid sequences
res2 = 0  # Sum of middle pages after fixing invalid sequences

for update in updates:
    u_len = len(update)
    rule_check, incorrect = check(update)

    if rule_check:
        # If sequence is valid, add middle page value to res1
        middle = update[u_len//2]
        res1 += int(middle)
    else:
        # Keep swapping conflicting pages until sequence becomes valid
        while not rule_check:
            update = switch(update, incorrect)
            rule_check, incorrect = check(update)
        middle = update[u_len//2]
        res2 += int(middle)

print(f"DAY 5[PART 1]: {res1}")  # Sum of middle pages in originally valid sequences
print(f"DAY 5[PART 2]: {res2}")  # Sum of middle pages after fixing invalid sequences
