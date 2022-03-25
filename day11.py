import itertools

with open("data/data11.txt", "r") as file:
    data = file.read().split("\n")

neighbour_diff = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]


class AllEnergizedException(Exception):
    pass


def initialize_matrix(dataset):
    matrix = [list(row) for row in dataset]
    width = len(matrix[0])
    height = len(matrix)
    new_matrix = [[[0, False] for _ in range(width + 2)] for __ in range(height + 2)]
    for row, col in itertools.product(range(height + 2), range(width + 2)):
        if row == 0 or row == height + 1 or col == 0 or col == width + 1:
            new_matrix[row][col] = [0, False]
        else:
            new_matrix[row][col] = [int(matrix[row - 1][col - 1]), False]
    return new_matrix


def get_center_matrix(outer_matrix):
    outer_matrix_w = len(outer_matrix[0])
    outer_matrix_h = len(outer_matrix)
    return [[outer_matrix[row][col] for col in range(1, outer_matrix_w - 1)] for row in range(1, outer_matrix_h - 1)]


def single_step(matrix):
    matrix_w = len(matrix[0])
    matrix_h = len(matrix)
    flash_count = 0

    def get_high_energy():
        center_matrix = get_center_matrix(matrix)
        return any(any(x[0] > 9 and not x[1] for x in cm_row) for cm_row in center_matrix)

    def is_all_energized():
        center_matrix = get_center_matrix(matrix)
        return all(all(x[1] for x in cm_row) for cm_row in center_matrix)

    # Add 1 to every cell in the matrix
    for row, col in itertools.product(range(1, matrix_h - 1), range(1, matrix_w - 1)):
        matrix[row][col][0] += 1

    # If the energy level is 9, then add 1 to adjacent cell, and set them to zero:
    while get_high_energy():
        for row, col in itertools.product(range(1, matrix_h - 1), range(1, matrix_w - 1)):
            # if the value larger than 9
            if matrix[row][col][0] > 9 and not matrix[row][col][1]:
                # set the cell value to zero, add flash count, and add adjacent cell
                matrix[row][col][1] = True
                flash_count += 1
                for dx, dy in neighbour_diff:
                    matrix[row + dx][col + dy][0] += 1

    if is_all_energized():
        raise AllEnergizedException("All octopuses are flashing now!")

    # After flashing, set the energy level to zero
    for row, col in itertools.product(range(matrix_h), range(matrix_w)):
        matrix[row][col][1] = False
        if row in [0, matrix_h] or col in [0, matrix_w]:
            matrix[row][col] = [0, False]
        elif matrix[row][col][0] > 9:
            matrix[row][col][0] = 0

    return flash_count


# PROBLEM 1
answer_1 = 0
matrix_1 = initialize_matrix(data)
for i in range(100):
    answer_1 += single_step(matrix_1)

print(answer_1)

# PROBLEM 2
answer_2 = 0
matrix_2 = initialize_matrix(data)
while True:
    try:
        single_step(matrix_2)
        answer_2 += 1
    except AllEnergizedException as aee:
        break

print(answer_2 + 1)
