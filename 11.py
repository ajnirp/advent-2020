# true iff two layouts are identical cell-for-cell
def are_same(layout1, layout2):
    return len(layout2) == len(layout1) and all(row1 == row2 for row1, row2 in zip(layout1, layout2))

# deep copy of a layout
def copy(layout):
    return [[val for val in row] for row in layout]

def count_occupied_nbrs(layout, rule, r, c):
    assert(r < len(layout) and c < len(layout[r]))
    if rule == 'one':
        result = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < len(layout) and 0 <= new_c < len(layout[new_r]):
                    result += layout[new_r][new_c] == '#'
        return result
    elif rule == 'two':
        drs = dcs = [-1, 0, 1]
        # direction vectors
        dvs = [(dr, dc) for dr in drs for dc in dcs if not (dr == 0 and dc == 0)]
        result = 0
        for dr, dc in dvs:
            curr_r, curr_c = r, c
            while True:
                new_r, new_c = curr_r + dr, curr_c + dc
                if not (0 <= new_r < len(layout) and 0 <= new_c < len(layout[0])):
                    break
                if layout[new_r][new_c] == '#':
                    result += 1
                    break
                elif layout[new_r][new_c] == 'L':
                    break
                elif layout[new_r][new_c] == '.':
                    curr_r, curr_c = new_r, new_c
                    continue
        return result
    else:
        return 0

# step the layout once
def step(layout, rule, empty_threshold):
    assert(len(layout) > 0)
    new_layout = copy(layout)
    for r in range(len(layout)):
        for c in range(len(layout[r])):
            if layout[r][c] == '.':
                continue
            else:
                occupied_nbrs = count_occupied_nbrs(layout, rule, r, c)
                if layout[r][c] == 'L' and occupied_nbrs == 0:
                    new_layout[r][c] = '#'
                elif layout[r][c] == '#' and occupied_nbrs >= empty_threshold:
                    new_layout[r][c] = 'L'
    return new_layout

# step until the layout is stable, then return # of occupied seats
def step_until_stable(layout, rule, empty_threshold):
    while True:
        new_layout = step(layout, rule, empty_threshold)
        if are_same(layout, new_layout):
            return sum(sum(val == '#' for val in row) for row in layout)
        else:
            layout = new_layout

with open('11.txt') as f:
    original = [line.strip() for line in f.readlines()]
    print('Part 1', step_until_stable(copy(original), 'one', 4))
    print('Part 2', step_until_stable(copy(original), 'two', 5))