import sys

def calculate_scores(scores: list):
    matched_problems_scores = {}
    for i, score in enumerate(scores, start=1):
        matched_problems_scores[i] = score

    scores.sort(reverse=True)
    total_score = sum(scores[:5])
    included_problems = [str(problem) for problem, score in matched_problems_scores.items() if score in scores[:5]]
    return total_score, included_problems


if __name__ == "__main__":
    scores = []
    for _ in range(8):
        scores.append(int(sys.stdin.readline()))
    total_score, included_problems = calculate_scores(scores)
    print(total_score)
    print(' '.join(included_problems))
