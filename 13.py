import math

with open('13.txt') as f:
    earliest_depart = int(f.readline())
    buses = [int(val) for val in f.readline().split(',') if val != 'x']

def part_1_result(earliest_depart, buses):
    def helper(earliest_depart, bus):
        rem = earliest_depart % bus
        if rem == 0:
            return 0
        return bus, bus - rem
    result = min((helper(earliest_depart, bus) for bus in buses), key=lambda x: x[1])
    return result[0] * result[1]

print('Part 1', part_1_result(earliest_depart, buses))

with open('13.txt') as f:
    f.readline() # ignore
    # idx + t modulo bus = 0 => t modulo bus = bus - idx
    data = [(int(val), int(val) - idx) for idx, val in enumerate(f.readline().split(',')) if val != 'x']

buses = [x[0] for x in data]
moduli = [x[1] % x[0] for x in data]

# find the bezout coefficients for a, b
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Description
def extended_euclidean(a, b):
    a_orig, b_orig = a, b
    s_0, s_1 = 1, 0
    t_0, t_1 = 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        s_0, s_1 = s_1, s_0 - (q * s_1)
        t_0, t_1 = t_1, t_0 - (q * t_1)
    return s_0, t_0

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(direct_construction)
def solve_congruences(buses, moduli):
    product_all = math.prod(buses)
    product_all_but = [product_all // x for x in buses]
    result = 0
    for i, (N, n) in enumerate(zip(product_all_but, buses)):
        M, m = extended_euclidean(N, n)
        print(M*N+m*n, N, n, M, m, moduli[i])
        result += moduli[i] * M * product_all_but[i]
    return result

part_2_result = solve_congruences(buses, moduli)

# ensure the answer is +ve
if part_2_result < 0:
    product_all = math.prod(buses)
    q = -part_2_result // product_all
    part_2_result += (q + 1) * product_all

print('Part 2', part_2_result)