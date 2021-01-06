# Functions galore!

import functools
import sys

# Begin parse utilities
def parse_class(line):
    def parse_bounds(line):
        def parse_pair(pair):
            split = pair.split('-')
            return (int(split[0]), int(split[1]))
        bounds = line.strip().split(' or ')
        return (parse_pair(bounds[0]), parse_pair(bounds[1]))
    name, bounds = line.split(':')
    bounds = parse_bounds(bounds)
    return (name, bounds)

def parse_ticket(ticket):
    return list(map(int, ticket.split(',')))
# End parse utilties

# True iff a value is valid for a class
def is_valid(val, class_):
    def in_bounds(val, bound):
        lo, hi = bound
        return lo <= val <= hi
    _, (bound1, bound2) = class_
    return in_bounds(val, bound1) or in_bounds(val, bound2)

# True iff a value isn't valid for any class
def never_valid(val, classes):
    return not any(is_valid(val, class_) for class_ in classes)

def part_1_result(nearby_tickets, classes, invalid_tickets):
    result = 0
    for idx, ticket in enumerate(nearby_tickets):
        for val in ticket:
            if never_valid(val, classes):
                result += val
                invalid_tickets.add(idx)
                break
    return result

# Return valid tickets given indices of invalid ones
def valid_tickets(tickets, invalid_tickets):
    return [ticket for idx, ticket in enumerate(tickets) if idx not in invalid_tickets]

# Find the potential indices of a class in a ticket's ordering. Why plural?
# Because multiple indices might work. We return them all and filter later.
def find_candidate_indices(class_, tickets):
    num_classes = len(tickets[0])
    candidates = set()
    for idx in range(num_classes):
        if all(is_valid(ticket[idx], class_) for ticket in tickets):
            candidates.add(idx)
    return candidates

# Find potential indices for a class for all classes. Discard the class bounds.
# They're not relevant going forward.
def find_candidate_indices_all(classes, tickets):
    return {class_[0] : find_candidate_indices(class_, tickets) for class_ in classes}

def resolve_indices(mapping):
    def find_class_with_only_one_candidate(mapping):
        final_mapping = {}
        for key in mapping:
            if len(mapping[key]) == 1:
                result = (key, list(mapping[key])[0])
                del mapping[key]
                return result
        sys.exit(1)

    def remove_from_candidate_map(idx, mapping):
        for key in mapping:
            mapping[key].remove(idx)

    final_mapping = {}
    target_len = len(mapping) # this decreases, so we save the initial value
    while len(final_mapping) < target_len:
        key, idx = find_class_with_only_one_candidate(mapping)
        final_mapping[key] = idx
        remove_from_candidate_map(idx, mapping)
    return final_mapping

# Extract the indices corresponding to classes beginning with 'departure'
def relevant_indices(mapping):
    return [mapping[key] for key in mapping if key.startswith('departure')]

def part_2_result(my_ticket, relevant_indices):
    return functools.reduce(lambda x, y: x*y, (my_ticket[idx] for idx in relevant_indices))

# Figure out which indices goes to which class. We start from the class with
# exactly one candidate index. Then we remove that index from every other class'
# candidate list. Iterate until every class has a final index.

if __name__ == '__main__':
    with open('16.txt') as f:
        data = [line.strip() for line in f.readlines()]

    classes = [parse_class(line) for line in data[:20]]
    my_ticket = parse_ticket(data[22])
    nearby_tickets = [parse_ticket(line) for line in data[25:]]
    invalid_tickets = set()
    print('Part 1', part_1_result(nearby_tickets, classes, invalid_tickets))
    nearby_tickets = valid_tickets(nearby_tickets, invalid_tickets)

    candidates = find_candidate_indices_all(classes, nearby_tickets)
    print('Part 2', part_2_result(my_ticket, relevant_indices(resolve_indices(candidates))))