# def causal_mask(n):
#     result = []
#     for i in range(n):
#         row_list = []
#         for j in range(n):
#             if (j <= i):
#                 row_list.append(1)
#             else:
#                 row_list.append(0)
#         result.append(row_list)

#     return result
            
def causal_mask(n):
    return [[1 if j <= i else 0 for j in range(n)] for i in range(n)]
