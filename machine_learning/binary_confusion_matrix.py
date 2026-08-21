def count_matrix(y_true, y_pred):
    tp, fp, fn, tn = 0, 0, 0, 0
    for true, pred in zip(y_true, y_pred):
        if true == 0 and pred == 0:
            tn +=1
        elif true == 1 and pred == 1:
            tp +=1
        elif true == 0 and pred == 1:
            fp +=1 
        else:
            fn +=1
    return tp, fp, fn, tn

def confusion_matrix(y_true, y_pred):
    tp, fp, fn, tn = count_matrix(y_true, y_pred)
    return [[tn, fp], [fn, tp]]