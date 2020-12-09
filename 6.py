from functools import reduce

with open('6.txt') as f:
    data = f.read().split('\n\n')

part_1_result = 0
for group in data:
    replied_yes = reduce(lambda x, y: x.union(y), map(set, group.split()))
    part_1_result += len(replied_yes)

print('Part 1', part_1_result)

part_2_result = 0
for group in data:
    replied_yes = reduce(lambda x, y: x.intersection(y), map(set, group.split()))
    part_2_result += len(replied_yes)

print('Part 2', part_2_result)
