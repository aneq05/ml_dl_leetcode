import math

def normalize_vector(x):
    norm = math.sqrt(sum(value**2 for value in x))

    if norm == 0:
        return [0 for _ in x]

    return [value / norm for value in x]