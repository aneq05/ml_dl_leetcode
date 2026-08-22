def center_row(row):
    observed = [x for x in row if x != 0]

    if not observed:
        return [0 for _ in row]

    mean = sum(observed) / len(observed)

    return [
        0 if x == 0 else x - mean
        for x in row
    ]


def mean_center_users(ratings):
    return [center_row(row) for row in ratings]