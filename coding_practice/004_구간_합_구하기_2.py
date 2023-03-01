# function
def sum_of_section(D, N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

def calculation(D):
    x1, y1, x2, y2 = map(int, input("질문을 4개 입력하세요.\n").split())
    return D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]

# calculate

N, M = map(int, input("N, M의 값을 입력하세요.\n").split())
A = [[0] * (N + 1)]
D = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    A_row = [0] + [int(x) for x in input("2차원 배열을 입력하세요.\n").split()]
    A.append(A_row)

sum_of_section(D, N)

for i in range(M):
    print(calculation(D))



# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# A = [[0] * (n + 1)]
# D = [[0] * (n + 1) for _ in range(n + 1)]
#
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
#     print(result)