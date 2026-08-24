import math

def softmax(logits):
    # stable softmax
    return [
        math.exp(logit - max(logits)) / (sum(math.exp(x-max(logits)) for x in logits)) 
        for logit in logits
    ]
