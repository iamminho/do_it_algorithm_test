N = int(input())
A = list(map(int, input().split()))
stack = []
Result = [0] * N
for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        top = stack.pop()
        Result[top] = A[i]
    stack.append(i)

while stack:
    top = stack.pop()
    Result[top] = -1

print(*Result)