def threshold_predictions(probabilities, threshold):
    labels = []
    for probability in probabilities:
        label = 1 if probability >= threshold else 0
        labels.append(label)
    return labels
