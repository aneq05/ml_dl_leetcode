def linear_gradient(xs, ys, weight, bias):
    dw, db = 0, 0
    n = len(xs)

    for x, y in zip(xs, ys):
        y_pred = weight * x + bias  # y = a*x + b
        error = y_pred - y

        dw += error * x
        db += error 

    dw = (2/n) * dw
    db = (2/n) * db

    return dw, db
