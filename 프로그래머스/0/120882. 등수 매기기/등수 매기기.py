def solution(score):
    totals = [sum(s) for s in score]
    ranked = sorted(totals, reverse=True)
    return [ranked.index(t) + 1 for t in totals]