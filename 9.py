WINDOW_SIZE = 25

with open('9.txt') as f:
    data = list(map(int, f.readlines()))

part_1_result = -1
part_1_result_idx = -1
for i in range(WINDOW_SIZE, len(data)):
    found = False
    for j in range(i-WINDOW_SIZE, i):
        if found:
            break
        for k in range(j+1, i):
            if data[j] + data[k] == data[i]:
                found = True
                break
    if not found:
        part_1_result = data[i]
        part_1_result_idx = i
        break

print('Part 1', part_1_result)

# Compute prefix sums for `data` up to `part_1_result_idx` (no need for entire
# array) and find the pair whose difference is `part_1_result`
# prefix_sums[0] = 0
# prefix_sums[i] = sum in `data` from index 0 up to index i-1, both inclusive
prefix_sums = [0]
for elem in data[:part_1_result_idx]:
    prefix_sums.append(elem + prefix_sums[-1])

for j in range(len(prefix_sums)-1, -1, -1):
    for k in range(j-1, -1, -1):
        if prefix_sums[j] - prefix_sums[k] == part_1_result:
            data_slice = data[k:j]
            print('Part 2', min(data_slice) + max(data_slice))