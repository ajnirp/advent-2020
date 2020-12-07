from functools import reduce

def new_pos(pos, dr, dc, num_rows, num_cols):
    row, col = pos
    row += dr
    if row >= num_rows:
        return -1 # out of bounds
    col += dc
    col %= num_cols
    return (row, col)

def num_trees(data, dr, dc):
    rows, cols = len(data), len(data[0])
    pos = (0, 0)
    num_trees = 0
    for _ in range(rows-1): # dr is at least 1, so we do at most #rows - 1 iterations
        pos = new_pos(pos, dr, dc, rows, cols)
        if pos == -1:
            break
        row, col = pos
        if data[row][col] == '#':
            num_trees += 1
    return num_trees

with open('3.txt') as f:
    data = [line.strip() for line in f.readlines()]

print('Part 1', num_trees(data, 1, 3))

deltas = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
print('Part 2', reduce(lambda x, y: x*y, [num_trees(data, dr, dc) for (dr, dc) in deltas]))