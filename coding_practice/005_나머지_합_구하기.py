# page 52~53참조
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(0, n):
    remain = S[i] % m
    if remain == 0:
        answer += 1
    C[remain] += 1

for i in range(0, m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)