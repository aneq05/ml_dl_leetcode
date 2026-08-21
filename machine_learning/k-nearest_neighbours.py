import math

def knn_classify(train_points, labels, query, k):
    distanses = []
    occurences = {}

    for train_point, label in zip(train_points, labels):
        distanse = math.sqrt(sum((a - b)**2 for a, b in zip(train_point, query)))
        distanses.append((distanse, label))
    
    distanses.sort()
    nearest = distanses[:k]

    for distanse, label in nearest:
        occurences[label] = occurences.get(label, 0) + 1
    return max(occurences, key=occurences.get)