import math

def euclidean_distance(a, b):
    return math.sqrt(sum(pow(ai - bi, 2) for ai, bi in zip(a,b)))
