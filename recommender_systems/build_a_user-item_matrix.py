def build_user_item_matrix(num_users, num_items, interactions):
    matrix = [
        [0 for _ in range(num_items)]
        for _ in range(num_users)
    ]

    for user, item, rating in interactions:
        matrix[user][item] = rating

    return matrix
