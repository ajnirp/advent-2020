def boarding_pass_to_seat_id(bp):
    row = 0
    for i in range(7):
        if bp[6-i] == 'B':
            row += (1 << i)
    col = 0
    for i in range(3):
        if bp[9-i] == 'R':
            col += (1 << i)
    return row*8 + col

with open('5.txt') as f:
    data = [line.strip() for line in f.readlines()]

seat_ids = [boarding_pass_to_seat_id(bp) for bp in data]
max_id, min_id = max(seat_ids), min(seat_ids)

print('Part 1', max_id)

seat_ids = set(seat_ids)
for i in range(min_id, max_id+1):
    if i not in seat_ids:
        print('Part 2', i)