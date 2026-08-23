#VERSION 1:

# def mean_reciprocal_rank(relevant_sets, rankings):
#     scores = []

#     for relevant_set, ranking in zip(relevant_sets, rankings):
#         score = 0

#         for rank, item in enumerate(ranking, start=1):
#             if item in relevant_set:
#                 score = 1/rank
#                 break

#         scores.append(score)

#     return sum(scores) / len(scores)

#VERSION 2:

def mean_reciprocal_rank(relevant_sets, rankings):
    scores = []

    for relevant, ranking in zip(relevant_sets, rankings):
        rank = next(
            (i for i, item in enumerate(ranking, start=1) if item in relevant),
            None
        )

        scores.append(0 if rank is None else 1 / rank)

    return sum(scores) / len(scores)