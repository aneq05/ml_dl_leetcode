# def marginalize_rows(joint):
#     result = []
#     elem_sum = 0
#     for row in joint:
#         for element in row:
#             elem_sum += element
#         result.append(elem_sum)
#         elem_sum = 0
#     return result

def marginalize_rows(joint):
    return [sum(row) for row in joint]
