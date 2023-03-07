from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))
myDeque = deque()

for i in range(N):
    now = A[i]
    while myDeque and myDeque[-1][1] >= now:
        myDeque.pop()
    myDeque.append((i, A[i]))

    nowIdx = myDeque[0][0]
    if nowIdx <= i - L:
        myDeque.popleft()

    print(myDeque[0][1], end=' ')



