from collections import Counter

def parse_rules(rules):
    nums, letter = rules.split()
    num1, num2 = nums.split('-')
    return (int(num1), int(num2), letter)

data = []
with open('2.txt') as f:
    for line in f.readlines():
        rules, password = line.split(':')
        data.append((parse_rules(rules), password.strip()))

num_valid = 0
for line in data:
    rules, password = line
    counter = Counter(password)
    min_occur, max_occur, letter = rules
    if letter not in counter:
        continue
    if min_occur <= counter[letter] <= max_occur:
        num_valid += 1

print('Part 1', num_valid)

num_valid = 0
for line in data:
    rules, password = line
    idx1, idx2, letter = rules
    idx1, idx2 = idx1-1, idx2-1
    if idx1 >= len(password) or idx2 >= len(password):
        continue
    if password[idx1] == letter and password[idx2] != letter:
        num_valid += 1
    elif password[idx2] == letter and password[idx1] != letter:
        num_valid += 1

print('Part 2', num_valid)