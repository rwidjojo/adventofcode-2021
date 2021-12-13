import itertools

with open("data/data9.txt", "r") as file:
    data = file.read().split("\n")

matrix = [list(row) for row in data]
width = len(matrix[0])
height = len(matrix)
neighbour_diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]
wall = '9'

new_matrix = [[None for i in range(width+2)] for j in range(height+2)]
for row, col in itertools.product(range(height+2), range(width+2)):
    if row == 0 or row == height + 1 or col == 0 or col == width + 1:
        new_matrix[row][col] = '9'
    else:
        new_matrix[row][col] = matrix[row - 1][col - 1]


# PROBLEM 1
low_points = []

for row, col in itertools.product(range(1, height+1), range(1, width+1)):
    neighbours = [new_matrix[row + dx][col + dy] for dx, dy in neighbour_diff]
    if all(neighbour > new_matrix[row][col] for neighbour in neighbours):
        low_points.append([(row,col), int(new_matrix[row][col])])

print(sum(low_point[1] + 1 for low_point in low_points))

# PROBLEM 2
def flood_fill(pos_x, pos_y, target_value):
    if new_matrix[pos_x][pos_y] == wall:
        return
    
    if new_matrix[pos_x][pos_y] == target_value:
        return
    
    new_matrix[pos_x][pos_y] = target_value

    flood_fill(pos_x + 1, pos_y, target_value)
    flood_fill(pos_x - 1, pos_y, target_value)
    flood_fill(pos_x, pos_y + 1, target_value)
    flood_fill(pos_x, pos_y - 1, target_value)

def count_occurrence(matrix, value):
    filtered = [
        list(filter(lambda x: x == value, row))
        for row in matrix
    ]
    return  sum(len(item) for item in filtered)

names = {low_point[0]: f"X{low_point[0]}" for low_point in low_points}
for low_point in low_points:
    flood_fill(low_point[0][0], low_point[0][1], names[low_point[0]])

basin_sizes = [
    (low_point[0], count_occurrence(new_matrix, names[low_point[0]]))
    for low_point in low_points
]
basin_sizes_sorted = sorted(basin_sizes, key=lambda x: -x[1])

print(basin_sizes_sorted[0][1] * basin_sizes_sorted[1][1] * basin_sizes_sorted[2][1])