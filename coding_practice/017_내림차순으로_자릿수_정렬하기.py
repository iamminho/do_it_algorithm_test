A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i + 1, len(A)):
        if int(A[j]) > int(A[Max]):
            Max = j
    if int(A[i]) < int(A[Max]):
        A[i], A[Max] = A[Max], A[i]

print("".join(A))
