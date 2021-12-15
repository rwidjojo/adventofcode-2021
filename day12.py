from collections import defaultdict


with open("data/data12.txt", "r") as file:
    data = file.read().split("\n")


routes = defaultdict(list)
for row in data:
    start, end = row.split("-")
    routes[start] += [end]
    routes[end] += [start]


def traverse_one(curr, seen):

    # from a starting point A, we count how many possible paths
    # if the next cave we choose is node "curr"

    # if current node is end, this is a valid route
    # add this to counter, and stop recursion
    if curr == 'end':
        return 1

    # if current node is start but we have gone somewhere
    # (therefore seen is not an empty set), this is invalid
    # stop recursion
    if curr == 'start' and seen:
        return 0

    # if current node is lowercase but already exists before
    # invalid route, skipping, stop recursion here
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

    # from a starting point A, we count how many possible paths
    # if the next cave we choose is node "curr"

    # if current node is end, this is a valid route
    # add this to counter, and stop recursion
    if curr == 'end':
        return 1

    # if current node is start but we have gone somewhere
    # (therefore seen is not an empty set), this is invalid
    # stop recursion
    if curr == 'start' and seen:
        return 0

    # if current node is lowercase but already exists before
    if curr.islower() and curr in seen:

        # check if there is a duplicate entry, if not then
        # register current node as the duplicate, but continue
        # the recursion
        if duplicate is None:
            duplicate = curr

        # if another small cave have been visited twice, not counted
        # stop recursion here, and this doesn't count towards total
        else:
            return 0

    # add the current node to the set
    seen = seen.union({curr})

    # start counting for recursion case
    output = 0

    # add total output from every possible next route
    # the current node can have
    for node in routes[curr]:
        output += traverse_two(node, seen, duplicate)

    return output


# PROBLEM 1 and 2
print(traverse_one('start', set()))
print(traverse_two('start', set(), None))
