with open("data/data6.txt", "r") as file:
    data = file.readline()

problem = data.split(",")
initial_state = list(map(lambda x: int(x), problem))

def convert_state(state):
    counter = {idx: 0 for idx in range(9)}
    for item in state:
        counter[item] += 1
    return counter

def move_one_day(prev_counter):
    new_counter = {idx: 0 for idx in range(9)}
    for idx, value in prev_counter.items():
        if idx == 0:
            new_counter[8] += value
            new_counter[6] += value
        else:
            new_counter[idx-1] += value
    return new_counter

# PROBLEM 1
last_counter = convert_state(initial_state)
for i in range(80):
    last_counter = move_one_day(last_counter)
print(sum(last_counter.values()))

# PROBLEM 2
last_counter = convert_state(initial_state)
for i in range(256):
    last_counter = move_one_day(last_counter)
print(sum(last_counter.values()))