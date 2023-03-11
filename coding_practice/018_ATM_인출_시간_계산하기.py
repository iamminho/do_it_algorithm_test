N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            tmp = A.pop(i)
            A.insert(j, tmp)
            break

sumNumber = 0
for i in range(N):
    sumNumber += A[i]
    A[i] = sumNumber

print(sum(A))

