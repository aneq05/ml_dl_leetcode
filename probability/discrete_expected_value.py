def expected_value(outcomes, probabilities):
    return sum(outcome*probability for outcome, probability in zip(outcomes, probabilities))
