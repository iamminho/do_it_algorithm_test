import math, sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
numbers = [2, 3, 5, 7]
N = int(input())

def DFS(layer, number):
    if layer == N:
        print(number)
    else:
        tmp = number * 10
        for i in range(10):
            tmp += 1
            if isPrime(tmp):
                DFS(layer + 1, tmp)
            else:
                continue

def isPrime(num):
    sqrt = math.ceil(math.sqrt(num))

    for i in range(2, sqrt + 1):
        if num % i == 0:
            return False
    return True

for i in numbers:
    DFS(1, i)


