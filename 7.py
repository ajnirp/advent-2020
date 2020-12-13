import collections

with open('7.txt') as f:
    data = f.readlines()

# adds a mapping {key: set(containee1, containee2, containee3)} to the graph
# each containee = (color, qty)
def update_graph(mapping, graph):
    key, vals = mapping
    if key in graph:
        graph[key] = graph[key].union(vals)
    else:
        graph[key] = vals

# given a line, output (key, set(containee1, containee2, containee3))
def parse_line(line):
    container, rest = line.split(' contain ')
    container = ' '.join(container.split()[:2])
    contents = set()
    if rest[:2] == 'no':
        return (container, contents)
    for containee in rest.split(', '):
        split = containee.split()
        qty = int(split[0])
        color = ' '.join(split[1:3])
        contents.add((color, qty))
    return (container, contents)

# reverse the above-defined graph, yielding
# (color: set(container1, container2, container3...))
def reverse_graph(graph):
    result = collections.defaultdict(set)
    for key in graph:
        for val in graph[key]:
            color, qty = val
            result[color].add(key)
    return result

# given a color, output its possible contents (and quantities of contents)
graph = {}
for line in data:
    update_graph(parse_line(line.strip()), graph)

# given a key, output who can contain it (no quantities)
reversed_graph = reverse_graph(graph)

# sanity check on prod data: uncomment to run
# assert(len(reversed_graph['dull aqua']) == 7)

# bfs exploration from a node: return the number of colors that can
# eventually contain that color
def count_eventual_containers(color, graph):
    if color not in graph:
        return 0
    result = 0
    seen = set() # stores seen colors
    to_search = collections.deque([color])
    while len(to_search) > 0:
        curr_color = to_search.popleft()
        for possible_container in reversed_graph[curr_color]:
            if possible_container not in seen:
                to_search.append(possible_container)
                seen.add(possible_container)
                result += 1
    return result

print('Part 1', count_eventual_containers('shiny gold', reversed_graph))

# bfs exploration from a node: return the number of bags it must contain,
# (including transitively contained bags)
def count_total_containees(color, graph):
    assert(color in graph)
    result = 0
    seen = set() # stores seen colors
    to_search = collections.deque([(color, 1)])
    while len(to_search) > 0:
        curr_color, qty = to_search.popleft()
        for possible_containee in graph[curr_color]:
            new_color, new_qty = possible_containee
            if new_color not in seen:
                total_qty = new_qty*qty
                to_search.append((new_color, total_qty))
                result += total_qty
    return result

print('Part 2', count_total_containees('shiny gold', graph))
