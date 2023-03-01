n = int(input())
scores = list(map(int, input().split()));
max_scores = max(scores)
sum_scores = 0;

def calculator(scores, max, n):
    return sum(scores) * 100 / max / n

print(calculator(scores, max_scores, n))

