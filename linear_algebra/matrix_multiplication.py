def matrix_multiply(a, b):
    matrix_mul = []

    for row_a in a:
        row_c = []

        for col_b in zip(*b):
            value = sum(x * y for x, y in zip(row_a, col_b))
            row_c.append(value)

        matrix_mul.append(row_c)

    return matrix_mul