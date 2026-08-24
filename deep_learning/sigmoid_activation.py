import math 

def sigmoid(xs):
    # 1 / (1 + e^-x) for each x
    return [1 / (1 + pow(math.e, -x)) for x in xs]
