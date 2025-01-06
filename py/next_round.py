def participants_selected(n, k, scores):
    #   Participants who got more marks for the person at kth place are selected
    kth_score = scores[k - 1]

    # Participants which are selected
    selected_participants = sum(score >= kth_score and score > 0 for score in scores)

    return selected_participants


n, k = map(int, input().split())
scores = list(map(int, input().split()))
result = participants_selected(n, k, scores)
print(result)
