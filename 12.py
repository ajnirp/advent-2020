with open('12.txt') as f:
    instructions = f.readlines()

# assert that all left and right turns are either 90, 180 or 270 degrees
assert(all(int(instr[1:]) / 90 in [1,2,3] for instr in instructions if instr[0] in 'LR'))

def run_instructions(instructions):
    x, y, heading = 0, 0, 'E'
    # counter-clockwise order starting from east
    headings = ['E', 'N', 'W', 'S']
    for instr in instructions:
        directive, value = instr[0], int(instr[1:])
        if directive == 'N':
            y += value
        elif directive == 'S':
            y -= value
        elif directive == 'E':
            x += value
        elif directive == 'W':
            x -= value
        elif directive in 'LR':
            value /= 90
            if directive == 'R':
                value = -value
            heading = headings[int((headings.index(heading) + value) % 4)]
        elif directive == 'F':
            if heading == 'N':
                y += value
            elif heading == 'S':
                y -= value
            elif heading == 'E':
                x += value
            elif heading == 'W':
                x -= value
    return abs(x) + abs(y)

def run_instructions_2(instructions):
    # wrt (x, y), (wx, wy) becomes (-wy, wx)
    def rotate_waypoint_left(x, y, wx, wy):
        # this is equivalent to wx -= x; wy -= y; return x - wy, y + wx
        return x - wy + y, y + wx - x

    # wrt (x, y), (wx, wy) becomes (wy, -wx)
    def rotate_waypoint_right(x, y, wx, wy):
        # this is equivalent to wx -= x; wy -= y; return x + wy, y - wx
        return x + wy - y, y - wx + x

    x, y, wx, wy = 0, 0, 10, 1
    for instr in instructions:
        directive, value = instr[0], int(instr[1:])
        if directive == 'N':
            wy += value
        elif directive == 'S':
            wy -= value
        elif directive == 'E':
            wx += value
        elif directive == 'W':
            wx -= value
        elif directive == 'L':
            for turn in range(value // 90):
                wx, wy = rotate_waypoint_left(x, y, wx, wy)
        elif directive == 'R':
            for turn in range(value // 90):
                wx, wy = rotate_waypoint_right(x, y, wx, wy)
        elif directive == 'F':
            dx, dy = value*(wx - x), value*(wy - y)
            x, y = x + dx, y + dy
            wx, wy = wx + dx, wy + dy
    return abs(x) + abs(y)

print('Part 1', run_instructions(instructions))
print('Part 2', run_instructions_2(instructions))