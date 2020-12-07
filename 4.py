required_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
])

accepted_eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def is_valid_hgt(hgt):
    if len(hgt) < 2:
        return False
    hgt_metric = hgt[-2:]
    if hgt_metric not in ['cm', 'in']:
        return False
    hgt_val = int(hgt[:-2])
    if hgt_metric == 'cm' and not(150 <= hgt_val <= 193):
        return False
    if hgt_metric == 'in' and not(59 <= hgt_val <= 76):
        return False
    return True

def is_valid_hcl(hcl):
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    for char in hcl[1:]:
        if char not in '0123456789abcdef':
            return False
    return True

def is_valid_pid(pid):
    if len(pid) != 9:
        return False
    for char in pid:
        if char not in '0123456789':
            return False
    return True

def is_valid_passport(passport):
    entries = passport.split()
    fields = {}
    for entry in entries:
        k, v = entry.split(':')
        if k != 'cid':
            fields[k] = v
    part_1_result = set(fields.keys()) == required_fields
    if not part_1_result:
        return False, False

    part_2_result = True
    if not(1920 <= int(fields['byr']) <= 2002):
        part_2_result = False
    if not(2010 <= int(fields['iyr']) <= 2020):
        part_2_result = False
    if not(2020 <= int(fields['eyr']) <= 2030):
        part_2_result = False
    if not(fields['ecl'] in accepted_eye_colors):
        part_2_result = False
    if not(is_valid_hgt(fields['hgt'])):
        part_2_result = False
    if not(is_valid_hcl(fields['hcl'])):
        part_2_result = False
    if not(is_valid_pid(fields['pid'])):
        part_2_result = False

    return part_1_result, part_2_result

with open('4.txt') as f:
    data = f.read()

data = data.split('\n\n')
print(len(data))

results = map(is_valid_passport, data)
part_1_result, part_2_result = 0, 0
for result in results:
    part_1_result += result[0]
    part_2_result += result[1]

print('Part 1', part_1_result)
print('Part 2', part_2_result)