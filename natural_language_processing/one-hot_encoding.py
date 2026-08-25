def one_hot(indices, num_classes):
    result = []
    
    for indice in indices:
        row = [0] * num_classes
        row[indice] = 1
        result.append(row)
    
    return result
