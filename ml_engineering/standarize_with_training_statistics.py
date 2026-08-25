import math

def calculate_mean(values):
    return sum(values)/len(values)

def calculate_sigma(train, mean):
    val_sum = 0
    for sample in train:
        val_sum += math.pow(sample - mean, 2)

    return math.sqrt(val_sum/len(train))

def standardize_test_data(train, test):
    columns = list(zip(*train))

    means = [
        calculate_mean(column)
        for column in columns
    ]

    sigmas = [
        calculate_sigma(column, mean)
        for column, mean in zip(columns, means)
    ]

    result = []

    for row in test:
        new_row = []

        for value, mean, sigma in zip(row, means, sigmas):
            if sigma == 0:
                new_row.append(0)
            else:
                new_row.append((value - mean) / sigma)

        result.append(new_row)

    return result
