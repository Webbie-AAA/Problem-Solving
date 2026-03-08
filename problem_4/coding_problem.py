def solution(s):
    list_of_pairs = []
    if len(s) % 2 != 0:
        s += "_"
    for i in range(0, len(s)+1):
        if i % 2 == 0 and i > 0:
            list_of_pairs.append(s[i-2:i])
    return list_of_pairs


# It worked - 104 tests passed.


# Someone else's solution:
# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result
