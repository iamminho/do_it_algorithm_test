n = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for k in range(n):
    find = A[k]
    s = 0
    e = n - 1
    while s < e:
        if A[s] + A[e] > find:
            e -= 1
        elif A[s] + A[e] < find:
            s += 1
        else:
            if s != k and e != k:
                count += 1
                break
            elif s == k:
                s += 1
            elif e == k:
                e -= 1

print(count)