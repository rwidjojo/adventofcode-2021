with open("data/data7.txt", "r") as file:
    data = file.readline()

problem = data.split(",")
initial_state = list(map(lambda x: int(x), problem))

def get_minimum_fuel(f):
    return min(sum(f(item-point) for item in initial_state) for point in range(max(set(initial_state))+1))

fuels = get_minimum_fuel(lambda x: abs(x))
fuels_2 = get_minimum_fuel(lambda x: abs(x) * (abs(x) + 1) / 2)

print(fuels)
print(fuels_2)