def get_matrix(y_true, y_pred):
    tp, fp, fn = 0, 0, 0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp += 1
        elif true == 0 and pred == 1:
            fp += 1
        elif true == 1 and pred == 0:
            fn += 1
    return tp, fn, fp

def count_precision(tp, fp):
    return tp / (tp+fp)

def count_recall(tp, fn):
    return tp / (tp+fn)

def f1_score(y_true, y_pred):
    tp, fn, fp = get_matrix(y_true, y_pred)
    precision = count_precision(tp, fp)
    recall = count_recall(tp, fn)
    return 2 * ((precision * recall) / (precision + recall))
