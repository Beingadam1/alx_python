def square_matrix_simple(matrix=[]):
    # new_list contained squared matrix
    new_list = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return new_list