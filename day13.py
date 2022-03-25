from itertools import product

with open("data/data13.txt", "r") as file:
    data = file.read().split("\n")


def initialize_data(input_data):
    in_points = [row.split(",") for row in input_data if row != "" and not row.startswith("fold")]
    in_folds = [row.replace("fold along ", "") for row in input_data if row.startswith("fold")]
    x_max, y_max = max(int(row[0]) + 1 for row in in_points), max(int(row[1]) + 1 for row in in_points)

    in_matrix = [[0 for col in range(x_max)] for row in range(y_max)]
    for right, down in in_points:
        in_matrix[int(down)][int(right)] = 1

    return in_folds, in_matrix


def fold_up(original_matrix, line):
    new_matrix = [
        [i + j for i, j in zip(original_matrix[height], original_matrix[2 * line - height])]
        for height in range(len(original_matrix) // 2)
    ]
    return new_matrix


def fold_left(original_matrix, line):
    new_matrix = [[row[idx] + row[2 * line - idx] for idx in range(len(row) // 2)] for row in original_matrix]
    return new_matrix


def get_sum(current_matrix):
    return sum(sum(row) for row in [list(map(lambda x: x >= 1, curr_row)) for curr_row in current_matrix])


folds, matrix = initialize_data(data)
counter = 0

for fold in folds:
    line_num = int(fold.replace("y=", "").replace("x=", ""))
    if fold.startswith("y"):
        matrix = fold_up(matrix, line_num)
        counter += 1
    else:
        matrix = fold_left(matrix, line_num)
        counter += 1

    # PROBLEM 1
    if counter == 1:
        print(get_sum(matrix))


# PROBLEM 2
for row, col in product(range(len(matrix)), range(len(matrix[0]))):
    # make it more readable
    if matrix[row][col] >= 1:
        matrix[row][col] = 1

for row in matrix:
    print(row)
