from collections import Counter

import sys

with open('1.txt') as f:
    data = Counter(int(x) for x in f.readlines())

for elem in data:
    if elem == 1010 and data[elem] == 2:
        print('Part 1', 1010*1010)
        break
    elif 2020 - elem in data:
        print('Part 1', elem * (2020 - elem))
        break

for elem in data:
    data[elem] -= 1
    for elem2 in data:
        if data[elem2] == 0:
            continue
        elif elem2 * 2 == 2020 - elem:
            print('Part 2', elem * elem2 * elem2)
            sys.exit(0)
        else:
            remainder = 2020 - elem - elem2
            if remainder in data and data[remainder] > 0:
                print('Part 2', elem * elem2 * remainder)
                sys.exit(0)
    data[elem] += 1