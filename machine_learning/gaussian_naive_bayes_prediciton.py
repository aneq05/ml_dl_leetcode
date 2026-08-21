import math

def calculate_prior(prior):
    return math.log(prior)

def calculate_posteriori(query, means, variances):
    score = 0
    for x, mean, variance in zip(query, means, variances):
        log_gaussian = (-0.5* math.log(2*math.pi*variance) - ((x-mean) ** 2) / (2 * variance))
        score += log_gaussian
    return score

def gaussian_naive_bayes(query, means, variances, priors):
    final_scores = []

    for class_index in range(len(priors)):
        apriori = calculate_prior(priors[class_index])

        aposteriori = calculate_posteriori(
            query,
            means[class_index],
            variances[class_index]
        )

        final_scores.append(apriori + aposteriori)

    return max(range(len(final_scores)), key=lambda i: final_scores[i])
