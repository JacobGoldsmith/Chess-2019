# import random
# # alpha_histogram = [[0 for i in range(8)] for j in range(4)]
# depth = 1


# def recursion(depth):
#     #DEPTH CONDITION
#     if depth > 3:
#         #GIVE EVALUATION SCORE
#         return random.randint(1,900)
#     #MAKE MOVE, RECURSIVE RETURN MAX EVAL SCORE, UNDO MOVE
#     #if depth !=1:
#     histogram = [[0 for i in range(8)] for j in range(4)]
#     for x in range(len(histogram)):
#         for y in range(len(histogram[x])):
#             histogram[x][y] += recursion(depth+1)
#     print(depth)
#     print(histogram)
#     return max(max(i) if isinstance(i, list) else i for i in histogram)

# recursion(depth)
a = set([1, 2, 3, 5, 6, 7, 8])
b = set([9, 10, 11, 12, 13, 4])
c = set([14, 15, 11, 16, 17])
for x in a | b |c:
    print(x)