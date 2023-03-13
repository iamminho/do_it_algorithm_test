import sys
sys.setrecursionlimit(10 ** 6)
# 파이썬 기본 재귀의 깊이는 1000으로 매우 얕은 편이다. 그러므로 필수로 설정해두도록 하자
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

for num in range(1, n + 1):
    if not visited[num]:
        count += 1
        DFS(num)

print(count)

