def matrix_add(a, b):
    matrix_sum = []
    for row_a, row_b in zip(a,b):

        row_c = []
    
        for xa, xb in zip(row_a, row_b):
            row_c.append(xa + xb)
    
        matrix_sum.append(row_c)
    
    return matrix_sum
