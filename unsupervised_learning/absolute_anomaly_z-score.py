import math

def calculate_mean(values):
    return sum(values) / len(values)

def calculate_variance(values, mean):
    return sum((value - mean) ** 2 for value in values) / len(values)

def anomaly_z_scores(values):
    mean = calculate_mean(values)
    std = math.sqrt(calculate_variance(values, mean))

    if std == 0:
        return [0 for _ in values]

    return [abs(value - mean) / std for value in values]