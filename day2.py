import itertools

with open("data/data2.txt", "r") as file:
    data = file.read().split("\n")

# PROBLEM 1
prob1 = [(datum.split(" ")[0], int(datum.split(" ")[1])) for datum in data]
prob1_sorted = sorted(prob1)
res = itertools.groupby(prob1_sorted, lambda x: x[0])

for key, group in res:
    print(key, sum([data[1] for data in list(group)]))

# PROBLEM 2
aim = 0
depth = 0
horizontal = 0
for row in prob1:
    if row[0] == 'forward':
        horizontal += row[1]
        depth += aim * row[1]
    elif row[0] == 'up':
        aim -= row[1]
    elif row[0] == 'down':
        aim += row[1]

print(depth * horizontal)