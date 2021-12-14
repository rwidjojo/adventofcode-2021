from collections import defaultdict


with open("data/data12.txt", "r") as file:
    data = file.read().split("\n")


routes = defaultdict(list)
for row in data:
    start, end = row.split("-")
    routes[start] += [end]
    routes[end] += [start]

 
def traverse_one(curr, seen):
    
    # if current node is end, this is a valid route
    # add this to counter
    if curr == 'end':
        return 1
    
    # if current node is start but we have gone somewhere
    # (therefore seen is not an empty set), this is invalid
    if curr == 'start' and seen:
        return 0
    
    # if current node is lowercase but already exists before
    # invalid route, skipping
    if curr.islower() and curr in seen:
        return 0
    
    # add the current node to the set
    seen = seen.union({curr})
    
    output = 0
    
    # add total output from every next route
    # the current node can have
    for node in routes[curr]:
        output += traverse_one(node, seen)
        
    return output


def traverse_two(curr, seen, duplicate):

    if curr == 'end':
        return 1
    
    if curr == 'start' and seen:
        return 0
    
    if curr.islower() and curr in seen:
        if duplicate is None:
            duplicate = curr
        else:  # another small cave have been visited twice, not counted
            return 0
    
    seen = seen.union({curr})
    
    output = 0
    
    for node in routes[curr]:
        output += traverse_two(node, seen, duplicate)
        
    return output

# PROBLEM 1 and 2
print(traverse_one('start', set()))
print(traverse_two('start', set(), None))