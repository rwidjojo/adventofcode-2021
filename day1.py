with open("data/data1.txt", "r") as file:
    data = file.read().split("\n")

# PROBLEM 1
count = 0
for idx in range(len(data)):
    if int(data[idx]) > int(data[idx - 1]):
        count += 1

print(count)

# PROBLEM 2
new_data = [int(data[idx]) + int(data[idx + 1]) + int(data[idx + 2]) for idx in range(len(data) - 2)]

count_2 = 0
for idx in range(len(new_data)):
    if int(new_data[idx]) > int(new_data[idx - 1]):
        count_2 += 1

print(count_2)
