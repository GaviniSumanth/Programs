def minimax(depth, index, max_turn, scores, target_depth):
    if depth == target_depth:
        return scores[index]
    if max_turn:
        return max(
            minimax(depth + 1, index * 2, False, scores, target_depth),
            minimax(depth + 1, index * 2 + 1, False, scores, target_depth),
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, scores, target_depth),
            minimax(depth + 1, index * 2 + 1, True, scores, target_depth),
        )


# scores = [3, 6, 9, 5, 12, 7, 6, 2, 4]
# tree_depth = 2
# print(minimax(0, 0, True, scores, tree_depth))

MIN = -1000
MAX = 1000


def alpha_beta_pruning(depth, index, max_turn, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[index]
    if max_turn:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta_pruning(
                depth + 1, index * 2 + i, False, scores, alpha, beta, max_depth
            )
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta_pruning(
                depth + 1, index * 2 + i, True, scores, alpha, beta, max_depth
            )
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
    return best


# scores = [3, 6, 4, 7, 5, 4, 2, 16, 4]
# print(
#     "The optimal value is :",
#     alpha_beta_pruning(0, 0, True, scores, MIN, MAX, 2),
# )

# scores = [12, 7, 6, 2, 4, 7, 5, 4, 2, 16, 2, 19]
# print("The optimal value is :", alpha_beta_pruning(0, 0, True, scores, MIN, MAX, 3))

# scores = [3, 6, 9, 5, 12, 7, 6, 2, 4, 7, 5, 4, 2, 16, 2, 19]
# print("The optimal value is :", alpha_beta_pruning(0, 0, True, scores, MIN, MAX, 4))

# scores = [
#     6,
#     3,
#     11,
#     2,
#     14,
#     15,
#     19,
#     23,
#     6,
#     9,
#     5,
#     12,
#     9,
#     6,
#     2,
#     4,
#     7,
#     5,
#     3,
#     8,
#     9,
#     7,
#     3,
#     19,
#     12,
#     19,
#     4,
# ]
# print("The optimal value is :", alpha_beta_pruning(0, 0, True, scores, MIN, MAX, 5))
