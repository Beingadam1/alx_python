def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        print()
    for row in matrix:
        for index, element in enumerate(row):
            if index == len(row) -1:
                print('{:d}'.format(element))
            else:
                print('{:d}'.format(element), end=' ')

