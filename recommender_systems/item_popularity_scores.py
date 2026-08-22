def item_mean(item):
    item_sum, count = 0, 0
    for col in item:
        if col != 0:
            item_sum += col
            count += 1

    if count == 0:
        return 0

    return item_sum / count

def item_popularity_scores(ratings):
    return [item_mean(item) for item in zip(*ratings)]
