def min_max_normalize(xs):
    x_min = min(xs)
    x_max = max(xs)
    normalized_list = []

    for element in xs:
        if x_max == x_min: 
            return [0.0 for _ in xs]
        else:
            new_elem = (element - x_min) / (x_max - x_min)
            normalized_list.append(new_elem)
    
    return normalized_list
