def advantages_from_returns(returns, values):
    result = []
    for return_n, value in zip(returns, values):
        result.append(return_n - value)
    return result

