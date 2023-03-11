N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

for i in range(N):
    for j in range(N - i -1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for num in A:
    print(num)




