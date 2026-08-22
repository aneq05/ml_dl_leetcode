def apply_repetition_penalty(logits, generated_ids, penalty):
    if len(generated_ids) == 0:
        return logits
    else:
        for index in set(generated_ids):
            if 0 <= index < len(logits):
                if logits[index] > 0:
                    logits[index] /= penalty
                else:
                    logits[index] *= penalty
    return logits