def mae(y_true, y_pred):
    mae = 0
    for true, pred in zip(y_true, y_pred):
        mae += abs(true - pred)
    return mae/len(y_true)
