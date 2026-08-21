def attended_context(weights, visual_tokens):
    return [
        sum(weight*token[i] for weight, token in zip(weights, visual_tokens))
        for i in range(len(visual_tokens[0]))
    ]
