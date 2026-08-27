def discounted_return(rewards, gamma):
    discount = 0   
    for i, row in enumerate(rewards):
        discount += row*(gamma ** i)
    return discount
