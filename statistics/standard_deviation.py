import math

def calculate_mean(values):
    return sum(values) / len(values)

def standard_deviation(values):
    mean = calculate_mean(values)
    to_be_summed = [(x - mean)**2 for x in values]
    summed = sum(to_be_summed)
    return math.sqrt((1/len(values))*summed)
