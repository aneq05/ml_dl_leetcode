def mse(y_true, y_pred):
    sum = 0
    for true, pred in zip(y_true, y_pred):
        sum += (true - pred) ** 2
    return sum/len(y_true)
