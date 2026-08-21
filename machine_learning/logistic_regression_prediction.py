import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def logistic_predict(features, weights, bias):
    predictions = []

    for row in features:
        score = sum(feature*weight for feature, weight in zip(row, weights)) + bias
        predictions.append(sigmoid(score))

    return predictions