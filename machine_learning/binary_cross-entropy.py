import math

def binary_cross_entropy(y_true, y_prob):
    return -1/len(y_true) * (sum([y * math.log(yp) + (1-y) * math.log(1-yp) for y, yp in zip(y_true, y_prob)]))
