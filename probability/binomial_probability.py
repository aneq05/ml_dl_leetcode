import math

def binomial_probability(trials, successes, p):
    arrange = math.factorial(trials)/(math.factorial(successes) * math.factorial(trials - successes))
    one_path = p ** successes * (1-p) ** (trials - successes)
    return arrange*one_path
