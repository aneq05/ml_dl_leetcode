import math 

def compute_sigmoid(xs):
    return [1 / (1 + math.exp(-x)) for x in xs]

def sigmoid_derivative(xs):
    sigmoids = compute_sigmoid(xs)
    return [
        sigmoid * (1-sigmoid)
        for sigmoid in sigmoids
    ]
